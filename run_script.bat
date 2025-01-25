@echo off
REM Batch file to run the system microphone volume detection script

REM Disable pip version upgrade notices
set PIP_DISABLE_PIP_VERSION_CHECK=1

REM Check if Python is installed
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python from https://www.python.org/.
    pause
    exit /b
)

REM Check if pip is installed
where pip >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed. Please ensure pip is installed with Python.
    pause
    exit /b
)

REM Check if a virtual environment already exists
if exist "venv\Scripts\activate" (
    echo Virtual environment already exists. Using it...
) else (
    echo Creating virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo Failed to create virtual environment.
        pause
        exit /b
    )
)

REM Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    pause
    exit /b
)

REM Install dependencies if not already installed
echo Checking and installing required Python packages...
pip install -q -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies. Please check your internet connection.
    pause
    exit /b
)

REM Run the Python script
echo Starting system microphone volume detection...
python microphone_system_volume_detection.py
if %errorlevel% neq 0 (
    echo An error occurred while running the script.
    pause
    exit /b
)

pause