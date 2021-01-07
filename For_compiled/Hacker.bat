rem Сборка .exe приложений из Python файлов

@ECHO OFF
cls
pyinstaller --onedir --onefile --name=Hacker Hacker.py
Hacker_delete.bat
rem set/p "usb=>"