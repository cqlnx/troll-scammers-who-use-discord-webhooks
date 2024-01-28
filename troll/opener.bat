@echo off
setlocal enabledelayedexpansion

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: Python is not installed. 
    echo Please download python from: https://www.python.org/downloads/
    pause
    exit /b 1
)

where pip >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: pip is not installed. 
    echo Please do as shown here to get pip on ur computer: https://www.geeksforgeeks.org/how-to-install-pip-on-windows/
    pause
    exit /b 1
)

set "packages=pystyle"
pip install %packages%

cls
color 0A
for %%i in (%packages%) do (
    echo %%i
)
echo.

echo Opening python script...
python cheezball_scammer_trolling_machine.py
pause
