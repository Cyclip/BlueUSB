@echo off
title BlueUSB
color b
mode 55,33

echo The path selected can be directly to a USB Flash drive.
echo It will active right when the drive is plugged in.
echo Nice mode will be a bit less deadlier. It wont suspend
echo all processes unlike the normal mode, and it will also
echo close the fake BSoD after X amount of seconds.
echo Set it to 0 seconds if you don't want Nice mode :(
echo.
echo The return code is a fake return code only for Windows
echo 10 Blue screens. You can change it to whatever suits.
echo.
echo If you want a different version blue screen, you can
echo force a version type by selecting one. Selecting the
echo 'off' option will blue screen to whatever the version
echo is -- for example, a Win7 BSoD for a Win7 machine.
echo 
echo Suspending a process does not end it, but kind of
echo pauses it completely. Yes this is quite bad so you
echo can choose what processes you don't want to suspend.
echo For example, python.exe or pythonw.exe
echo.
echo By using the program you agree to the license and
echo take all responsibility and liability for anything you
echo make or cause with this program. The creator of the
echo program is not liable at all for anything. You'll also
echo have to agree to this because I'm making this for fun.
echo You're using it for fun too, so it only makes sense?
echo.
echo The EXE version of the BlueUSB Generator takes longer
echo to load but I guess that isn't too bad. You should
echo download the EXE if you don't have the modules
echo required, although you'll need to install some modules
echo to build the real file.

python BlueUSB.py > nul

echo nsnsns
