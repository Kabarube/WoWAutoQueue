import tkinter as tk
from pywinauto.application import Application
import time

#
# Function for initialising a windows
#
dlgbox = tk.Tk(screenName="WoW Auto Queue")
WidgetFrame = tk.Frame(dlgbox, bd=2)

Label1 = tk.Label(dlgbox, text="Path: ")
Label2 = tk.Label(dlgbox, text="Delay: ")
Label1.pack(side="left")
Label2.pack(side="bottom")
pathfield = tk.Entry(dlgbox, bd=3)
pathfield.pack(side="left")


dlgbox.mainloop()


#
# Function for starting the wow launcher
#
def startLauncher(launcher_path, delay=5):
    time.sleep(delay)
    wow_launcher = Application(backend='uia')
    wow_launcher.start(launcher_path)

    # Locate window with title similar to "World of warcraft"
    # Clicking on button similar to "Play"
    wow_launcher['World of Warcraft'].Play.click()

startLauncher(launcher_path='C:\World of Warcraft\Launcher.exe', delay=0)
