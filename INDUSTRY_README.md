# 🚀 Smart Timetable & Attendance System

**Industry-Ready Machine Learning-Powered Educational Management Platform**

## 🌟 Features

### Core Functionality
- **Smart Attendance Tracking** - ML-powered attendance prediction and risk assessment
- **Intelligent Timetabling** - AI-optimized class schedules with constraint handling
- **Real-time Analytics** - Interactive dashboards with predictive insights
- **AI Chatbot** - RAG-enabled intelligent assistant for student queries
- **Risk Management** - Automated attendance risk detection and notifications
- **Multi-platform Support** - Web-based frontend with responsive design

### Technical Highlights
- **Machine Learning Integration** - Random Forest, Gradient Boosting, and heuristic algorithms
- **RAG System** - Retrieval-Augmented Generation for intelligent responses
- **Real-time Processing** - Background task processing for ML operations
- **Scalable Architecture** - Microservices-based design with Docker support
- **Data Persistence** - SQLite database with optimized schemas
- **API-First Design** - RESTful APIs for seamless integration

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │   ML Service    │
│   (Next.js)     │◄──►│   (Node.js)     │◄──►│   (FastAPI)     │
│                 │    │                 │    │                 │
│ • Dashboard     │    │ • REST APIs     │    │ • ML Models     │
│ • Analytics     │    │ • Auth          │    │ • RAG System    │
│ • Live Chat     │    │ • Database      │    │ • Predictions   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Chatbot       │    │   Database      │    │   ML Outputs    │
│   (Static HTML) │    │   (SQLite)      │    │   (CSV/Images)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** with pip
- **Node.js 16+** with npm
- **Git** for version control

### 1. Clone & Setup
```bash
git clone <repository-url>
cd smart-timetable-attendance
```

### 2. One-Click Startup (Windows)
```bash
start-project.bat
```

### 3. Manual Setup (Alternative)
```bash
# Install dependencies
cd backend && npm install
cd ../frontend && npm install  
cd ../ml-service && pip install -r requirements.txt

# Initialize database
cd ../backend
node -e "
const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');
const schema = fs.readFileSync('src/scripts/init_db.sql', 'utf8');
const db = new sqlite3.Database('../data/db.sqlite');
db.exec(schema, (err) => {
    if (err) console.error('DB init error:', err);
    else console.log('Database initialized');
    db.close();
});
"

# Start services (in separate terminals)
cd backend && npm run dev      # Backend on :4000
cd frontend && npm run dev     # Frontend on :3000  
cd ml-service && python api_server.py  # ML Service on :8000
```

## 🌐 Access Points

| Service | URL | Description |
|---------|-----|-------------|
| **Frontend** | http://localhost:3000 | Main application dashboard |
| **Backend API** | http://localhost:4000 | REST API endpoints |
| **ML Service** | http://localhost:8000 | Machine learning APIs |
| **API Docs** | http://localhost:8000/docs | FastAPI documentation |
| **Chatbot** | http://localhost:3001 | AI assistant interface |

## 🔧 Configuration

### Environment Variables
Create `.env` file in the root directory:

```env
# Backend Configuration
PORT=4000
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# ML Service Configuration  
ML_SERVICE_PORT=8000
GEMINI_API_KEY=your_gemini_api_key_here

# Database Configuration
DATABASE_URL=sqlite:///./data/db.sqlite

# Email Configuration (for notifications)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

### Database Schema
The system automatically creates these tables:
- `users` - User authentication and roles
- `departments` - Academic departments
- `sections` - Class sections per department  
- `students` - Student information
- `teachers` - Faculty information
- `subjects` - Course catalog
- `rooms` - Classroom and lab facilities
- `timetable` - Class schedules
- `attendance` - Student attendance records

## 📊 ML Models & Features

### 1. Timetable Optimization
- **Algorithm**: Random Forest Regressor + Heuristic Optimization
- **Features**: Room capacity, teacher availability, subject constraints
- **Output**: Optimized weekly schedules with conflict resolution

### 2. Attendance Prediction
- **Algorithm**: Random Forest Classifier + Gradient Boosting
- **Features**: Historical patterns, time-based factors, student demographics
- **Output**: Future attendance probabilities and risk scores

### 3. Risk Assessment
- **Algorithm**: Rule-based + ML classification
- **Features**: Attendance rates, consecutive absences, subject performance
- **Output**: Risk levels (Low/Medium/High/Critical) with intervention recommendations

### 4. RAG System
- **Knowledge Base**: CSV data, ML outputs, generated reports
- **Search**: Semantic similarity and keyword matching
- **Response**: Context-aware answers with fallback to Gemini API

## 🧪 Testing & Validation

### Automated Testing
```bash
# Test all functionality
python test-chatbot.py

