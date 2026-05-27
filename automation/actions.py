import subprocess


def open_browser():
    subprocess.Popen(["firefox"])


def open_vscode():
    subprocess.Popen(["code"])


def open_terminal():
    subprocess.Popen(["gnome-terminal"])


def coding_workspace():
    subprocess.Popen(["code"])
    subprocess.Popen(["firefox"])
    subprocess.Popen(["gnome-terminal"])