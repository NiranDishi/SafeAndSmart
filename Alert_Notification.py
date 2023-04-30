import tkinter.messagebox as messagebox
import subprocess
import simpleaudio as sa
import threading

#---------alarm on mac desktop
wave_obj = sa.WaveObject.from_wave_file("alarm.wav")
play_obj = None
process = None
subprocess.run(['osascript', '-e', 'set volume output volume 30'])
# Define a function to run another Python script
def run_script():
    global process
    if process is not None:
        process.kill()
    process = subprocess.Popen(['python3', 'main.py'])

# Define a function to play the alarm sound
def play_sound():
    global play_obj
    play_obj = wave_obj.play()

# Create a thread to play the alarm sound
sound_thread = threading.Thread(target=play_sound)

# Display a message box with a button and play a sound
message = "ALARM!\nDanger in the pool!!"
sound_thread.start()

button = messagebox.showwarning("Alert", message, detail="OPEN CAMERA", type="ok")

if button == "OK":
    button = "OK"

run_script()
#----------end of alarm on mac desktop

#alarm while loop
#alarm windows
#notification for phones
#approve/deny alarm