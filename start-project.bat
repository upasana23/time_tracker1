@echo off
echo ========================================
echo Starting Smart Timetable & Attendance System
echo ========================================
echo.

echo [1/5] Checking prerequisites...
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

where node >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Node.js is not installed or not in PATH
    pause
    exit /b 1
)

echo [2/5] Installing dependencies...
echo Installing backend dependencies...
cd backend
npm install
if %errorlevel% neq 0 (
    echo ERROR: Failed to install backend dependencies
    pause
    exit /b 1
)

echo Installing frontend dependencies...
cd ..\frontend
npm install
if %errorlevel% neq 0 (
    echo ERROR: Failed to install frontend dependencies
    pause
    exit /b 1
)

echo Installing ML service dependencies...
cd ..\ml-service
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install ML service dependencies
    pause
    exit /b 1
)

echo [3/5] Initializing database...
cd ..\backend
echo Creating database schema...
node -e "
const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');
const path = require('path');

const dbPath = path.join(__dirname, '..', 'data', 'db.sqlite');
const schemaPath = path.join(__dirname, 'src', 'scripts', 'init_db.sql');

if (!fs.existsSync(path.dirname(dbPath))) {
    fs.mkdirSync(path.dirname(dbPath), { recursive: true });
}

const db = new sqlite3.Database(dbPath);
const schema = fs.readFileSync(schemaPath, 'utf8');

db.exec(schema, (err) => {
    if (err) {
        console.error('Database initialization error:', err);
        process.exit(1);
    } else {
        console.log('Database initialized successfully');
        db.close();
        process.exit(0);
    }
});
"

echo [4/5] Starting services...
echo Starting backend service...
start "Backend Service" cmd /k "cd backend && npm run dev"

echo Starting frontend service...
start "Frontend Service" cmd /k "cd frontend && npm run dev"

echo Starting ML service...
start "ML Service" cmd /k "cd ml-service && python api_server.py"

echo [5/5] Waiting for services to start...
timeout /t 10 /nobreak >nul

echo.
echo ========================================
echo Services are starting up...
echo ========================================
echo Backend: http://localhost:4000
echo Frontend: http://localhost:3000
echo ML Service: http://localhost:8000
echo Chatbot: http://localhost:3001
echo.
echo Please wait a few moments for all services to be ready.
echo.
echo Press any key to open the frontend...
pause >nul

start http://localhost:3000

echo.
echo Project started successfully!
echo All services are now running.
echo.
pause
