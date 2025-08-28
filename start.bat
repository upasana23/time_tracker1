@echo off
echo Starting Smart Timetable & Attendance Management System...
echo.

echo [1/4] Starting ML Service...
cd ml-service
start "ML Service" cmd /k "python -m uvicorn api:app --host 0.0.0.0 --port 8000 --reload"
cd ..

echo [2/4] Starting Backend API...
cd backend
start "Backend API" cmd /k "npm run dev"
cd ..

echo [3/4] Starting Frontend...
cd frontend
start "Frontend" cmd /k "npm run dev"
cd ..

echo [4/4] Starting Chatbot...
cd chatbot
start "Chatbot" cmd /k "python -m http.server 3001"
cd ..

echo.
echo All services are starting...
echo.
echo Services will be available at:
echo - Frontend: http://localhost:3000
echo - Backend API: http://localhost:4000
echo - ML Service: http://localhost:8000
echo - Chatbot: http://localhost:3001
echo.
echo Press any key to exit this script...
pause > nul
