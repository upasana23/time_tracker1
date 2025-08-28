#!/bin/bash

echo "Starting Smart Timetable & Attendance Management System..."
echo

echo "[1/4] Starting ML Service..."
cd ml-service
python -m uvicorn api:app --host 0.0.0.0 --port 8000 --reload &
ML_PID=$!
cd ..

echo "[2/4] Starting Backend API..."
cd backend
npm run dev &
BACKEND_PID=$!
cd ..

echo "[3/4] Starting Frontend..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo "[4/4] Starting Chatbot..."
cd chatbot
python -m http.server 3001 &
CHATBOT_PID=$!
cd ..

echo
echo "All services are starting..."
echo
echo "Services will be available at:"
echo "- Frontend: http://localhost:3000"
echo "- Backend API: http://localhost:4000"
echo "- ML Service: http://localhost:8000"
echo "- Chatbot: http://localhost:3001"
echo
echo "Press Ctrl+C to stop all services..."

# Function to cleanup on exit
cleanup() {
    echo
    echo "Stopping all services..."
    kill $ML_PID $BACKEND_PID $FRONTEND_PID $CHATBOT_PID 2>/dev/null
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

# Wait for all background processes
wait
