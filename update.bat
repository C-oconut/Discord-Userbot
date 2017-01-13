@echo off
chcp 65001
echo.
pushd %~dp0

net session >nul 2>&1
if NOT %errorLevel% == 0 (
    echo This script NEEDS to be run as administrator.
    echo Right click on it ^-^> Run as administrator.
    echo.
    PAUSE
    GOTO end  
)

git.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO gitmessage
echo Updating Sanjay-DiscordBot...
git stash
git pull

echo.
echo Updating Requirements...
%SYSTEMROOT%\py.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO attempt
%SYSTEMROOT%\py.exe -3.5 -m pip install --upgrade -r requirements.txt
PAUSE
GOTO end

:attempt
py.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO lastattempt
py.exe -3.5 -m pip install --upgrade -r requirements.txt
PAUSE
GOTO end

:lastattempt
python.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO pythonmessage
python.exe -m pip install --upgrade -r requirements.txt
PAUSE
GOTO end

:pythonmessage
echo Python 3.5 or higher was not found on this machine.
echo Install the lastest version of Python here: https://www.python.org/downloads/
echo Link to original repo is here: https://github.com/Sanjay-B/Sanjay-DiscordBot
PAUSE
GOTO end

:gitmessage
echo Git was not found on this machine. 
echo Install the lastest veerson of Git here: https://git-scm.com/downloads
echo Link to original repo is here: https://github.com/Sanjay-B/Sanjay-DiscordBot
PAUSE

:end