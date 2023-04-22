import tkinter as tk
from tkinter import ttk, messagebox

# Create the main window
root = tk.Tk()
root.title("My Application")

# Set the window size and position
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width, height))

# Create a notebook (tabs)
notebook = ttk.Notebook(root)

# Create the three tabs
tab1 = tk.Frame(notebook, bg="white")
tab2 = tk.Frame(notebook, bg="black")
tab3 = tk.Frame(notebook, bg="white")

notebook.add(tab1, text="Pool Stream")
notebook.add(tab2, text="User Settings")
notebook.add(tab3, text="Pool Settings")

# Create a sidebar that is shared between the tabs
sidebar = tk.Frame(root, bg="white", width=200)
sidebar.pack(side="left", fill="y")

# Create the scopes in the sidebar
scope1 = tk.Frame(sidebar, bg="white", highlightbackground="black", highlightthickness=1)
scope2 = tk.Frame(sidebar, bg="white", highlightbackground="black", highlightthickness=1)
scope3 = tk.Frame(sidebar, bg="white", highlightbackground="black", highlightthickness=1)

scope1.pack(side="top", fill="x")
scope2.pack(side="top", fill="x")
scope3.pack(side="top", fill="x")

# Create the "Hey" buttons in each scope
hey_button1 = tk.Button(scope1, text="Hey")
hey_button2 = tk.Button(scope2, text="Hey")
hey_button3 = tk.Button(scope3, text="Hey")

hey_button1.pack(side="left", padx=10)
hey_button2.pack(side="left", padx=10)
hey_button3.pack(side="left", padx=10)

# Define a function to handle the window closing event
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the application
notebook.pack(side="right", expand=True, fill="both")
root.mainloop()
