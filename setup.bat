@echo off
REM Setup script for Python Snake Game (Windows)
REM
REM Usage: setup.bat
REM
REM This script will:
REM   1. Check Python installation (requires Python 3.8.1+)
REM   2. Create a virtual environment
REM   3. Install dependencies
REM   4. Verify installation

setlocal enabledelayedexpansion

echo ===================================
echo Python Snake Game Setup
echo ===================================
echo.

REM Check if Python is installed
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed.
    echo.
    echo Please install Python 3.8.1 or higher and try again.
    echo Download from: https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

REM Get and display Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo √ Python found: %PYTHON_VERSION%

REM Check Python version is 3.8 or higher
for /f "tokens=1,2 delims=." %%a in ("%PYTHON_VERSION%") do (
    set MAJOR=%%a
    set MINOR=%%b
)

if %MAJOR% LSS 3 (
    echo Error: Python 3.8.1 or higher is required.
    echo Current version: %PYTHON_VERSION%
    pause
    exit /b 1
)

if %MAJOR% EQU 3 if %MINOR% LSS 8 (
    echo Error: Python 3.8.1 or higher is required.
    echo Current version: %PYTHON_VERSION%
    pause
    exit /b 1
)

echo.

REM Check if virtual environment already exists
if exist "venv\" (
    echo Virtual environment already exists. Skipping creation.
    echo To recreate, delete the 'venv' directory first.
    echo.
) else (
    REM Create virtual environment
    echo Creating virtual environment...
    python -m venv venv
    
    if errorlevel 1 (
        echo Error: Failed to create virtual environment.
        echo.
        echo This might happen if:
        echo   - Python installation is incomplete
        echo   - Antivirus is blocking the operation
        echo   - You don't have write permissions
        echo.
        pause
        exit /b 1
    )
    
    echo √ Virtual environment created successfully!
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
    echo √ Virtual environment activated
) else (
    echo Error: Could not find activation script.
    pause
    exit /b 1
)
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip --quiet
echo √ pip upgraded
echo.

REM Install requirements
echo Installing requirements...
if exist "requirements.txt" (
    pip install -r requirements.txt
    
    if errorlevel 1 (
        echo Error: Failed to install requirements.
        echo.
        echo This might be due to:
        echo   - Network connectivity issues
        echo   - Missing system dependencies
        echo   - Antivirus blocking installation
        echo.
        pause
        exit /b 1
    )
    
    echo √ Requirements installed successfully!
) else (
    echo Warning: requirements.txt not found. Skipping dependencies.
)

echo.
echo ===================================
echo √ Setup completed successfully!
echo ===================================
echo.
echo Next steps:
echo.
echo 1. Activate the virtual environment:
echo    venv\Scripts\activate.bat
echo.
echo 2. Run the game:
echo    python src\snake_game.py
echo    # Or the modular version:
echo    python src\snake_game_modular.py
echo.
echo 3. Run tests (optional):
echo    python tests\test_game.py
echo.
echo Game controls:
echo    Arrow Keys   Move
echo    P            Pause/Resume
echo    R            Restart
echo    Q            Quit
echo.
echo Enjoy playing Snake! 🐍🎮
echo.
pause
