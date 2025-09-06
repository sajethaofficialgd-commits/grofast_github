import pyautogui
import time
import os
import subprocess
import sys

# File name and path
file_name = "firstautomation.txt"
file_path = os.path.join(os.getcwd(), file_name)

def open_notepad(path=None):
    """Open Notepad, optionally with an existing file."""
    if path:
        subprocess.Popen(["notepad", path])
    else:
        subprocess.Popen("notepad")
    time.sleep(1.5)  # Give Notepad enough time to open

def write_text(user_text):
    """Write or append text in Notepad."""
    if not os.path.exists(file_path):
        # Create and write
        open_notepad()
        pyautogui.typewrite(user_text)
        pyautogui.hotkey("ctrl", "s")
        time.sleep(0.8)
        pyautogui.typewrite(file_name)
        pyautogui.press("enter")
        print(f"✅ File created and saved as: {file_name}")
    else:
        # Append new line
        open_notepad(file_path)
        time.sleep(1)
        pyautogui.hotkey("ctrl", "end")  # Move to end
        pyautogui.press("enter")         # New line
        pyautogui.typewrite(user_text)
        pyautogui.hotkey("ctrl", "s")
        print(f"✅ Text appended to: {file_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Please provide text to write. Example:")
        print(f"python {sys.argv[0]} \"Your text here\"")
        sys.exit(1)

    text_to_write = sys.argv[1]
    write_text(text_to_write)
