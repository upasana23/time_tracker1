#!/usr/bin/env python3
"""
Comprehensive Test Script for Enhanced ML Features
Tests timetable optimization, attendance prediction, and notification alerts
"""

import requests
import json
import os
import time
from datetime import datetime

class EnhancedMLTester:
    def __init__(self):
        self.base_urls = {
            'ml_service': 'http://localhost:8000',
            'frontend': 'http://localhost:3000',
            'backend': 'http://localhost:4000'
        }
        self.results = []
        
    def log_test(self, test_name, status, message=""):
        timestamp = datetime.now().strftime("%H:%M:%S")
        result = {
            'test': test_name,
            'status': status,
            'message': message,
            'timestamp': timestamp
        }
        self.results.append(result)
        
        status_icon = "✅" if status == "PASS" else "❌" if status == "FAIL" else "⚠️"
        print(f"{status_icon} {timestamp} - {test_name}: {status}")
        if message:
            print(f"   └─ {message}")
    
    def test_timetable_optimization(self):
        """Test timetable optimization functionality"""
        print("\n🔍 Testing Timetable Optimization...")
        
        try:
            # Test timetable optimization endpoint
            response = requests.post(
                f"{self.base_urls['ml_service']}/api/optimize-timetable",
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'processing':
                    self.log_test("Timetable Optimization API", "PASS", "Optimization started successfully")
                else:
                    self.log_test("Timetable Optimization API", "FAIL", f"Unexpected response: {data}")
            else:
                self.log_test("Timetable Optimization API", "FAIL", f"HTTP {response.status_code}")
                
        except Exception as e:
            self.log_test("Timetable Optimization API", "FAIL", f"Error: {str(e)}")
        
        # Check if optimized timetable file exists
        try:
            timetable_path = "ml-service/data/timetable.csv"
            if os.path.exists(timetable_path):
                self.log_test("Optimized Timetable File", "PASS", "Timetable file exists")
            else:
                self.log_test("Optimized Timetable File", "WARN", "Timetable file not found")
        except Exception as e:
            self.log_test("Optimized Timetable File", "FAIL", f"Error: {str(e)}")
    
    def test_attendance_prediction(self):
        """Test attendance prediction functionality"""
        print("\n🔍 Testing Attendance Prediction...")
        
        try:
            # Test attendance prediction endpoint
            response = requests.post(
                f"{self.base_urls['ml_service']}/api/predict-attendance",
                params={'days_ahead': 30},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'processing':
                    self.log_test("Attendance Prediction API", "PASS", "Prediction started successfully")
                else:
                    self.log_test("Attendance Prediction API", "FAIL", f"Unexpected response: {data}")
            else:
                self.log_test("Attendance Prediction API", "FAIL", f"HTTP {response.status_code}")
                
        except Exception as e:
            self.log_test("Attendance Prediction API", "FAIL", f"Error: {str(e)}")
        
        # Check if prediction files exist
        try:
            predictions_path = "ml-service/data/attendance_predictions.csv"
            if os.path.exists(predictions_path):
                self.log_test("Attendance Predictions File", "PASS", "Predictions file exists")
            else:
                self.log_test("Attendance Predictions File", "WARN", "Predictions file not found")
        except Exception as e:
            self.log_test("Attendance Predictions File", "FAIL", f"Error: {str(e)}")
    
    def test_notification_system(self):
        """Test notification alert system"""
        print("\n🔍 Testing Notification System...")
        
        try:
            # Test notification endpoint
            response = requests.post(
                f"{self.base_urls['ml_service']}/api/send-notifications",
                params={'notification_type': 'high'},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'processing':
                    self.log_test("Notification System API", "PASS", "Notifications started successfully")
                else:
                    self.log_test("Notification System API", "FAIL", f"Unexpected response: {data}")
            else:
                self.log_test("Notification System API", "FAIL", f"HTTP {response.status_code}")
                
        except Exception as e:
            self.log_test("Notification System API", "FAIL", f"Error: {str(e)}")
    
    def test_attendance_status_queries(self):
        """Test attendance status query endpoints"""
        print("\n🔍 Testing Attendance Status Queries...")
        
        try:
            # Test risk summary endpoint
            response = requests.get(
                f"{self.base_urls['ml_service']}/api/risk-summary",
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'risk_distribution' in data and 'total_students' in data:
                    self.log_test("Risk Summary API", "PASS", f"Risk data for {data['total_students']} students")
                else:
                    self.log_test("Risk Summary API", "FAIL", "Invalid response format")
            else:
                self.log_test("Risk Summary API", "FAIL", f"HTTP {response.status_code}")
                
        except Exception as e:
            self.log_test("Risk Summary API", "FAIL", f"Error: {str(e)}")
        
        try:
            # Test individual student attendance status
            response = requests.get(
                f"{self.base_urls['ml_service']}/api/attendance-status/ST001",
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'student_id' in data and 'attendance_rate' in data:
                    self.log_test("Student Attendance Status API", "PASS", f"Status for student {data['student_id']}")
                else:
                    self.log_test("Student Attendance Status API", "FAIL", "Invalid response format")
            elif response.status_code == 404:
                self.log_test("Student Attendance Status API", "WARN", "Student not found (expected for test)")
            else:
                self.log_test("Student Attendance Status API", "FAIL", f"HTTP {response.status_code}")
                
        except Exception as e:
            self.log_test("Student Attendance Status API", "FAIL", f"Error: {str(e)}")
    
    def test_chatbot_integration(self):
        """Test chatbot integration with new ML features"""
        print("\n🔍 Testing Chatbot ML Integration...")
        
        # Test routine image generation
        try:
            response = requests.post(
                f"{self.base_urls['ml_service']}/api/chat",
                json={
                    "query": "What's my today's routine?",
                    "context": "timetable_attendance_system"
                },
                timeout=30
            )
            
            if response.status_code == 200:
                content_type = response.headers.get('content-type', '')
                if 'image' in content_type:
                    self.log_test("Chatbot Routine Image", "PASS", "Routine image generated successfully")
                else:
                    self.log_test("Chatbot Routine Image", "WARN", "Expected image but got: " + content_type)
            else:
                self.log_test("Chatbot Routine Image", "FAIL", f"HTTP {response.status_code}")
                
        except Exception as e:
            self.log_test("Chatbot Routine Image", "FAIL", f"Error: {str(e)}")
        
        # Test attendance queries
        try:
            response = requests.post(
                f"{self.base_urls['ml_service']}/api/chat",
                json={
                    "query": "What is my attendance status?",
                    "context": "timetable_attendance_system"
                },
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'response' in data:
                    self.log_test("Chatbot Attendance Query", "PASS", "Attendance response generated")
                else:
                    self.log_test("Chatbot Attendance Query", "FAIL", "Invalid response format")
            else:
                self.log_test("Chatbot Attendance Query", "FAIL", f"HTTP {response.status_code}")
                
        except Exception as e:
            self.log_test("Chatbot Attendance Query", "FAIL", f"Error: {str(e)}")
    
    def test_ml_model_files(self):
        """Test if ML model files are properly created"""
        print("\n🔍 Testing ML Model Files...")
        
        model_files = [
            "ml-service/src/timetable_optimizer.py",
            "ml-service/src/attendance_predictor.py", 
            "ml-service/src/notification_system.py"
        ]
        
        for model_file in model_files:
            try:
                if os.path.exists(model_file):
                    self.log_test(f"ML Model File: {os.path.basename(model_file)}", "PASS", "File exists")
                else:
                    self.log_test(f"ML Model File: {os.path.basename(model_file)}", "FAIL", "File not found")
            except Exception as e:
                self.log_test(f"ML Model File: {os.path.basename(model_file)}", "FAIL", f"Error: {str(e)}")
    
    def test_data_integration(self):
        """Test data integration between ML models and chatbot"""
        print("\n🔍 Testing Data Integration...")
        
        try:
            # Test that chatbot can access ML-generated data
            response = requests.get(
                f"{self.base_urls['ml_service']}/api/chatbot/context",
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'data_sources' in data:
                    self.log_test("Chatbot Data Context", "PASS", "Data sources available")
                else:
                    self.log_test("Chatbot Data Context", "FAIL", "Invalid response format")
            else:
                self.log_test("Chatbot Data Context", "FAIL", f"HTTP {response.status_code}")
                
        except Exception as e:
            self.log_test("Chatbot Data Context", "FAIL", f"Error: {str(e)}")
    
    def generate_report(self):
        """Generate comprehensive test report"""
        print("\n" + "="*70)
        print("📊 ENHANCED ML FEATURES TEST REPORT")
        print("="*70)
        
        total_tests = len(self.results)
        passed_tests = len([r for r in self.results if r['status'] == 'PASS'])
        failed_tests = len([r for r in self.results if r['status'] == 'FAIL'])
        warning_tests = len([r for r in self.results if r['status'] == 'WARN'])
        
        print(f"\n📈 Test Summary:")
        print(f"   Total Tests: {total_tests}")
        print(f"   ✅ Passed: {passed_tests}")
        print(f"   ❌ Failed: {failed_tests}")
        print(f"   ⚠️  Warnings: {warning_tests}")
        print(f"   Success Rate: {(passed_tests/total_tests*100):.1f}%")
        
        if failed_tests > 0:
            print(f"\n❌ Failed Tests:")
            for result in self.results:
                if result['status'] == 'FAIL':
                    print(f"   • {result['test']}: {result['message']}")
        
        if warning_tests > 0:
            print(f"\n⚠️  Warnings:")
            for result in self.results:
                if result['status'] == 'WARN':
                    print(f"   • {result['test']}: {result['message']}")
        
        print(f"\n🎯 Features Tested:")
        print("   • Timetable Optimization (ML-based)")
        print("   • Attendance Prediction (ML models)")
        print("   • Notification Alert System")
        print("   • Attendance Status Queries")
        print("   • Chatbot ML Integration")
        print("   • Data Integration & File Management")
        
        print(f"\n🚀 System Status:")
        if failed_tests == 0:
            print("   ✅ ENHANCED ML SYSTEM FULLY FUNCTIONAL")
            print("   All new features are working correctly!")
        elif failed_tests <= 2:
            print("   ⚠️  ENHANCED ML SYSTEM MOSTLY FUNCTIONAL")
            print("   Minor issues detected, but core functionality works.")
        else:
            print("   ❌ ENHANCED ML SYSTEM HAS ISSUES")
            print("   Multiple failures detected. Check service status.")
        
        # Save detailed report
        report_data = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total': total_tests,
                'passed': passed_tests,
                'failed': failed_tests,
                'warnings': warning_tests,
                'success_rate': (passed_tests/total_tests*100) if total_tests > 0 else 0
            },
            'results': self.results
        }
        
        with open('enhanced_ml_test_report.json', 'w') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"\n📄 Detailed report saved to: enhanced_ml_test_report.json")
        print("="*70)

def main():
    print("🚀 Starting Enhanced ML Features Test...")
    print("This will test all new ML capabilities including:")
    print("• Automatic timetable optimization")
    print("• ML-based attendance prediction")
    print("• Notification alert system")
    print("• Enhanced chatbot integration")
    print("• Data integration and file management")
    
    tester = EnhancedMLTester()
    
    try:
        # Run all tests
        tester.test_timetable_optimization()
        tester.test_attendance_prediction()
        tester.test_notification_system()
        tester.test_attendance_status_queries()
        tester.test_chatbot_integration()
        tester.test_ml_model_files()
        tester.test_data_integration()
        
        # Generate report
        tester.generate_report()
        
    except KeyboardInterrupt:
        print("\n⚠️  Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Test failed with error: {str(e)}")

if __name__ == "__main__":
    main()
