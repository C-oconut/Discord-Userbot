@echo off
chcp 65001
echo.
pushd %~dp0

:loopstart

%SYSTEMROOT%\py.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO attempt
%SYSTEMROOT%\py.exe -3.5 SanjayBot/Bot.py
timeout 3
GOTO loopstart

:attempt
py.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO lastattempt
py.exe -3.5 SanjayBot/Bot.py
timeout 3
GOTO loopstart

:lastattempt
python.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO message
python.exe SanjayBot/Bot.py
timeout 3
GOTO loopstart

:message
echo Couldn't find a valid Python 3.5 installation. Python needs to be installed and available in the PATH environment 
echo variable. 
echo Restart This.
PAUSE

:end
