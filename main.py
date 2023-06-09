import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='white')

        
        # Set up the main window
        self.title("Safe and Smart")
        self.geometry("800x1000")
        
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
        
    def load_tab1(self):
        # Load the content for Tab 1 from another file
        from Pool_Stream import PoolStream
        tab1_content = PoolStream(self.tab1)
        
    def load_tab2(self):
        # Load the content for Tab 2 from another file
        from User_Settings import UserSettings
        tab2_content = UserSettings(self.tab2)

if __name__ == '__main__':
    app = App()
    app.mainloop()

    

class Tab1Content:
    def __init__(self, parent):
        self.parent = parent
        self.label = tk.Label(self.parent, text="This is the content for Tab 1")
        self.label.pack(padx=20, pady=20)

