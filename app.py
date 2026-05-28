from flask import Flask, render_template, request, jsonify
import requests

from automation.actions import *

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"


# -----------------------------------
# LOCAL COMMAND ROUTER
# -----------------------------------

def detect_local_command(message):

    msg = message.lower()


    # BROWSER

    if "github" in msg:
        return "github"

    if "instagram" in msg:
        return "instagram"

    if "youtube" in msg:
        return "youtube"


    # APPS

    if "vscode" in msg or "vs code" in msg:
        return "vscode"

    if "terminal" in msg:
        return "terminal"

    if "spotify" in msg:
        return "spotify"


    # WORKSPACES

    if "coding workspace" in msg:
        return "coding_workspace"


    return None


# -----------------------------------
# OLLAMA CHAT
# -----------------------------------

def ask_ai(prompt):

    response = requests.post(

        OLLAMA_URL,

        json={

            "model": "tinyllama",

            "prompt": prompt,

            "stream": False

        }

    )

    data = response.json()

    return data["response"]


# -----------------------------------
# ROUTES
# -----------------------------------

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    user_message = data.get("message", "")

    # -----------------------------------
    # LOCAL COMMAND DETECTION
    # -----------------------------------

    intent = detect_local_command(user_message)

    # -----------------------------------
    # EXECUTE COMMANDS
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
        # FALLBACK TO AI
        # -----------------------------------

        result = ask_ai(user_message)

    return jsonify({
        "response": result
    })


# -----------------------------------
# MAIN
# -----------------------------------

if __name__ == "__main__":

    app.run(debug=True)