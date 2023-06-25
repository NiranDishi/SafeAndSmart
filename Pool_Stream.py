import tkinter as tk
import tkinter.font as tkFont
import subprocess
import os



class PoolStream:
    def __init__(self, parent):
        self.parent = parent
        self.parent.configure(bg='white')
        
        self.parent = parent
        self.parent.configure(bg='white')
        Text_label_font= ("Times", 20)
        H1_label_font=("Times", 40)
        H2_label_font=("Times", 30)
        text_color= "#000000"
        background= "#FFFFFF"
        

        # #cam stream
        # label_stream=tk.Label(self.parent, text="Camera Stream", font=H2_label_font,fg=background, bg=text_color, justify="center")
        # label_stream.place(x=200,  y=65, width=1197, height=736)

        #camera1 btn
        btn_cam1 = tk.Button(self.parent, text="Camera 1", font=Text_label_font,borderwidth="0px", command=self.btn_cam1_command)
        btn_cam1.place(x=525,  y=120,width=141,height=30)

        #camera2 btn
        btn_cam2 = tk.Button(self.parent, text="Camera 2", font=Text_label_font,borderwidth="0px", command=self.btn_cam2_command)
        btn_cam2.place(x=525,  y=160,width=141,height=30)


        #header
        label_header = tk.Label(self.parent, text="Pool Stream", font=H1_label_font,fg=text_color, bg=background,justify="center")
        label_header.place(x=10, y=10)


    def btn_cam1_command(self):
        original_path = os.getcwd()  # Store the original working directory
        project_path = "AI/"
        os.chdir(project_path)
        subprocess.run(["python3", "DrownDetect.py"])
        os.chdir(original_path)  # Return to the original working directory





    def btn_cam2_command(self):
        original_path = os.getcwd()  # Store the original working directory
        project_path = "AI/"
        os.chdir(project_path)
        subprocess.run(["python3", "DrownDetect2.py"])
        os.chdir(original_path)  # Return to the original working directory


