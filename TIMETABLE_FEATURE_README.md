# ML-Generated Timetable Feature

## Overview

The ML-Generated Timetable feature provides a comprehensive timetable management system with AI-powered optimization, facial recognition attendance, and real-time analytics. This feature is integrated into both the dedicated timetable page and the ML analysis dashboard.

## Features

### 🎯 Core Functionality
- **Full 9 AM to 5 PM Schedule**: Complete weekly routine with flexible 1-hour lunch break
- **Department & Section Selection**: User-configurable department and section inputs
- **ML-Generated Content**: Timetable data identical to ML-generated timetables
- **Real-time Attendance Tracking**: Live attendance monitoring with color-coded indicators
- **Current Time Highlighting**: Visual indication of current time slot

### 🤖 AI-Powered Features
- **Facial Recognition Demo**: Simulated face recognition attendance system
- **Low Attendance Alerts**: Automated notifications for at-risk students
- **ML Optimization**: AI-driven timetable optimization for maximum attendance
- **Risk Assessment**: Machine learning-based student risk analysis

### 📊 Analytics & Insights
- **Attendance Statistics**: Real-time attendance percentages and trends
- **Room Utilization**: Optimal room allocation and capacity management
- **Risk Factor Analysis**: Identification of attendance risk factors
- **Performance Metrics**: ML model accuracy and prediction performance

## Technical Architecture

### Frontend Components
- **Timetable Page**: `/frontend/app/timetable/page.tsx`
- **ML Analysis Dashboard**: `/frontend/app/ml-predictions/page.tsx`
- **UI Components**: Shadcn/ui components with Framer Motion animations
- **Responsive Design**: Mobile-friendly grid layout

### Backend Services
- **ML Service API**: `/ml-service/api.py` (Flask)
- **Data Sources**: CSV files in `/ml-service/data/`
- **Endpoints**:
  - `GET /api/timetable` - Fetch timetable data
  - `GET /api/attendance/alerts` - Get attendance alerts
  - `POST /api/face-recognition/demo` - Face recognition demo
  - `GET /api/timetable/statistics` - Timetable statistics

### Data Integration
- **Timetable Data**: `timetable.csv` - Core schedule information
- **Subject Data**: `subjects.csv` - Subject details and mappings
- **Teacher Data**: `teachers.csv` - Teacher information
- **Room Data**: `rooms.csv` - Room capacity and availability

## API Endpoints

### Timetable API
```http
GET http://localhost:5001/api/timetable?department={dept}&section={sec}
```

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "mon-09-00-10-00",
      "day": "Mon",
      "time": "09:00-10:00",
      "subject": "Distributed Systems",
      "teacher": "Rowan Williams",
      "room": "R020",
      "capacity": 30,
      "department": "Computer Science",
      "section": "A",
      "attendance": 85
    }
  ],
  "department": "Computer Science",
  "section": "A",
  "total_classes": 40
}
```

### Attendance Alerts API
```http
GET http://localhost:5001/api/attendance/alerts
```

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "studentId": "ST001",
      "studentName": "Alex Johnson",
      "attendance": 65,
      "riskLevel": "high",
      "lastSeen": "2024-01-15 14:30"
    }
  ],
  "total_alerts": 5,
  "high_risk_count": 3
}
```

### Face Recognition Demo API
```http
POST http://localhost:5001/api/face-recognition/demo
```

**Response:**
```json
{
  "success": true,
  "students_identified": 25,
  "total_students": 30,
  "attendance_percentage": 83.33,
  "recognition_time": "2.1 seconds",
  "confidence_score": 0.94
}
```

## Setup Instructions

### 1. Start ML Service
```bash
# Option 1: Use the batch script
start-ml-service.bat

# Option 2: Manual setup
cd ml-service
pip install -r requirements.txt
python api.py
```

### 2. Start Frontend
```bash
cd frontend
npm install
npm run dev
```

### 3. Access the Features
- **Timetable Page**: `http://localhost:3000/timetable`
- **ML Analysis Dashboard**: `http://localhost:3000/ml-predictions`
- **ML Service API**: `http://localhost:5001`

## Usage Guide

