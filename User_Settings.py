import tkinter as tk
import tkinter.font as tkFont

class UserSettings:
    def __init__(self, parent):
        self.parent = parent
        self.parent.configure(bg='white')
        length_input=10
        Text_label_font= ("Times", 20)
        H1_label_font=("Times", 40)
        H2_label_font=("Times", 30)
        text_color= "#000000"
        background= "#FFFFFF"
        
        # Label for settings page
        GLabel_763 = tk.Label(self.parent, text="Settings page", font=H1_label_font,fg=text_color, bg=background)
        GLabel_763.place(x=100, y=50)


        #system number 
        input_systemNumber = tk.Entry(self.parent, bd=1, font=Text_label_font,fg=text_color, bg=text_color, justify="center", width=7,state="readonly")
        input_systemNumber.insert(0, "Entry")
        input_systemNumber.place(x=200, y=120, width=100)

        label_systemNumber = tk.Label(self.parent, text="System ID", font=Text_label_font,fg=text_color, bg=background, justify="left")
        label_systemNumber.place(x=100,  y=120, width=100, height=25)


        # Label List of contacts
        label_listofContacts = tk.Label(self.parent, text="List of contacts", font=H2_label_font,fg=text_color, bg=background, justify="left")
        label_listofContacts.place(x=100,  y=220, height=30)

        # Label for number of contacts
        label_numofContacts = tk.Label(self.parent, text="Up to 5 Contacts", font=Text_label_font,fg=text_color, bg=background,justify="left")
        label_numofContacts.place(x=100, y=250)
        
        # Button to set pool boundaries
        btn_poolBound = tk.Button(self.parent, text="Set Pool Boundaries", font=Text_label_font,borderwidth="0px", command=self.btn_poolBound_command)
        btn_poolBound.place(x=1000, y=90,height=30)


        # contact 1
        label_c1 = tk.Label(self.parent, text="Contact 1", font=Text_label_font,fg=text_color, bg=background, justify="left")
        label_c1.place(x=100,  y=290, width=100, height=25)


        input_nameC1 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        input_nameC1.place(x=200, y=290,height=30)


        # phone number 1
        input_phoneC1 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        input_phoneC1.place(x=300,  y=290,height=30)

        
        # Button to update 1
        btn_updateC1 = tk.Button(self.parent, text="Update", font=Text_label_font,borderwidth="0px", command=self.btn_updateC1_command)
        btn_updateC1.place(x=400,  y=290,height=30)

        
        # contact 2
        label_c2 = tk.Label(self.parent, text="Contact 2", font=Text_label_font,fg=text_color, bg=background, justify="left")
        label_c2.place(x=100,  y=330, width=100, height=25)

        input_nameC2 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        input_nameC2.place(x=200,  y=330,height=30)


        # phone number 2
        input_phoneC2 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        input_phoneC2.place(x=300,  y=330,height=30)

        
        # Button to update 2
        btn_updateC2 = tk.Button(self.parent, text="Update",borderwidth="0px", font=Text_label_font, command=self.btn_updateC2_command)
        btn_updateC2.place(x=400,  y=330,height=30)


        # contact 3
        label_c3 = tk.Label(self.parent, text="Contact 3", font=Text_label_font,fg=text_color, bg=background, justify="left")
        label_c3.place(x=100,  y=370, width=100, height=25)
        input_nameC3 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        input_nameC3.place(x=200,  y=370,height=30)


        # phone number 3
        input_phoneC3 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        input_phoneC3.place(x=300,  y=370,height=30)

        
        # Button to update 3
        btn_updateC3 = tk.Button(self.parent, text="Update",borderwidth="0px", font=Text_label_font, command=self.btn_updateC3_command)
        btn_updateC3.place(x=400,  y=370,height=30)
        

        # contact 4
        label_c4 = tk.Label(self.parent, text="Contact 4", font=Text_label_font,fg=text_color, bg=background, justify="left")
        label_c4.place(x=100,  y=410, width=100, height=25)
        input_nameC4 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        input_nameC4.place(x=200,  y=410,height=30)


        # phone number 4
        input_phoneC4 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        input_phoneC4.place(x=300,  y=410,height=30)

        
        # Button to update 4
        btn_updateC4 = tk.Button(self.parent, text="Update",borderwidth="0px", font=Text_label_font, command=self.btn_updateC4_command)
        btn_updateC4.place(x=400,  y=410,height=30)


        # contact 5
        label_c5 = tk.Label(self.parent, text="Contact 5", font=Text_label_font,fg=text_color, bg=background, justify="left")
        label_c5.place(x=100,  y=450, width=100, height=25)
        input_nameC5 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        input_nameC5.place(x=200,  y=450,height=30)


        # phone number 5
        input_phoneC5 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        input_phoneC5.place(x=300,  y=450,height=30)

        
        # Button to update 5
        btn_updateC5 = tk.Button(self.parent, text="Update",borderwidth="0px", font=Text_label_font,bg=background, command=self.btn_updateC5_command)
        btn_updateC5.place(x=400,  y=450,height=30)


    def btn_poolBound_command(self):
        print("command")


    def btn_updateC1_command(self):
        print("command")
    
    
    def btn_updateC2_command(self):
        print("command")
        
    def btn_updateC3_command(self):
        print("command")
    
    def btn_updateC4_command(self):
        print("command")

    def btn_updateC5_command(self):
        print("command")



