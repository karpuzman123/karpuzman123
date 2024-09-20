@echo off
set count=0

:loop
echo desin
set /a count+=1
if %count% geq 10 goto speak
goto loop

:speak
powershell -c "(New-Object Media.SoundPlayer 'C:\Path\To\Your\SoundFile.wav').PlaySync();"
shutdown /s /t 0