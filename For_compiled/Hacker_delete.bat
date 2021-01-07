rem Удаление лишних папок

@ECHO OFF
RD /S /F build
DEL /F Hacker.spec
RD /S /F __pycache__