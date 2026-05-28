import subprocess
import webbrowser
import os


# =========================================
# CORE LAUNCHER
# =========================================

def launch_app(command):

    try:
        subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return True

    except Exception as e:
        print("ERROR:", e)
        return False


# =========================================
# BASIC APPS
# =========================================

def open_terminal():
    return launch_app(["gnome-terminal"])


def open_vscode():
    return launch_app(["code"])


def open_spotify():
    return launch_app(["spotify"])


def open_browser():
    return launch_app(["brave-browser"])


def open_files():
    return launch_app(["nautilus"])


def open_settings():
    return launch_app(["gnome-control-center"])


def open_calculator():
    return launch_app(["gnome-calculator"])


def open_system_monitor():
    return launch_app(["gnome-system-monitor"])


# =========================================
# PERSONAL LINKS
# =========================================

def open_github():
    webbrowser.open("https://github.com/PATILPARTH1500")


def open_instagram():
    webbrowser.open("https://www.instagram.com/parth_patil.mp4/")


def open_youtube():
    webbrowser.open("https://youtube.com")


def open_chatgpt():
    webbrowser.open("https://chatgpt.com")


def open_stackoverflow():
    webbrowser.open("https://stackoverflow.com")


# =========================================
# DEVELOPMENT
# =========================================

def open_vyom_project():

    project_path = "/home/parth/Desktop/CODE PLAYGROUND/IoT PROJECTS/VYOM/VYOM"

    subprocess.Popen(["code", project_path])


def open_github_repo():

    webbrowser.open(
        "https://github.com/PATILPARTH1500"
    )


# =========================================
# SYSTEM ACTIONS
# =========================================

def lock_screen():
    return launch_app(["gnome-screensaver-command", "-l"])


def restart_pc():
    return launch_app(["reboot"])


# =========================================
# WORKSPACES
# =========================================

def coding_workspace():

    open_vyom_project()

    open_terminal()

    open_spotify()

    open_github()


def study_workspace():

    open_youtube()

    open_chatgpt()

    open_terminal()


def creator_workspace():

    open_instagram()

    open_youtube()

    open_spotify()


# =========================================
# EXTRA PRODUCTIVITY
# =========================================

def open_music():

    open_spotify()


def open_ai_tools():

    open_chatgpt()

    open_stackoverflow()


def open_socials():

    open_instagram()

    open_github()


def night_mode():

    open_spotify()

    open_terminal()


def focus_mode():

    open_vscode()

    open_spotify()

    open_terminal()