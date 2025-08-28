# Smart Timetable & Attendance Management System

A comprehensive web application that integrates machine learning models for attendance prediction, timetable optimization, and an intelligent chatbot for data querying.

## 🏗️ Project Structure

```
project/
├── frontend/                 # Next.js React frontend
├── backend/                  # Node.js Express API
├── ml-service/              # Python FastAPI ML service
├── chatbot/                 # RAG-enabled chatbot
├── docker-compose.yml       # Complete system orchestration
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.8+
- Docker & Docker Compose (optional)

### Option 1: Docker (Recommended)
```bash
# Clone and start all services
git clone <repository>
cd project
docker-compose up -d

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:4000
# ML Service: http://localhost:8000
# Chatbot: http://localhost:3000/chatbot
```

### Option 2: Manual Setup
```bash
# 1. Start ML Service
cd ml-service
pip install -r requirements.txt
uvicorn api:app --host 0.0.0.0 --port 8000

# 2. Start Backend
cd backend
npm install
npm run dev

# 3. Start Frontend
cd frontend
npm install
npm run dev
```

## 🧠 Machine Learning Features

- **Attendance Prediction**: XGBoost-based models for predicting student attendance
- **Risk Assessment**: Deep learning models for identifying at-risk students
- **Timetable Optimization**: AI-powered scheduling optimization
- **Energy Efficiency**: Smart room allocation and energy usage analysis

## 🤖 Chatbot Features

- **RAG Integration**: Retrieval-Augmented Generation for accurate responses
- **Data Querying**: Natural language queries for attendance and timetable data
- **Real-time Analytics**: Live dashboard integration
- **Multi-modal Support**: Text and voice input capabilities

## 📊 Dashboard Features

- **Real-time Analytics**: Live attendance tracking and visualization
- **Predictive Insights**: ML-powered attendance predictions
- **Interactive Charts**: Dynamic data visualization
- **User Management**: Role-based access control
- **Export Capabilities**: Data export in multiple formats

## 🔧 API Endpoints

### Backend API (Port 4000)
- `POST /api/auth/login` - User authentication
- `POST /api/attendance` - Record attendance
- `GET /api/attendance/:id` - Get attendance data
- `POST /api/contact` - Contact form submission

### ML Service API (Port 8000)
- `GET /api/departments` - Get available departments
- `GET /api/attendance/{dept}/{section}` - Get ML predictions
- `POST /api/train` - Train new models
- `GET /api/analytics` - Get analytics data

### Chatbot API
- `POST /api/chatbot/query` - Process natural language queries
- `GET /api/chatbot/context` - Get available data context

## 🛠️ Development

### Frontend Development
```bash
cd frontend
npm run dev
```

### Backend Development
```bash
cd backend
npm run dev
```

### ML Service Development
```bash
cd ml-service
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

## 📁 Data Structure

The system uses the following data files:
- `students.csv` - Student information
- `teachers.csv` - Teacher information
- `subjects.csv` - Course information
- `rooms.csv` - Room availability
- `timetable.csv` - Current timetable
- `attendance_auto.csv` - Historical attendance data

## 🔒 Security Features

- JWT-based authentication
- Rate limiting
- CORS protection
- Input validation
- SQL injection prevention

## 📈 Monitoring & Analytics

- Real-time attendance tracking
- Predictive analytics
- Risk assessment
- Energy efficiency reports
- Performance metrics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.
