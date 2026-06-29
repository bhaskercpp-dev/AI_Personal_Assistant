from datetime import datetime

def current_time():
    return datetime.now().strftime("%I:%M %p")


def current_date():
    return datetime.now().strftime("%d-%m-%Y")


def current_day():
    return datetime.now().strftime("%A")


def greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "Good Morning"

    elif hour < 17:
        return "Good Afternoon"

    else:
        return "Good Evening"