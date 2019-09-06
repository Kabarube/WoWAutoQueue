import tkinter as tk
import time
import pyautogui as auto
from tkinter import filedialog as fd  # Just a note
from pywinauto.application import Application


#---- Initialise GUI ----#
dlgbox = tk.Tk()
dlgbox.title("WoW Auto Queue")
dlgbox.geometry("500x200")

#---- Frame for delay control ----#
delayFrame = tk.Frame(dlgbox, bg="grey")
delayFrame.place(relx=0.05, rely=0.032, relwidth=0.9, relheight=0.25)

#---- Frame for WoW server list ----#
serverFrame = tk.Frame(dlgbox, bg="grey")
serverFrame.place(relx=0.05, rely=0.3, relwidth=0.6, relheight=0.65)

#---- Frame for countdown and a run button ----#
countdownFrame = tk.Frame(dlgbox, bg="grey")
countdownFrame.place(anchor="nw", relx=0.66, rely=0.3,
                     relwidth=0.29, relheight=0.65)

#---- Serverlist ----#
serverList = tk.Listbox(serverFrame, bg="light grey", bd=0,
                        selectmode="single", font=22)
serverList.place(relwidth=1, relheight=1)

#---- Filling the serverList with information ----#
serverArray = ["Shadowsong", "Draenor", "Burning Blade"]

for n in serverArray:
    serverList.insert(0, str(n))


dlgbox.mainloop()


#
#---- Function for starting the wow launcher ----#
#
def startLauncher(launcher_path, delay=5):
    time.sleep(delay)
    wow_launcher = Application(backend="uia")
    wow_launcher.start(launcher_path)
    time.sleep(2)

    # playButton_location = auto.locateCenterOnScreen(
    #    "G:/Dropbox/Dokumenter/Programming/GitHub/WoWAutoQueue/play.png")
    time.sleep(2)
    #xpos = playButton_location[0]
    #ypos = playButton_location[1]

    auto.moveTo("G:/Dropbox/Dokumenter/Programming/GitHub/WoWAutoQueue/play.png")


startLauncher(
    launcher_path='C:/Program Files (x86)/Battle.net/Battle.net.exe', delay=2)
