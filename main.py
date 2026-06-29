from modules.voice import listen, speak

from modules.browser import (
    open_google,
    open_youtube,
    open_github,
    search_google
)

from modules.apps import (
    open_notepad,
    open_calculator,
    open_cmd,
    open_paint,
    open_explorer,
    open_chrome,
    open_vscode
)

from modules.system import (
    shutdown,
    restart,
    lock_pc
)


def main():

    print("=" * 40)
    print("AI Personal Assistant Started")
    print("=" * 40)

    speak("Hello Bhaskar. I am your AI Personal Assistant.")

    while True:

        command = listen()

        if not command:
            continue

        command = command.lower()

        if "google" in command:
            open_google()

        elif "youtube" in command:
            open_youtube()

        elif "github" in command:
            open_github()

        elif "notepad" in command:
            open_notepad()

        elif "calculator" in command:
            open_calculator()

        elif "cmd" in command:
            open_cmd()

        elif "shutdown" in command:
            shutdown()

        elif "restart" in command:
            restart()

        elif "lock" in command:
            lock_pc()

        elif "search" in command:
            query = command.replace("search", "").strip()
            search_google(query)

        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

        else:
            speak("I didn't understand that. Please try again.")


if __name__ == "__main__":
    main()