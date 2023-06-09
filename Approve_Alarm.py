import tkinter as tk
import tkinter.font as tkFont

class Approve_Alarm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='white')
# Set up the main window
        self.title("ALERT")
        self.geometry("1400x800")
  


        Text_label_font= ("Times", 20)
        H1_label_font=("Times", 40)
        H2_label_font=("Times", 30)
        text_color= "#000000"
        background= "#FFFFFF"
      

        #cam stream
        label_stream=tk.Label(self, text="camera stream", font=H2_label_font,fg=background, bg=text_color, justify="center")
        label_stream.place(x=200,  y=65, width=1197, height=736)

        #Approve btn
        btn_approve = tk.Button(self, text="Real-Time Alert", font=Text_label_font,borderwidth="2px", command=self.btn_approve_command,bg="red",highlightbackground="red")
        btn_approve.place(x=20,  y=120,width=141,height=30)

        #false alarm btn
        btn_false = tk.Button(self, text="False Alarm", font=Text_label_font,borderwidth="2px", command=self.btn_false_command,bg="green",highlightbackground="green")
        btn_false.place(x=20,  y=160,width=141,height=30)


        #header
        label_header = tk.Label(self, text="ALARM!!!  Confirm or deny the event using the buttons", font=H1_label_font,fg=text_color, bg=background,justify="center")
        label_header.place(x=10, y=10)


    def btn_approve_command(self):
        print("command")
    def btn_false_command(self):
        print("command")

if __name__ == '__main__':
    alarmPG = Approve_Alarm()
    alarmPG.mainloop() 





