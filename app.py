from flask import Flask, render_template, request, jsonify
import requests
import psutil
import logging

from automation.actions import *

# -----------------------------------
# FLASK APP
# -----------------------------------

app = Flask(__name__)

# -----------------------------------
# DISABLE FLASK TERMINAL SPAM
# -----------------------------------

log = logging.getLogger('werkzeug')
log.disabled = True

# -----------------------------------
# OLLAMA CONFIG
# -----------------------------------

OLLAMA_URL = "http://localhost:11434/api/generate"

# -----------------------------------
# LIVE UI VARIABLES
# -----------------------------------

latest_user_message = ""
latest_ai_response = ""

# -----------------------------------
# LOCAL COMMAND ROUTER
# -----------------------------------

def detect_local_command(message):

    msg = message.lower()

    # -----------------------------------
    # BROWSER
    # -----------------------------------

    if "github" in msg:
        return "github"

    elif "instagram" in msg:
        return "instagram"

    elif "youtube" in msg:
        return "youtube"

    # -----------------------------------
    # APPS
    # -----------------------------------

    elif "vscode" in msg or "vs code" in msg:
        return "vscode"

    elif "terminal" in msg:
        return "terminal"

    elif "spotify" in msg:
        return "spotify"

    # -----------------------------------
    # WORKSPACES
    # -----------------------------------

    elif "coding workspace" in msg:
        return "coding_workspace"

    return None

# -----------------------------------
# OLLAMA AI CHAT
# -----------------------------------

def ask_ai(prompt):

    try:

        response = requests.post(

            OLLAMA_URL,

            json={

                "model": "tinyllama",

                "prompt": f"""
                You are VYOM, an advanced desktop AI assistant.

Rules:
- Keep replies under 3 lines
- Be modern and concise
- Never repeat responses
- Speak naturally
- Do not give outdated information
- Avoid long paragraphs

User:
{prompt}

VYOM:
""",

                "stream": False

            },

            timeout=60

        )

        data = response.json()

        return data.get("response", "No response from AI.")

    except Exception as e:

        print("OLLAMA ERROR:", e)

        return "AI system offline."
# -----------------------------------
# HOME PAGE
# -----------------------------------

@app.route("/")
def home():

    return render_template("index.html")

# -----------------------------------
# CHAT API
# -----------------------------------

@app.route("/ask", methods=["POST"])
def ask():

    global latest_user_message
    global latest_ai_response

    try:

        data = request.get_json()

        user_message = data.get("message", "")

        latest_user_message = user_message

        intent = detect_local_command(user_message)

        # -----------------------------------
        # COMMAND EXECUTION
        # -----------------------------------

        if intent == "github":

            open_github()

            result = "Opening GitHub..."

        elif intent == "instagram":

            open_instagram()

            result = "Opening Instagram..."

        elif intent == "youtube":

            open_youtube()

            result = "Opening YouTube..."

        elif intent == "vscode":

            open_vscode()

            result = "Opening VS Code..."

        elif intent == "terminal":

            open_terminal()

            result = "Opening terminal..."

        elif intent == "spotify":

            open_spotify()

            result = "Launching Spotify..."

        elif intent == "coding_workspace":

            coding_workspace()

            result = "Launching coding workspace..."

        else:

            # -----------------------------------
            # AI FALLBACK
            # -----------------------------------

            result = ask_ai(user_message)

        latest_ai_response = result

        return jsonify({

            "response": result

        })

    except Exception as e:

        print("ASK ROUTE ERROR:", e)

        return jsonify({

            "response": "System error occurred."

        })

# -----------------------------------
# SYSTEM STATS API
# -----------------------------------

@app.route("/system")
def system_data():

    try:

        cpu = psutil.cpu_percent(interval=0.5)

        ram = psutil.virtual_memory().percent

        return jsonify({

            "cpu": cpu,
            "ram": ram

        })

    except Exception as e:

        print("SYSTEM API ERROR:", e)

        return jsonify({

            "cpu": 0,
            "ram": 0

        })

# -----------------------------------
# LIVE FEED API
# -----------------------------------

@app.route("/live-feed")
def live_feed():

    global latest_user_message
    global latest_ai_response

    return jsonify({

        "user": latest_user_message,
        "ai": latest_ai_response

    })

# -----------------------------------
# MAIN
# -----------------------------------

if __name__ == "__main__":

    print("\n===================================")
    print(" VYOM AI ASSISTANT STARTED ")
    print(" http://127.0.0.1:5000 ")
    print("===================================\n")

    app.run(

        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False

    )