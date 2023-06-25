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

        #1
        self.input_nameC1 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_nameC1.place(x=200, y=290, height=30)

        self.input_phoneC1 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_phoneC1.place(x=300,  y=290,height=30)


        #2
        self.input_nameC2 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_nameC2.place(x=200, y=330, height=30)

        self.input_phoneC2 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_phoneC2.place(x=300,  y=330,height=30)

        #3

        self.input_nameC3 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_nameC3.place(x=200, y=370, height=30)

        self.input_phoneC3 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_phoneC3.place(x=300,  y=370,height=30)

        #4
        self.input_nameC4 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_nameC4.place(x=200, y=410, height=30)

        self.input_phoneC4 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_phoneC4.place(x=300,  y=410,height=30)

        #5
        self.input_nameC5 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_nameC5.place(x=200, y=450, height=30)

        self.input_phoneC5 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_phoneC5.place(x=300,  y=450,height=30)

        # Label for settings page
        GLabel_763 = tk.Label(self.parent, text="Settings page", font=H1_label_font,fg=text_color, bg=background)
        GLabel_763.place(x=100, y=50)


        #system number 
        label_systemNumber = tk.Label(self.parent, text="#1", font=Text_label_font, fg="black", bg="white", justify="center", width=7)
        label_systemNumber.place(x=200, y=120, width=100)

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
        from dataBaseAPI import User
                # Load the updated user1 from the database
        self.updated_user1 = User.load('User1')

        # Access and print the updated name
        self.label_c1 = tk.Label(self.parent, text="Contact 1", font=Text_label_font, fg=text_color, bg=background, justify="left")
        self.label_c1.place(x=100, y=290, width=100, height=25)

        self.input_nameC1 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_nameC1.place(x=200, y=290, height=30)
        self.input_nameC1.insert(0, self.updated_user1.get_name())  # Placeholder text for name

        # phone number 1
        self.input_phoneC1 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_phoneC1.place(x=300, y=290, height=30)
        self.input_phoneC1.insert(0, self.updated_user1.get_phone())  # Placeholder text for phone number


        
        # Button to update 1
        btn_updateC1 = tk.Button(self.parent, text="Update", font=Text_label_font,borderwidth="0px", command=self.btn_updateC1_command)
        btn_updateC1.place(x=400,  y=290,height=30)

        
        # contact 2
        
                # Load the updated user1 from the database
        self.updated_user2 = User.load('User2')
        self.label_c2 = tk.Label(self.parent, text="Contact 2", font=Text_label_font,fg=text_color, bg=background, justify="left")
        self.label_c2.place(x=100,  y=330, width=100, height=25)

        self.input_nameC2 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_nameC2.place(x=200,  y=330,height=30)
        self.input_nameC2.insert(0, self.updated_user2.get_name())  # Placeholder text for name

        # phone number 2
        self.input_phoneC2 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_phoneC2.place(x=300,  y=330,height=30)
        self.input_phoneC2.insert(0, self.updated_user2.get_phone())  # Placeholder text for phone number

        
        # Button to update 2
        btn_updateC2 = tk.Button(self.parent, text="Update",borderwidth="0px", font=Text_label_font, command=self.btn_updateC2_command)
        btn_updateC2.place(x=400,  y=330,height=30)


        # contact 3
        
                # Load the updated user1 from the database
        self.updated_user3 = User.load('User3')
        self.label_c3 = tk.Label(self.parent, text="Contact 3", font=Text_label_font,fg=text_color, bg=background, justify="left")
        self.label_c3.place(x=100,  y=370, width=100, height=25)
        self.input_nameC3 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_nameC3.place(x=200,  y=370,height=30)
        self.input_nameC3.insert(0, self.updated_user3.get_name())  # Placeholder text for name


        # phone number 3
        self.input_phoneC3 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_phoneC3.place(x=300,  y=370,height=30)
        self.input_phoneC3.insert(0, self.updated_user3.get_phone())  # Placeholder text for phone number
        
        # Button to update 3
        btn_updateC3 = tk.Button(self.parent, text="Update",borderwidth="0px", font=Text_label_font, command=self.btn_updateC3_command)
        btn_updateC3.place(x=400,  y=370,height=30)
        

        # contact 4
        self.updated_user4 = User.load('User4')
        self.label_c4 = tk.Label(self.parent, text="Contact 4", font=Text_label_font,fg=text_color, bg=background, justify="left")
        self.label_c4.place(x=100,  y=410, width=100, height=25)
        self.input_nameC4 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_nameC4.place(x=200,  y=410,height=30)
        self.input_nameC4.insert(0, self.updated_user4.get_name())  # Placeholder text for name


        # phone number 4
        self.input_phoneC4 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_phoneC4.place(x=300,  y=410,height=30)
        self.input_phoneC4.insert(0, self.updated_user4.get_phone())  # Placeholder text for phone number
        
        # Button to update 4
        btn_updateC4 = tk.Button(self.parent, text="Update",borderwidth="0px", font=Text_label_font, command=self.btn_updateC4_command)
        btn_updateC4.place(x=400,  y=410,height=30)


        # contact 5
        self.updated_user5 = User.load('User5')
        self.label_c5 = tk.Label(self.parent, text="Contact 5", font=Text_label_font,fg=text_color, bg=background, justify="left")
        self.label_c5.place(x=100,  y=450, width=100, height=25)
        self.input_nameC5 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_nameC5.place(x=200,  y=450,height=30)
        self.input_nameC5.insert(0, self.updated_user5.get_name())  # Placeholder text for name

        # phone number 5
        self.input_phoneC5 = tk.Entry(self.parent, borderwidth="0px", width=length_input)
        self.input_phoneC5.place(x=300,  y=450,height=30)
        self.input_phoneC5.insert(0, self.updated_user5.get_phone())  # Placeholder text for phone number
        
        # Button to update 5
        btn_updateC5 = tk.Button(self.parent, text="Update",borderwidth="0px", font=Text_label_font,bg=background, command=self.btn_updateC5_command)
        btn_updateC5.place(x=400,  y=450,height=30)


    def btn_poolBound_command(self):
        print("command")


    def btn_updateC1_command(self):

        
        global input_nameC1
        x = self.input_nameC1.get()
        y = self.input_phoneC1.get()
        self.updated_user1.update_field('name', x)
        self.updated_user1.update_field('phone', y)
        self.updated_user1.save()

        # print("command")
        # print(f"Value of x: '{x}'")
        # print(f"Value of y: '{y}'")
    
    
    def btn_updateC2_command(self):
        global input_nameC2
        x = self.input_nameC2.get()
        y = self.input_phoneC2.get()
        self.updated_user2.update_field('name', x)
        self.updated_user2.update_field('phone', y)
        self.updated_user2.save()
        # print("command")
        # print(f"Value of x: '{x}'")
        # print(f"Value of y: '{y}'")
        
    def btn_updateC3_command(self):
        global input_nameC3
        x = self.input_nameC3.get()
        y = self.input_phoneC3.get()
        self.updated_user3.update_field('name', x)
        self.updated_user3.update_field('phone', y)
        self.updated_user3.save()
        # print("command")
        # print(f"Value of x: '{x}'")
        # print(f"Value of y: '{y}'")
    
    def btn_updateC4_command(self):
        global input_nameC4
        x = self.input_nameC4.get()
        y = self.input_phoneC4.get()
        self.updated_user4.update_field('name', x)
        self.updated_user4.update_field('phone', y)
        self.updated_user4.save()
        # print("command")
        # print(f"Value of x: '{x}'")
        # print(f"Value of y: '{y}'")

    def btn_updateC5_command(self):
        global input_nameC5
        x = self.input_nameC5.get()
        y = self.input_phoneC5.get()
        self.updated_user5.update_field('name', x)
        self.updated_user5.update_field('phone', y)
        self.updated_user5.save()
        # print("command")
        # print(f"Value of x: '{x}'")
        # print(f"Value of y: '{y}'")



