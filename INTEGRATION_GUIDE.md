# Smart Timetable & Attendance Management System - Integration Guide

## 🎯 Project Overview

This is a fully integrated web application that combines:
- **Machine Learning Models** for attendance prediction and risk assessment
- **Next.js Frontend** with modern UI components
- **Node.js Backend API** for user management and data handling
- **RAG-enabled Chatbot** for intelligent data querying
- **Docker Support** for easy deployment

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   ML Service    │
│   (Next.js)     │◄──►│   (Node.js)     │◄──►│   (FastAPI)     │
│   Port: 3000    │    │   Port: 4000    │    │   Port: 8000    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Chatbot       │    │   Database      │    │   ML Models     │
│   (HTML/JS)     │    │   (SQLite)      │    │   (XGBoost/DL)  │
│   Port: 3001    │    │   Local Files   │    │   Output Files  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

1. **Setup Dependencies**
   ```bash
   # Windows
   setup.bat
   
   # Linux/Mac
   chmod +x setup.sh
   ./setup.sh
   ```

2. **Start All Services**
   ```bash
   # Windows
   start.bat
   
   # Linux/Mac
   chmod +x start.sh
   ./start.sh
   ```

3. **Test Integration**
   ```bash
   python test-integration.py
   ```

### Option 2: Docker Deployment

```bash
docker-compose up -d
```

### Option 3: Manual Setup

1. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

2. **Backend Setup**
   ```bash
   cd backend
   npm install
   npm run dev
   ```

3. **ML Service Setup**
   ```bash
   cd ml-service
   pip install -r requirements.txt
   uvicorn api:app --host 0.0.0.0 --port 8000 --reload
   ```

4. **Chatbot Setup**
   ```bash
   cd chatbot
   python -m http.server 3001
   ```

## 🔧 Configuration

### Environment Variables

Copy `env.example` to `.env` and configure:

```bash
# Frontend
NEXT_PUBLIC_API_URL=http://localhost:4000
NEXT_PUBLIC_ML_API_URL=http://localhost:8000
NEXT_PUBLIC_CHATBOT_URL=http://localhost:3001

# Backend
JWT_SECRET=your-secret-key
ML_SERVICE_URL=http://localhost:8000

# ML Service
PYTHONPATH=/app
```

### Data Files

Place your data files in `ml-service/data/`:
- `students.csv` - Student information
- `teachers.csv` - Teacher information
- `subjects.csv` - Course information
- `rooms.csv` - Room availability
- `timetable.csv` - Current timetable
- `attendance_auto.csv` - Historical attendance data

## 🧠 Machine Learning Features

### 1. Attendance Prediction
- **Model**: XGBoost with hyperparameter tuning
- **Features**: Historical attendance, time patterns, student demographics
- **Output**: Risk scores for each student

### 2. Risk Assessment
- **Model**: Deep Learning (Neural Networks)
- **Features**: Attendance patterns, academic performance, demographic data
- **Output**: High-risk student identification

### 3. Timetable Optimization
- **Algorithm**: AI-powered scheduling optimization
- **Features**: Room availability, teacher schedules, student preferences
- **Output**: Optimized timetable with energy efficiency

### 4. Energy Efficiency Analysis
- **Analysis**: Room allocation optimization
- **Features**: Room usage patterns, energy consumption data
- **Output**: Energy efficiency reports and recommendations

## 🤖 Chatbot Integration

### RAG (Retrieval-Augmented Generation)
The chatbot uses RAG technology to provide accurate, data-driven responses:

1. **Knowledge Base**: All CSV data and ML outputs are indexed
2. **Query Processing**: Natural language queries are processed
3. **Data Retrieval**: Relevant data is retrieved based on query context
4. **Response Generation**: Contextual responses are generated using the retrieved data

### Available Queries
- "What is the attendance rate for Computer Science department?"
- "Show me high-risk students"
- "What's the energy efficiency of room allocation?"
- "Generate attendance predictions for next week"

### API Endpoints
- `POST /api/chat` - Process natural language queries
- `GET /api/chatbot/context` - Get available data context

## 📊 Frontend Features

### 1. Dashboard
- Real-time attendance tracking
- Interactive charts and visualizations
- User management interface

### 2. ML Analytics Page
- Department and section selection
- Attendance data visualization
- Risk assessment charts
- Model training controls

### 3. Chatbot Integration
- Direct access to chatbot interface
- Seamless integration with main application

## 🔌 API Integration

### Backend API (Port 4000)
```bash
# Authentication
POST /api/auth/login
POST /api/auth/register

# Attendance
POST /api/attendance
GET /api/attendance/:id

# Contact
POST /api/contact
```

### ML Service API (Port 8000)
```bash
# Data Access
GET /api/departments
GET /api/sections
GET /api/attendance/{dept}/{section}

# ML Operations
POST /api/train-models
POST /api/generate-energy-report
POST /api/export-attendance/{dept}/{section}

# Chatbot
POST /api/chat
GET /api/chatbot/context
```

## 🔒 Security Features

- **JWT Authentication**: Secure user sessions
- **Rate Limiting**: API protection against abuse
- **CORS Configuration**: Cross-origin request handling
- **Input Validation**: Data sanitization and validation
- **SQL Injection Prevention**: Parameterized queries

## 📈 Monitoring & Analytics

### Real-time Metrics
- Service health monitoring
- API response times
- Error tracking and logging

### Performance Analytics
- Attendance trend analysis
- Risk prediction accuracy
- Energy efficiency metrics

## 🐛 Troubleshooting

### Common Issues

1. **Port Conflicts**
   ```bash
   # Check if ports are in use
   netstat -ano | findstr :3000
   netstat -ano | findstr :4000
   netstat -ano | findstr :8000
   netstat -ano | findstr :3001
   ```

2. **ML Service Not Starting**
   ```bash
   # Check Python dependencies
   cd ml-service
   pip install -r requirements.txt
   ```

3. **Frontend Build Issues**
   ```bash
   # Clear cache and reinstall
   cd frontend
   rm -rf node_modules package-lock.json
   npm install
   ```

4. **Database Issues**
   ```bash
   # Reset database
   cd backend
   rm data/db.sqlite
   npm run dev
   ```

### Integration Testing

Run the integration test to verify all services:
```bash
python test-integration.py
```

## 🚀 Deployment

### Production Deployment

1. **Environment Setup**
   ```bash
   # Set production environment variables
   NODE_ENV=production
   JWT_SECRET=your-production-secret
   ```

2. **Build Applications**
   ```bash
   # Frontend
   cd frontend
   npm run build
   
   # Backend
   cd backend
   npm run build
   ```

3. **Docker Deployment**
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

### Scaling

- **Horizontal Scaling**: Use load balancers for multiple instances
- **Database Scaling**: Consider PostgreSQL for production
- **ML Model Serving**: Use dedicated ML serving infrastructure

## 📚 API Documentation

### Swagger Documentation
- ML Service: http://localhost:8000/docs
- Backend API: Available through Postman collection

### Postman Collection
Import the provided Postman collection for API testing.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

---

## 🎉 Success!

Your Smart Timetable & Attendance Management System is now fully integrated and ready to use! 

**Access Points:**
- 🌐 **Main Application**: http://localhost:3000
- 🤖 **Chatbot**: http://localhost:3001
- 📊 **ML Analytics**: http://localhost:3000/ml-predictions
- 🔧 **API Documentation**: http://localhost:8000/docs

**Next Steps:**
1. Add your data files to `ml-service/data/`
2. Train the ML models using the dashboard
3. Start using the chatbot for data queries
4. Monitor and optimize based on usage patterns
