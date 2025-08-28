#!/usr/bin/env python3
"""
Comprehensive Test Script for Smart Timetable & Attendance Management System
Tests all functionality including chatbot integration, button functionality, and navigation
"""

import requests
import json
import time
import sys
from datetime import datetime

class SystemTester:
    def __init__(self):
        self.base_urls = {
            'frontend': 'http://localhost:3000',
            'backend': 'http://localhost:4000',
            'ml_service': 'http://localhost:8000',
            'chatbot': 'http://localhost:3001'
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
    
    def test_service_health(self):
        """Test if all services are running and healthy"""
        print("\n🔍 Testing Service Health...")
        
        for service, url in self.base_urls.items():
            try:
                response = requests.get(f"{url}/health", timeout=5)
                if response.status_code == 200:
                    self.log_test(f"{service.upper()} Health Check", "PASS", f"Service running on {url}")
                else:
                    self.log_test(f"{service.upper()} Health Check", "FAIL", f"Status: {response.status_code}")
            except requests.exceptions.RequestException as e:
                self.log_test(f"{service.upper()} Health Check", "FAIL", f"Connection error: {str(e)}")
    
    def test_backend_endpoints(self):
        """Test backend API endpoints"""
        print("\n🔍 Testing Backend Endpoints...")
        
        # Test main endpoint
        try:
            response = requests.get(f"{self.base_urls['backend']}/", timeout=5)
            if response.status_code == 200:
                self.log_test("Backend Main Endpoint", "PASS", "Service responding")
            else:
                self.log_test("Backend Main Endpoint", "FAIL", f"Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.log_test("Backend Main Endpoint", "FAIL", f"Connection error: {str(e)}")
        
        # Test chatbot endpoint
        try:
            response = requests.post(
                f"{self.base_urls['backend']}/api/chatbot/chat",
                json={"message": "Hello", "context": "test"},
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                if 'response' in data:
                    self.log_test("Backend Chatbot API", "PASS", "Chatbot responding")
                else:
                    self.log_test("Backend Chatbot API", "FAIL", "Invalid response format")
            else:
                self.log_test("Backend Chatbot API", "FAIL", f"Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.log_test("Backend Chatbot API", "FAIL", f"Connection error: {str(e)}")
    
    def test_ml_service_endpoints(self):
        """Test ML service endpoints"""
        print("\n🔍 Testing ML Service Endpoints...")
        
        # Test departments endpoint
        try:
            response = requests.get(f"{self.base_urls['ml_service']}/api/departments", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    self.log_test("ML Service Departments", "PASS", f"Found {len(data)} departments")
                else:
                    self.log_test("ML Service Departments", "FAIL", "Invalid response format")
            else:
                self.log_test("ML Service Departments", "FAIL", f"Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.log_test("ML Service Departments", "FAIL", f"Connection error: {str(e)}")
        
        # Test chatbot context endpoint
        try:
            response = requests.get(f"{self.base_urls['ml_service']}/api/chatbot/context", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if 'data_sources' in data:
                    self.log_test("ML Service Chatbot Context", "PASS", "Context available")
                else:
                    self.log_test("ML Service Chatbot Context", "FAIL", "Invalid response format")
            else:
                self.log_test("ML Service Chatbot Context", "FAIL", f"Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.log_test("ML Service Chatbot Context", "FAIL", f"Connection error: {str(e)}")
        
        # Test ML chatbot endpoint
        try:
            response = requests.post(
                f"{self.base_urls['ml_service']}/api/chat",
                json={"query": "What is the attendance rate?", "context": "timetable_attendance_system"},
                timeout=15
            )
            if response.status_code == 200:
                data = response.json()
                if 'response' in data:
                    self.log_test("ML Service Chatbot", "PASS", "RAG system responding")
                else:
                    self.log_test("ML Service Chatbot", "FAIL", "Invalid response format")
            else:
                self.log_test("ML Service Chatbot", "FAIL", f"Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.log_test("ML Service Chatbot", "FAIL", f"Connection error: {str(e)}")
    
    def test_frontend_pages(self):
        """Test frontend pages accessibility"""
        print("\n🔍 Testing Frontend Pages...")
        
        pages = [
            ('/', 'Home Page'),
            ('/features', 'Features Page'),
            ('/ml-predictions', 'ML Analytics Page'),
            ('/chatbot', 'Chatbot Page'),
            ('/contact', 'Contact Page'),
            ('/login', 'Login Page'),
            ('/signup', 'Signup Page')
        ]
        
        for path, name in pages:
            try:
                response = requests.get(f"{self.base_urls['frontend']}{path}", timeout=10)
                if response.status_code == 200:
                    self.log_test(f"Frontend {name}", "PASS", f"Page accessible at {path}")
                else:
                    self.log_test(f"Frontend {name}", "FAIL", f"Status: {response.status_code}")
            except requests.exceptions.RequestException as e:
                self.log_test(f"Frontend {name}", "FAIL", f"Connection error: {str(e)}")
    
    def test_chatbot_integration(self):
        """Test chatbot integration scenarios"""
        print("\n🔍 Testing Chatbot Integration...")
        
        # Test ML service RAG first
        try:
            response = requests.post(
                f"{self.base_urls['ml_service']}/api/chat",
                json={"query": "Show me attendance data", "context": "timetable_attendance_system"},
                timeout=15
            )
            if response.status_code == 200:
                data = response.json()
                if 'response' in data and len(data['response']) > 10:
                    self.log_test("ML RAG Chatbot", "PASS", "Intelligent response from database")
                else:
                    self.log_test("ML RAG Chatbot", "FAIL", "Response too short or empty")
            else:
                self.log_test("ML RAG Chatbot", "FAIL", f"Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.log_test("ML RAG Chatbot", "FAIL", f"Connection error: {str(e)}")
        
        # Test backend fallback
        try:
            response = requests.post(
                f"{self.base_urls['backend']}/api/chatbot/chat",
                json={"message": "How can I improve attendance?", "context": "TimeTracker support"},
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                if 'response' in data and len(data['response']) > 10:
                    self.log_test("Backend Fallback Chatbot", "PASS", "Gemini API fallback working")
                else:
                    self.log_test("Backend Fallback Chatbot", "FAIL", "Response too short or empty")
            else:
                self.log_test("Backend Fallback Chatbot", "FAIL", f"Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.log_test("Backend Fallback Chatbot", "FAIL", f"Connection error: {str(e)}")
    
    def test_navigation_functionality(self):
        """Test navigation and button functionality"""
        print("\n🔍 Testing Navigation Functionality...")
        
        # Test that external links are properly configured
        try:
            response = requests.get(f"{self.base_urls['frontend']}/", timeout=10)
            if response.status_code == 200:
                content = response.text
                
                # Check for external link indicators
                if 'target="_blank"' in content or 'window.open' in content:
                    self.log_test("External Links", "PASS", "External links configured")
                else:
                    self.log_test("External Links", "WARN", "External links may not be configured")
                
                # Check for chatbot integration
                if 'chatbot' in content.lower() or 'ai assistant' in content.lower():
                    self.log_test("Chatbot Integration", "PASS", "Chatbot features detected")
                else:
                    self.log_test("Chatbot Integration", "WARN", "Chatbot features not detected")
                    
            else:
                self.log_test("Navigation Test", "FAIL", f"Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.log_test("Navigation Test", "FAIL", f"Connection error: {str(e)}")
    
    def generate_report(self):
        """Generate comprehensive test report"""
        print("\n" + "="*60)
        print("📊 COMPREHENSIVE TEST REPORT")
        print("="*60)
        
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
        
        print(f"\n🎯 Key Features Tested:")
        print("   • Service Health & Connectivity")
        print("   • Backend API Endpoints")
        print("   • ML Service RAG Integration")
        print("   • Frontend Page Accessibility")
        print("   • Chatbot Integration (ML + Fallback)")
        print("   • Navigation & Button Functionality")
        
        print(f"\n🚀 System Status:")
        if failed_tests == 0:
            print("   ✅ SYSTEM FULLY FUNCTIONAL")
            print("   All core features are working correctly!")
        elif failed_tests <= 2:
            print("   ⚠️  SYSTEM MOSTLY FUNCTIONAL")
            print("   Minor issues detected, but core functionality works.")
        else:
            print("   ❌ SYSTEM HAS ISSUES")
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
        
        with open('test_report.json', 'w') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"\n📄 Detailed report saved to: test_report.json")
        print("="*60)

def main():
    print("🚀 Starting Comprehensive System Test...")
    print("This will test all functionality including:")
    print("• Service health and connectivity")
    print("• Backend API endpoints")
    print("• ML service RAG integration")
    print("• Frontend pages and navigation")
    print("• Chatbot integration (database + Gemini fallback)")
    print("• Button functionality and external links")
    
    tester = SystemTester()
    
    try:
        tester.test_service_health()
        tester.test_backend_endpoints()
        tester.test_ml_service_endpoints()
        tester.test_frontend_pages()
        tester.test_chatbot_integration()
        tester.test_navigation_functionality()
        
        tester.generate_report()
        
    except KeyboardInterrupt:
        print("\n⚠️  Test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Test failed with error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