# Test ML features specifically
python test-enhanced-ml-features.py

# Test routine image generation
python test-routine-image.py
```

### Manual Testing Checklist
- [ ] Frontend loads without errors
- [ ] Department/Section dropdowns populate correctly
- [ ] Attendance recording works
- [ ] ML analytics display properly
- [ ] Chatbot responds to queries
- [ ] Routine images generate correctly
- [ ] All navigation links work
- [ ] External links open in new tabs

## 🔒 Security Features

- **Authentication**: JWT-based user authentication
- **Authorization**: Role-based access control
- **Input Validation**: Comprehensive request validation
- **Rate Limiting**: API request throttling
- **CORS Protection**: Cross-origin request security
- **SQL Injection Prevention**: Parameterized queries

## 📈 Performance & Scalability

- **Database Indexing**: Optimized queries with proper indexes
- **Background Processing**: Non-blocking ML operations
- **Caching**: Intelligent data caching strategies
- **Load Balancing**: Ready for horizontal scaling
- **Monitoring**: Health check endpoints and logging

## 🚀 Deployment

### Production Considerations
1. **Environment Variables**: Secure configuration management
2. **Database**: Consider PostgreSQL for production workloads
3. **Caching**: Implement Redis for session and data caching
4. **Monitoring**: Add application performance monitoring
5. **SSL/TLS**: Enable HTTPS for all endpoints
6. **Backup**: Implement automated database backups

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up -d

# Scale services
docker-compose up -d --scale ml-service=3
```

## 🛠️ Development

### Project Structure
```
smart-timetable-attendance/
├── frontend/                 # Next.js frontend
├── backend/                  # Node.js backend
├── ml-service/              # Python ML service
├── chatbot/                 # Static chatbot interface
├── data/                    # Database and CSV files
├── scripts/                 # Utility scripts
└── docs/                    # Documentation
```

### Adding New Features
1. **Backend**: Add routes in `backend/src/routes/`
2. **Frontend**: Create components in `frontend/components/`
3. **ML Service**: Add endpoints in `ml-service/api_server.py`
4. **Database**: Update schema in `backend/src/scripts/init_db.sql`

## 📚 API Documentation

### Core Endpoints

#### Attendance Management
- `POST /api/attendance` - Record attendance
- `GET /api/attendance` - List attendance records

#### Academic Data
- `GET /api/departments` - List departments
- `GET /api/departments/:id/sections` - Get sections by department
- `GET /api/subjects` - List subjects
- `GET /api/subjects/department/:id` - Get subjects by department

#### ML Services
- `POST /api/ml/chat` - AI chatbot queries
- `POST /api/ml/optimize-timetable` - Generate optimal schedules
- `POST /api/ml/predict-attendance` - Predict future attendance
- `POST /api/ml/send-notifications` - Send risk alerts

## 🤝 Contributing

### Development Workflow
1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open Pull Request

### Code Standards
- **Python**: PEP 8, type hints, docstrings
- **JavaScript/TypeScript**: ESLint, Prettier, JSDoc
- **SQL**: Consistent naming, proper indexing
- **Testing**: Unit tests for all new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Common Issues
1. **Port conflicts**: Ensure ports 3000, 4000, 8000 are available
2. **Database errors**: Check if `data/` directory exists and is writable
3. **ML service issues**: Verify Python dependencies are installed
4. **Frontend not loading**: Check if backend is running on port 4000

### Getting Help
- **Documentation**: Check this README and inline code comments
- **Issues**: Open GitHub issues for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions and ideas

## 🎯 Roadmap

### Phase 1 (Current) ✅
- [x] Core attendance tracking
- [x] Basic ML predictions
- [x] RAG chatbot
- [x] Timetable optimization

### Phase 2 (Next) 🚧
- [ ] Mobile app development
- [ ] Advanced analytics dashboard
- [ ] Integration with LMS systems
- [ ] Multi-language support

### Phase 3 (Future) 🔮
- [ ] AI-powered content recommendations
- [ ] Predictive maintenance for facilities
- [ ] Advanced student performance analytics
- [ ] Blockchain-based credential verification

---

**Built with ❤️ using Next.js, Node.js, FastAPI, and Machine Learning**

*For enterprise support and custom development, contact our team.*
