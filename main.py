from tkinter import *

import json
import os
from turtle import right

class Config:
    def __init__(self):
        self.config_file = "config.json"
        self.config = self.load_config()
        
        self.colorMode = self.config.get("colorMode",{}).get("current", "dark")
        self.backgroundColor = self.config.get("colors",{}).get("background", "black")
        self.foregroundColor = self.config.get("colors",{}).get("foreground", "white")

    def load_config(self):
        try:
            with open(self.config_file) as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

class State :
    def __init__(self) :
        self.state_file = "state.json"
        self.state = self.load_state()
        # Set variables with keys from self.state
        for key in self.state.keys():
            setattr(self, key, self.state.get(key))
    def load_state(self) :
        try:
            with open(self.state_file) as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

CONFIG = Config()
STATE = State()

master = Tk()
# Set window height and width to maximum possible
master.geometry("%dx%d+0+0" % (640, 480))
# Set window title
master.title("Tkinter GUI")
# Set Window to full screen
master.attributes("-fullscreen", False)
# Set window background color
master.configure(background=CONFIG.backgroundColor)
# Set window to exit on close
master.protocol("WM_DELETE_WINDOW", lambda: quit())

# Add Menu Bar
menu = Menu(master)
master.config(menu=menu)
# Add File Menu
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=lambda: print("New"))
filemenu.add_command(label="Open...", command=lambda: print("Open..."))
filemenu.add_separator()
filemenu.add_command(label="Exit", command=lambda: quit())
# Add Edit Menu
editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo", command=lambda: print("Undo"))
editmenu.add_separator()
editmenu.add_command(label="Cut", command=lambda: print("Cut"))
editmenu.add_command(label="Copy", command=lambda: print("Copy"))
editmenu.add_command(label="Paste", command=lambda: print("Paste"))
editmenu.add_separator()

# Add Minimize button in Menu bar
minimize = Menu(menu)
menu.add_cascade(label="Minimize", menu=minimize)
minimize.add_command(label="Minimize", command=lambda: master.iconify())
# Add Toggle Maximize button in Menu bar
maximize = Menu(menu)
menu.add_cascade(label="Maximize", menu=maximize)
maximize.add_command(label="Maximize", command=lambda: master.state('zoomed'))
# Add Toggle Fullscreen button in Menu bar
fullscreen = Menu(menu)
menu.add_cascade(label="Fullscreen", menu=fullscreen)
fullscreen.add_command(label="Fullscreen", command=lambda: master.attributes("-fullscreen",not master.attributes("-fullscreen")))

# Add 2 Panes
left = PanedWindow(master, orient=VERTICAL)
left.pack(side=LEFT, fill=BOTH, expand=1)
master.update_idletasks()
# Set left pane width to 20% of master window
left.config(width=int(master.winfo_width()*0.2))
# Set left pane background color
left.config(background=CONFIG.backgroundColor)
# Add left pane to master

def file_handler(event):
    print(f'[+] {event}')
    file_name = event.widget.cget("text")
    file = open(file_name, 'r')
    data = file.read()
    for child in right.winfo_children():
        child.destroy()
    # Display data in right pane
    text = Text(right, width=100, height=20)
    text.insert(END, data)
    text.pack()
    right.grid_columnconfigure(0, weight=1)
    master.update_idletasks()

for file in os.listdir(STATE.currentDirectory):
    # Add Label with max height 10px
    label = Label(left, text=file, height=1)
    label.pack(fill=BOTH, expand=1)
    # Add onclick event
    label.bind("<Button-1>",lambda e : file_handler(e))

right = PanedWindow(master, orient=VERTICAL)
right.pack(side=RIGHT, fill=BOTH, expand=1)
master.update_idletasks()
# Set right pane width to 80%
right.config(width=int(master.winfo_width()*0.8))
# Set right pane background color
right.config(background=CONFIG.foregroundColor)

# def contextChange(event) :
#     lWidth = left.winfo_width()
#     rWidth = right.winfo_width()
#     percent = (lWidth/master.winfo_width())*100
#     print(f'[+] Left Pane Width: {lWidth}')
#     print(f'[+] Right Pane Width: {rWidth}')
#     print(f'[+] Percent: {percent}')


# Call function when zoom change
# master.bind("<Configure>", lambda e: contextChange(e))

mainloop()