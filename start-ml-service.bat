@echo off
echo Starting ML Service...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Navigate to ml-service directory
cd ml-service

REM Check if requirements.txt exists
if not exist requirements.txt (
    echo Error: requirements.txt not found in ml-service directory
    pause
    exit /b 1
)

REM Install dependencies if needed
echo Installing dependencies...
pip install -r requirements.txt

REM Check if Flask is installed
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo Installing Flask...
    pip install flask flask-cors pandas numpy
)

REM Start the ML service
echo.
echo Starting ML Service on http://localhost:5001
echo Press Ctrl+C to stop the service
echo.
python api.py

pause
