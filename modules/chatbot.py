# modules/chatbot.py

from datetime import datetime


def chatbot(command):

    command = command.lower()

    if "hello" in command:
        return "Hello Bhaskar! How can I help you?"

    elif "hi" in command:
        return "Hi! Nice to meet you."

    elif "how are you" in command:
        return "I am doing great."

    elif "your name" in command:
        return "I am your AI Personal Assistant."

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The time is {current_time}"

    elif "date" in command:
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}"

    elif "thank you" in command:
        return "You're welcome."

    elif "bye" in command:
        return "Goodbye! Have a wonderful day."

    else:
        return "Sorry, I don't understand that command yet."