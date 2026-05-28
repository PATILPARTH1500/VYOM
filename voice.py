import queue
import sounddevice as sd
import vosk
import json
import pyttsx3
import requests
import time

# --------------------------------
# SETTINGS
# --------------------------------

MODEL_PATH = "vosk-model-small-en-us-0.15"

q = queue.Queue()

engine = pyttsx3.init()

listening_for_command = False
is_speaking = False

# Prevent repeated commands
last_command = ""
last_command_time = 0

# --------------------------------
# SPEAK FUNCTION
# --------------------------------

def speak(text):

    global is_speaking

    is_speaking = True

    print(f"\nVYOM: {text}\n")

    engine.say(text)
    engine.runAndWait()

    # Small cooldown so mic doesn't capture speaker audio
    time.sleep(1.5)

    is_speaking = False

# --------------------------------
# AUDIO CALLBACK
# --------------------------------

def callback(indata, frames, time_info, status):

    if status:
        print(status)

    # Don't capture audio while speaking
    if not is_speaking:
        q.put(bytes(indata))

# --------------------------------
# LOAD MODEL
# --------------------------------

print("Loading VOSK model...")

model = vosk.Model(MODEL_PATH)

recognizer = vosk.KaldiRecognizer(model, 16000)

print("\n===================================")
print(" VYOM VOICE SYSTEM STARTED ")
print(" Wake Word: HEY VYOM ")
print("===================================\n")

# --------------------------------
# MICROPHONE STREAM
# --------------------------------

with sd.RawInputStream(

    samplerate=16000,
    blocksize=4000,
    dtype='int16',
    channels=1,
    callback=callback

):

    while True:

        # Prevent CPU overuse
        time.sleep(0.05)

        # Ignore while speaking
        if is_speaking:
            continue

        data = q.get()

        if recognizer.AcceptWaveform(data):

            result = json.loads(recognizer.Result())

            text = result.get("text", "").lower().strip()

            if text == "":
                continue

            # --------------------------------
            # REMOVE DUPLICATE DETECTIONS
            # --------------------------------

            current_time = time.time()

            if (
                text == last_command and
                current_time - last_command_time < 4
            ):
                continue

            last_command = text
            last_command_time = current_time

            print("YOU:", text)

            # --------------------------------
            # WAKE WORD
            # --------------------------------

            if "hey vyom" in text:

                listening_for_command = True

                speak("Yes sir")

                continue

            # --------------------------------
            # COMMAND MODE
            # --------------------------------

            if listening_for_command:

                listening_for_command = False

                try:

                    response = requests.post(

                        "http://127.0.0.1:5000/ask",

                        json={
                            "message": text
                        },

                        timeout=30

                    )

                    ai = response.json()

                    reply = ai.get(
                        "response",
                        "I could not process that."
                    )

                    speak(reply)

                except Exception as e:

                    print("ERROR:", e)

                    speak("Connection to system failed")