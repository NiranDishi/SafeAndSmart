import tkinter.messagebox as messagebox
import subprocess
import simpleaudio as sa
import threading
import ctypes
import platform
from twilio.rest import Client
import subprocess

def warning():
    # Define the path to the alarm sound file
    alarm_file_path = "warning.wav"  # Use a WAV audio file instead of MP3

    message = "WARNING!\nDanger in the pool!!"
    process = None  # Initialize the process variable
    play_obj = [None]  # Use a mutable object to store play_obj

    def alarm_WindowsOS():
        import winsound
        import win32api

        # Define a function to play the alarm sound
        def play_sound():
            winsound.PlaySound(alarm_file_path, winsound.SND_FILENAME)

        # Create a thread to play the alarm sound
        sound_thread = threading.Thread(target=play_sound)

        # Set the volume to 10%
        win32api.SendMessage(-1, win32api.WM_APPCOMMAND, 0, win32api.APPCOMMAND_VOLUME_UP * 0x10000 + 0x0)

        sound_thread.start()

        # Show a message box
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, message, "Alert", 0x40 | 0x1)

        run_script()

    def alarm_MacOS():
        nonlocal process  # Use nonlocal to access the outer process variable
        # ---------alarm on mac desktop
        wave_obj = sa.WaveObject.from_wave_file(alarm_file_path)

        subprocess.run(['osascript', '-e', 'set volume output volume 10'])

        # Define a function to play the alarm sound
        def play_sound():
            play_obj[0] = wave_obj.play()

        # Create a thread to play the alarm sound
        sound_thread = threading.Thread(target=play_sound)

        sound_thread.start()

        button = messagebox.showwarning("WARNING", message, detail="OPEN POOL CAMERA", type="ok")

        if button == "OK":
            button = "OK"

        run_script()

    # Define a function to run another Python script
    def run_script():
        nonlocal process  # Use nonlocal to access the outer process variable
        if process is not None:
            process.kill()
        process = subprocess.Popen(['python3', 'Approve_Alarm.py'])

    # Get the operating system
    os_name = platform.system()

    # Check if the operating system is macOS
    if os_name == "Darwin":
        process = None
        # Activate the alarm for macOS
        alarm_MacOS()

    # Check if the operating system is Windows
    elif os_name == "Windows":
        # Activate the alarm for Windows
        alarm_WindowsOS()

    # Otherwise, print an error message
    else:
        print("Error: unsupported operating system")

warning()
