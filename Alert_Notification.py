import tkinter.messagebox as messagebox
import subprocess
import simpleaudio as sa
import threading
import ctypes
import platform
from twilio.rest import Client

def alarm_desktop():
    # Define the path to the alarm sound file
    alarm_file_path = "alarm.wav"
    message = "ALARM!\nDanger in the pool!!"
    global process
    def alarm_WindowsOS():

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
        global process
        #---------alarm on mac desktop
        wave_obj = sa.WaveObject.from_wave_file(alarm_file_path)

        subprocess.run(['osascript', '-e', 'set volume output volume 10'])

        # Define a function to play the alarm sound
        def play_sound():
            global play_obj
            play_obj = wave_obj.play()

        # Create a thread to play the alarm sound
        sound_thread = threading.Thread(target=play_sound)

        sound_thread.start()

        button = messagebox.showwarning("Alert", message, detail="OPEN CAMERA", type="ok")

        if button == "OK":
            button = "OK"

        run_script()


    # Define a function to run another Python script
    def run_script():
        global process
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
        import winsound
        import win32api
        alarm_WindowsOS()

    # Otherwise, print an error message
    else:
        print("Error: unsupported operating system")






import subprocess
def call_alarm(phone_number):
    account_sid = 'ACf5952cb9a8c5f6c811b2584bc8d20783'
    auth_token = 'b4591c476c7f568f54002b4158e72c20'
    client = Client(account_sid, auth_token)
    call = client.calls.create(
        from_='+16203373912',
        to=phone_number,
        url='https://handler.twilio.com/twiml/EH2fa2f3f00f72453d700e74a0b875769b'
    )


def call_mac():
    import subprocess
    import time
    import AppKit

    # set the phone number or email address to call
    destination = "+972546245600"

    # open the FaceTime app and start the call
    subprocess.run(["open", "facetime://" + destination])

    # wait for the call to be answered
    print("Waiting for call to be answered...")
    while True:
        output = subprocess.check_output(["pgrep", "FaceTime"])
        if output:
            break
        time.sleep(1)

    # play the text-to-speech message
    speech = AppKit.NSSpeechSynthesizer.alloc().initWithVoice_(None)
    speech.startSpeakingString_("This is an alarm")

    # wait for the call to end
    input("Press enter to end the call")

    # end the call by quitting the FaceTime app
    subprocess.run(["killall", "FaceTime"])








#approve/deny alarm
alarm_desktop()