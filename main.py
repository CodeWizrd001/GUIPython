from tkinter import *
import json

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

CONFIG = Config()

master = Tk()
# Set window height and width to maximum possible
master.geometry("%dx%d+0+0" % (master.winfo_screenwidth(), master.winfo_screenheight()))
# Set window title
master.title("Tkinter GUI")
# Set Window to full screen
master.attributes("-fullscreen", True)
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
# Set left pane background color
left.configure(background=CONFIG.backgroundColor)
right = PanedWindow(master, orient=VERTICAL)
right.pack(side=RIGHT, fill=BOTH, expand=1)
# Set right pane background color
right.configure(background=CONFIG.foregroundColor)

mainloop()