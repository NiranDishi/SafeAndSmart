import tkinter as tk
from tkinter import ttk
import cv2
import urllib.request
import urllib.error


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='white')
        
        # Set up the main window
        self.title("Safe and Smart")
        self.geometry("1400x800")
        
        # Create the tabs
        self.notebook = ttk.Notebook(self)
        
        # Add the tabs
        self.tab1 = tk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Tab 1")
        
        self.tab2 = tk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Tab 2")
        
        # Pack the notebook
        self.notebook.pack(expand=True, fill="both")
        
        # Load the content for each tab
        self.load_tab1()
        self.load_tab2()
        
        # Start the camera input and internet connection check
        self.check_camera_input()
        self.check_internet_connection()
        
    def load_tab1(self):
        # Load the content for Tab 1 from another file
        from Pool_Stream import PoolStream
        tab1_content = PoolStream(self.tab1)
        
    def load_tab2(self):
        # Load the content for Tab 2 from another file
        from User_Settings import UserSettings
        tab2_content = UserSettings(self.tab2)
        
    def check_camera_input(self):
        # set up the camera capture
        cap = cv2.VideoCapture(0)

        # read a frame from the camera
        ret, frame = cap.read()

        # if the frame is None, display an error message
        if frame is None:
            camera_error_popup()

        # release the camera capture
        cap.release()

        # call this function again in 1 second
        self.after(1000, self.check_camera_input)

    def check_internet_connection(self):
        try:
            # try to open a connection to google.com
            urllib.request.urlopen("https://www.google.com")
        except urllib.error.URLError:
            # If the connection is lost, show the error popup
            internet_error_popup()

        # call this function again in 1 second
        self.after(1000, self.check_internet_connection)

        
def internet_error_popup():
    popup = tk.Toplevel()
    popup.title("Internet Connection Error")
    popup.geometry("400x200")
    popup.resizable(False, False)
    
    label1 = tk.Label(popup, text="Internet connection is lost", font=("Helvetica", 16), pady=20)
    label1.pack()
    
    button_ok = tk.Button(popup, text="OK", font=("Helvetica", 14), width=10, command=popup.destroy)
    button_ok.pack(pady=20)
    
    popup.focus_set()
    popup.grab_set()
    popup.wait_window()
    
    
def camera_error_popup():
    popup = tk.Toplevel()
    popup.title("Camera Input Error")
    popup.geometry("400x200")
    popup.resizable(False, False)
    
    label1 = tk.Label(popup, text="Camera input is not stable or having hard time", font=("Helvetica", 16), pady=20)
    label1.pack()
    
    button_ok = tk.Button(popup, text="OK", font=("Helvetica", 14), width=10, command=popup.destroy)
    button_ok.pack(pady=20)
    
    popup.focus_set()
    popup.grab_set()
    popup.wait_window()

    
if __name__ == '__main__':
    app = App()
    app.mainloop()
