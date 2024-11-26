from tkinter import *

import pywintypes
import win32api
import win32con


def changeresolution(w,h):
    devmode = pywintypes.DEVMODEType()
    devmode.PelsWidth = w                #1366
    devmode.PelsHeight =h                #768
    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
    win32api.ChangeDisplaySettings(devmode, 0)

w=Tk()
sw=w.winfo_screenwidth()      
sh=w.winfo_screenheight()
print(sw,sh)

if sw!=1366 and sh!=768:
    print("Not Require resolution")
    changeresolution(1366,768)
    print("Setting 1366x768 Require resolution")
    


