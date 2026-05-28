import subprocess
import webbrowser
import os


def execute_command(command):

    command = command.lower()


    # -----------------------------
    # OPEN APPLICATIONS
    # -----------------------------

    if "open vscode" in command:

        subprocess.Popen(["code"])

        return "Opening VS Code."


    elif "open terminal" in command:

        subprocess.Popen(["gnome-terminal"])

        return "Opening terminal."


    elif "open spotify" in command:

        subprocess.Popen(["spotify"])

        return "Launching Spotify."


    elif "open files" in command:

        subprocess.Popen(["nautilus"])

        return "Opening file manager."


    elif "open monitor" in command:

        subprocess.Popen(["gnome-system-monitor"])

        return "Opening system monitor."


    # -----------------------------
    # WEBSITES
    # -----------------------------

    elif "open github" in command:

        webbrowser.open("https://github.com/PATILPARTH1500")

        return "Opening GitHub."


    elif "open instagram" in command:

        webbrowser.open("https://www.instagram.com/parth_patil.mp4/")

        return "Opening Instagram."


    elif "open youtube" in command:

        webbrowser.open("https://youtube.com")

        return "Opening YouTube."


    # -----------------------------
    # WORKSPACES
    # -----------------------------

    elif "start coding workspace" in command:

        subprocess.Popen(["code"])

        subprocess.Popen(["gnome-terminal"])

        webbrowser.open("https://github.com/PATILPARTH1500")

        return "Coding workspace started."


    # -----------------------------
    # SYSTEM
    # -----------------------------

    elif "shutdown pc" in command:

        os.system("shutdown now")

        return "Shutting down system."


    elif "restart pc" in command:

        os.system("reboot")

        return "Restarting system."


    # -----------------------------
    # UNKNOWN
    # -----------------------------

    return None