# modules/system.py

import os


# def shutdown():
#     """Shutdown the computer after 5 seconds."""
#     os.system("shutdown /s /t 5")


# def restart():
#     """Restart the computer after 5 seconds."""
#     os.system("shutdown /r /t 5")


def cancel_shutdown():
    """Cancel a scheduled shutdown/restart."""
    os.system("shutdown /a")


def lock_pc():
    """Lock the Windows computer."""
    os.system("rundll32.exe user32.dll,LockWorkStation")


def sleep_pc():
    """Put the computer to sleep."""
    os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")


# ---------------------------
# Placeholder Volume Controls
# ---------------------------

def volume_up():
    print("Increasing volume...")


def volume_down():
    print("Decreasing volume...")


def mute():
    print("Muting system...")

if __name__ == "__main__":
    print("System module started...")

    # Uncomment only ONE function at a time

    # cancel_shutdown()
    lock_pc()
    # sleep_pc()
    # volume_up()
    # volume_down()
    # mute()