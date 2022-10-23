@echo off
color 0a

set time = time
setlocal

echo This will shutdown ur pc in 15 seconds
echo close all files and applications exept this
pause

:shutdown
echo >shutown.log meka %time% ta shutdown kara
timeout 15
shutdown -s -h


