@echo off
echo Starting Frontend Development Server...
echo.

cd frontend

echo Installing dependencies...
call npm install

if %ERRORLEVEL% NEQ 0 (
    echo Error installing dependencies!
    pause
    exit /b 1
)

echo.
echo Starting development server...
echo Frontend will be available at: http://localhost:3000
echo.
call npm run dev

pause
