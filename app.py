from flask import Flask, render_template, request, jsonify
import requests

from automation.actions import *

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_ai(prompt):

    system_prompt = f"""
You are an AI intent classifier.

Convert user request into ONLY one of these commands:

- browser
- vscode
- terminal
- coding_workspace
- unknown

User request:
{prompt}

Return only command word.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "tinyllama",
            "prompt": system_prompt,
            "stream": False
        }
    )

    data = response.json()

    return data["response"].strip().lower()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    print("DATA:", data)

    user_message = data.get("message", "")

    intent = ask_ai(user_message)

    result = ""

    if "browser" in intent:
        open_browser()
        result = "Opening browser..."

    elif "vscode" in intent:
        open_vscode()
        result = "Opening VS Code..."

    elif "terminal" in intent:
        open_terminal()
        result = "Opening terminal..."

    elif "coding_workspace" in intent:
        coding_workspace()
        result = "Launching coding workspace..."

    else:
        result = "Command not recognized."

    return jsonify({
        "response": result
    })


if __name__ == "__main__":
    app.run(debug=True)