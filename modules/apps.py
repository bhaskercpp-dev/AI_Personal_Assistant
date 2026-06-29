import os
import subprocess
from modules.voice import speak


def open_notepad():
    """Open Windows Notepad"""
    speak("Opening Notepad")
    os.system("notepad")


def open_calculator():
    """Open Windows Calculator"""
    speak("Opening Calculator")
    os.system("calc")


def open_cmd():
    """Open Command Prompt"""
    speak("Opening Command Prompt")
    os.system("start cmd") 


def open_paint():
    """Open Microsoft Paint"""
    speak("Opening Paint")
    os.system("mspaint")


def open_explorer():
    """Open File Explorer"""
    speak("Opening File Explorer")
    os.system("explorer")


def open_chrome():
    """Open Google Chrome"""

    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]

    for path in chrome_paths:
        if os.path.exists(path):
            speak("Opening Google Chrome")
            subprocess.Popen(path)
            return

    speak("Google Chrome is not installed.")


def open_vscode():
    """Open Visual Studio Code"""

    vscode_paths = [
        r"C:\Users\{}\AppData\Local\Programs\Microsoft VS Code\Code.exe".format(os.getlogin()),
        r"C:\Program Files\Microsoft VS Code\Code.exe",
    ]

    for path in vscode_paths:
        if os.path.exists(path):
            speak("Opening Visual Studio Code")
            subprocess.Popen(path)
            return

    speak("Visual Studio Code is not installed.")