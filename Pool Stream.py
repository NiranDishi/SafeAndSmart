import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1400
        height=800
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_883=tk.Label(root)
        GLabel_883["activeforeground"] = "#ffffff"
        GLabel_883["bg"] = "#000000"
        GLabel_883["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_883["font"] = ft
        GLabel_883["fg"] = "#ffffff"
        GLabel_883["justify"] = "center"
        GLabel_883["text"] = "Camera Stream"
        GLabel_883.place(x=170,y=40,width=1197,height=736)

        GButton_362=tk.Button(root)
        GButton_362["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_362["font"] = ft
        GButton_362["fg"] = "#000000"
        GButton_362["justify"] = "center"
        GButton_362["text"] = "Unarm Warning"
        GButton_362.place(x=10,y=40,width=141,height=66)
        GButton_362["command"] = self.GButton_362_command

        GMessage_28=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_28["font"] = ft
        GMessage_28["fg"] = "#333333"
        GMessage_28["justify"] = "center"
        GMessage_28["text"] = "Pool Stream"
        GMessage_28.place(x=720,y=10,width=80,height=25)

    def GButton_362_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
