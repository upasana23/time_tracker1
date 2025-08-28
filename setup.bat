@echo off
echo Setting up Smart Timetable & Attendance Management System...
echo.

echo [1/5] Installing Frontend Dependencies...
cd frontend
call npm install
if %errorlevel% neq 0 (
    echo Error installing frontend dependencies
    pause
    exit /b 1
)
cd ..

echo [2/5] Installing Backend Dependencies...
cd backend
call npm install
if %errorlevel% neq 0 (
    echo Error installing backend dependencies
    pause
    exit /b 1
)
cd ..

echo [3/5] Installing ML Service Dependencies...
cd ml-service
call pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error installing ML service dependencies
    pause
    exit /b 1
)
cd ..

echo [4/5] Creating necessary directories...
if not exist "ml-service\data" mkdir "ml-service\data"
if not exist "ml-service\outputs" mkdir "ml-service\outputs"
if not exist "backend\data" mkdir "backend\data"

echo [5/5] Setting up environment...
if not exist ".env" (
    copy "env.example" ".env"
    echo Environment file created. Please edit .env with your configuration.
)

echo.
echo Setup completed successfully!
echo.
echo Next steps:
echo 1. Edit .env file with your configuration
echo 2. Add your data files to ml-service/data/
echo 3. Run start.bat to start all services
echo.
pause
