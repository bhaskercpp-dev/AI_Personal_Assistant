from modules.browser import (
    open_google,
    open_youtube,
    open_github,
    search_google
)

from modules.voice import speak


def process_command(command):
    """
    Process the user's voice command and call the appropriate module.
    """

    if not command:
        return

    command = command.lower()

    # ---------------- Browser Commands ---------------- #

    if "open google" in command:
        speak("Opening Google")
        open_google()

    elif "open youtube" in command:
        speak("Opening YouTube")
        open_youtube()

    elif "open github" in command:
        speak("Opening GitHub")
        open_github()

    elif command.startswith("search "):
        query = command.replace("search", "", 1).strip()

        if query:
            speak(f"Searching Google for {query}")
            search_google(query)
        else:
            speak("Please tell me what to search.")

    # ---------------- Exit ---------------- #

    elif "exit" in command or "stop" in command or "goodbye" in command:
        speak("Goodbye. Have a nice day.")
        exit()

    # ---------------- Unknown Command ---------------- #

    else:
        speak("Sorry, I don't understand that command.")