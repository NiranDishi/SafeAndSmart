import tkinter as tk
import tkinter.font as tkFont

class UserSettings:
    def __init__(self, parent):
        self.parent = parent
        self.parent.configure(bg='white')

        GLineEdit_415=tk.Entry(self.parent)
        GLineEdit_415["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_415["font"] = ft
        GLineEdit_415["fg"] = "#333333"
        GLineEdit_415["justify"] = "center"
        GLineEdit_415["text"] = "Entry"
        GLineEdit_415.place(x=180,y=170,width=70,height=25)

        GLabel_739=tk.Label(self.parent)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_739["font"] = ft
        GLabel_739["fg"] = "#333333"
        GLabel_739["justify"] = "left"
        GLabel_739["text"] = "System ID"
        GLabel_739.place(x=110,y=120,width=70,height=25)

        GLabel_214=tk.Label(self.parent)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_214["font"] = ft
        GLabel_214["fg"] = "#333333"
        GLabel_214["justify"] = "left"
        GLabel_214["text"] = "Name"
        GLabel_214.place(x=110,y=170,width=70,height=25)

        GLineEdit_785=tk.Entry(self.parent)
        GLineEdit_785["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_785["font"] = ft
        GLineEdit_785["fg"] = "#333333"
        GLineEdit_785["justify"] = "center"
        GLineEdit_785["text"] = "Entry"
        GLineEdit_785.place(x=180,y=120,width=70,height=25)

        GLabel_955=tk.Label(self.parent)
        ft = tkFont.Font(family='Times',size=20)
        GLabel_955["font"] = ft
        GLabel_955["fg"] = "#333333"
        GLabel_955["justify"] = "left"
        GLabel_955["text"] = "List of contacts"
        GLabel_955.place(x=110,y=220,width=174,height=30)

        GLineEdit_738=tk.Entry(self.parent)
        GLineEdit_738["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_738["font"] = ft
        GLineEdit_738["fg"] = "#333333"
        GLineEdit_738["justify"] = "center"
        GLineEdit_738["text"] = "Phone Number"
        GLineEdit_738.place(x=190,y=290,width=122,height=25)

        GLabel_763=tk.Label(self.parent)
        ft = tkFont.Font(family='Times',size=30)
        GLabel_763["font"] = ft
        GLabel_763["fg"] = "#333333"
        GLabel_763["justify"] = "center"
        GLabel_763["text"] = "Settings page"
        GLabel_763.place(x=20,y=50,width=374,height=30)

        GButton_644=tk.Button(self.parent)
        GButton_644["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_644["font"] = ft
        GButton_644["fg"] = "#000000"
        GButton_644["justify"] = "center"
        GButton_644["text"] = "Update"
        GButton_644.place(x=330,y=290,width=70,height=25)
        GButton_644["command"] = self.GButton_644_command

        GButton_927=tk.Button(self.parent)
        GButton_927["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_927["font"] = ft
        GButton_927["fg"] = "#000000"
        GButton_927["justify"] = "center"
        GButton_927["text"] = "Set Pool Boundaries"
        GButton_927.place(x=1000,y=90,width=97,height=30)
        GButton_927["command"] = self.GButton_927_command

        GLabel_33=tk.Label(self.parent)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_33["font"] = ft
        GLabel_33["fg"] = "#333333"
        GLabel_33["justify"] = "center"
        GLabel_33["text"] = "Up to 5 Contacts"
        GLabel_33.place(x=100,y=250,width=137,height=30)

        GLineEdit_991=tk.Entry(self.parent)
        GLineEdit_991["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_991["font"] = ft
        GLineEdit_991["fg"] = "#333333"
        GLineEdit_991["justify"] = "center"
        GLineEdit_991["text"] = "Name"
        GLineEdit_991.place(x=110,y=290,width=70,height=25)

        GLineEdit_701=tk.Entry(self.parent)
        GLineEdit_701["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_701["font"] = ft
        GLineEdit_701["fg"] = "#333333"
        GLineEdit_701["justify"] = "center"
        GLineEdit_701["text"] = "Name"
        GLineEdit_701.place(x=110,y=330,width=70,height=25)

        GLineEdit_577=tk.Entry(self.parent)
        GLineEdit_577["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_577["font"] = ft
        GLineEdit_577["fg"] = "#333333"
        GLineEdit_577["justify"] = "center"
        GLineEdit_577["text"] = "Phone Number"
        GLineEdit_577.place(x=190,y=330,width=123,height=25)

        GButton_570=tk.Button(self.parent)
        GButton_570["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_570["font"] = ft
        GButton_570["fg"] = "#000000"
        GButton_570["justify"] = "center"
        GButton_570["text"] = "Update"
        GButton_570.place(x=330,y=330,width=70,height=25)
        GButton_570["command"] = self.GButton_570_command

        GLineEdit_701=tk.Entry(self.parent)
        GLineEdit_701["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_701["font"] = ft
        GLineEdit_701["fg"] = "#333333"
        GLineEdit_701["justify"] = "center"
        GLineEdit_701["text"] = "Name"
        GLineEdit_701.place(x=110,y=370,width=70,height=25)

        GLineEdit_577=tk.Entry(self.parent)
        GLineEdit_577["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_577["font"] = ft
        GLineEdit_577["fg"] = "#333333"
        GLineEdit_577["justify"] = "center"
        GLineEdit_577["text"] = "Phone Number"
        GLineEdit_577.place(x=190,y=370,width=123,height=25)

        GButton_570=tk.Button(self.parent)
        GButton_570["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_570["font"] = ft
        GButton_570["fg"] = "#000000"
        GButton_570["justify"] = "center"
        GButton_570["text"] = "Update"
        GButton_570.place(x=330,y=370,width=70,height=25)
        GButton_570["command"] = self.GButton_570_command

        GLineEdit_701=tk.Entry(self.parent)
        GLineEdit_701["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_701["font"] = ft
        GLineEdit_701["fg"] = "#333333"
        GLineEdit_701["justify"] = "center"
        GLineEdit_701["text"] = "Name"
        GLineEdit_701.place(x=110,y=410,width=70,height=25)

        GLineEdit_577=tk.Entry(self.parent)
        GLineEdit_577["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_577["font"] = ft
        GLineEdit_577["fg"] = "#333333"
        GLineEdit_577["justify"] = "center"
        GLineEdit_577["text"] = "Phone Number"
        GLineEdit_577.place(x=190,y=410,width=123,height=25)

        GButton_570=tk.Button(self.parent)
        GButton_570["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_570["font"] = ft
        GButton_570["fg"] = "#000000"
        GButton_570["justify"] = "center"
        GButton_570["text"] = "Update"
        GButton_570.place(x=330,y=410,width=70,height=25)
        GButton_570["command"] = self.GButton_570_command

        GLineEdit_701=tk.Entry(self.parent)
        GLineEdit_701["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_701["font"] = ft
        GLineEdit_701["fg"] = "#333333"
        GLineEdit_701["justify"] = "center"
        GLineEdit_701["text"] = "Name"
        GLineEdit_701.place(x=110,y=450,width=70,height=25)

        GLineEdit_577=tk.Entry(self.parent)
        GLineEdit_577["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_577["font"] = ft
        GLineEdit_577["fg"] = "#333333"
        GLineEdit_577["justify"] = "center"
        GLineEdit_577["text"] = "Phone Number"
        GLineEdit_577.place(x=190,y=450,width=123,height=25)

        GButton_570=tk.Button(self.parent)
        GButton_570["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_570["font"] = ft
        GButton_570["fg"] = "#000000"
        GButton_570["justify"] = "center"
        GButton_570["text"] = "Update"
        GButton_570.place(x=330,y=450,width=70,height=25)
        GButton_570["command"] = self.GButton_570_command



    def GButton_644_command(self):
        print("command")


    def GButton_927_command(self):
        print("command")


    def GButton_570_command(self):
        print("command")