### Timetable Management
1. **Select Department & Section**: Choose from dropdown menus
2. **View Full Schedule**: Toggle between compact and full timetable views
3. **Monitor Attendance**: Real-time attendance percentages with color coding
4. **Export Data**: Download timetable in various formats

### ML Features
1. **Generate Predictions**: Run ML models for attendance prediction
2. **Optimize Timetable**: AI-powered schedule optimization
3. **Risk Assessment**: Analyze student risk factors
4. **Face Recognition**: Demo facial recognition attendance system

### Analytics Dashboard
1. **View Statistics**: Real-time performance metrics
2. **Monitor Trends**: Attendance prediction vs actual charts
3. **Risk Analysis**: Student risk factor impact visualization
4. **AI Insights**: Machine learning recommendations

## Data Structure

### Timetable CSV Format
```csv
department,section,day,slot,subject_id,teacher_id,room_id,room_capacity
Computer Science,A,Mon,12:00-13:00,S0009,T0064,R020,30
Computer Science,A,Mon,13:00-14:00,S0059,T0020,R005,40
```

### Subject CSV Format
```csv
subject_id,name,department
S0009,Distributed Systems,Computer Science
S0059,Linear Algebra,Computer Science
```

### Teacher CSV Format
```csv
teacher_id,name,department
T0064,Rowan Williams,Computer Science
T0020,Harper Jones,Computer Science
```

### Room CSV Format
```csv
room_id,capacity
R020,30
R005,40
```

## Customization Options

### Adding New Departments
1. Update CSV files with new department data
2. Add department options in frontend dropdowns
3. Configure ML models for new department patterns

### Modifying Time Slots
1. Edit `timeSlots` array in frontend components
2. Update API logic for new time ranges
3. Adjust ML optimization constraints

### Customizing Attendance Thresholds
1. Modify `getAttendanceColor` function
2. Update risk assessment criteria
3. Adjust ML model parameters

## Troubleshooting

### Common Issues

**ML Service Not Starting**
- Check Python installation: `python --version`
- Install dependencies: `pip install -r requirements.txt`
- Verify port 5001 is available

**Frontend API Errors**
- Ensure ML service is running on port 5001
- Check CORS configuration in Flask app
- Verify API endpoint URLs

**Data Loading Issues**
- Confirm CSV files exist in `/ml-service/data/`
- Check file permissions and formats
- Validate data structure matches expected schema

### Debug Mode
```bash
# Enable debug logging
export FLASK_DEBUG=1
python api.py
```

## Performance Optimization

### Frontend Optimizations
- Lazy loading for large timetable data
- Virtual scrolling for long lists
- Memoized components for frequent updates
- Optimized re-renders with React.memo

### Backend Optimizations
- Database indexing for fast queries
- Caching for frequently accessed data
- Async processing for ML operations
- Connection pooling for database operations

## Security Considerations

### API Security
- Input validation for all endpoints
- Rate limiting for API requests
- CORS configuration for frontend access
- Error handling without sensitive data exposure

### Data Privacy
- Anonymized student data in analytics
- Secure storage of attendance records
- Compliance with educational data regulations
- Audit logging for data access

## Future Enhancements

### Planned Features
- **Real-time Collaboration**: Multi-user timetable editing
- **Advanced ML Models**: Deep learning for attendance prediction
- **Mobile App**: Native mobile application
- **Integration APIs**: Third-party system integration
- **Advanced Analytics**: Predictive analytics and insights

### Technical Improvements
- **Microservices Architecture**: Service decomposition
- **Real-time Updates**: WebSocket integration
- **Offline Support**: Progressive Web App features
- **Performance Monitoring**: Application performance tracking

## Support & Documentation

### Additional Resources
- **API Documentation**: Swagger/OpenAPI specs
- **Component Library**: Storybook documentation
- **Testing Guide**: Unit and integration test examples
- **Deployment Guide**: Production deployment instructions

### Contact Information
- **Technical Support**: Development team
- **Feature Requests**: Product management
- **Bug Reports**: Issue tracking system

---

*This feature represents a comprehensive solution for educational timetable management with AI-powered optimization and real-time analytics.*
