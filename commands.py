import os
import webbrowser

def handle_command(command):
    command = command.lower()

    if "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad."

    elif "open browser" in command:
        webbrowser.open("https://www.google.com")
        return "Opening your browser."

    elif "shutdown" in command:
        return "shutdown"  # Signal to exit

    return None  # No command matched
