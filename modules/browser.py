import webbrowser

def open_google():
    webbrowser.open("https://www.google.com")


def open_youtube():
    webbrowser.open("https://www.youtube.com")


def open_github():
    webbrowser.open("https://github.com")


def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")