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
echo Updating "SanjayBot" Folder...
git stash
git pull

echo.
echo Updating "SanjayBot" Files...
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
echo Couldn't find a valid Python 3.5 installation. Python needs to be installed to the latest version.
echo https://github.com/Sanjay-B/Sanjay-DiscordBot
PAUSE
GOTO end

:gitmessage
echo Git is not installed. Please install it and try again. 
echo https://github.com/Sanjay-B/Sanjay-DiscordBot
PAUSE

:end
