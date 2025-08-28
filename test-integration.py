#!/usr/bin/env python3
"""
Integration test script for Smart Timetable & Attendance Management System
Tests all services and their communication
"""

import requests
import json
import time
import sys
from typing import Dict, List

class IntegrationTester:
    def __init__(self):
        self.base_urls = {
            'frontend': 'http://localhost:3000',
            'backend': 'http://localhost:4000',
            'ml_service': 'http://localhost:8000',
            'chatbot': 'http://localhost:3001'
        }
        self.results = {}

    def test_service_health(self, service_name: str, url: str) -> bool:
        """Test if a service is responding"""
        try:
            response = requests.get(f"{url}/health", timeout=5)
            if response.status_code == 200:
                print(f"✅ {service_name} is healthy")
                return True
            else:
                print(f"❌ {service_name} returned status {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"❌ {service_name} is not responding: {e}")
            return False

    def test_ml_service_endpoints(self) -> Dict:
        """Test ML service specific endpoints"""
        results = {}
        base_url = self.base_urls['ml_service']
        
        # Test departments endpoint
        try:
            response = requests.get(f"{base_url}/api/departments")
            if response.status_code == 200:
                data = response.json()
                results['departments'] = len(data.get('departments', []))
                print(f"✅ ML Service: Found {results['departments']} departments")
            else:
                print(f"❌ ML Service: Departments endpoint failed")
                results['departments'] = 0
        except Exception as e:
            print(f"❌ ML Service: Departments endpoint error: {e}")
            results['departments'] = 0

        # Test chatbot context endpoint
        try:
            response = requests.get(f"{base_url}/api/chatbot/context")
            if response.status_code == 200:
                data = response.json()
                results['chatbot_context'] = len(data.get('available_data', []))
                print(f"✅ ML Service: Chatbot context available with {results['chatbot_context']} data sources")
            else:
                print(f"❌ ML Service: Chatbot context endpoint failed")
                results['chatbot_context'] = 0
        except Exception as e:
            print(f"❌ ML Service: Chatbot context endpoint error: {e}")
            results['chatbot_context'] = 0

        # Test chat endpoint
        try:
            chat_payload = {
                "query": "What is the attendance rate?",
                "context": "timetable_attendance_system"
            }
            response = requests.post(f"{base_url}/api/chat", json=chat_payload)
            if response.status_code == 200:
                data = response.json()
                results['chat_response'] = len(data.get('response', '')) > 0
                print(f"✅ ML Service: Chat endpoint working")
            else:
                print(f"❌ ML Service: Chat endpoint failed")
                results['chat_response'] = False
        except Exception as e:
            print(f"❌ ML Service: Chat endpoint error: {e}")
            results['chat_response'] = False

        return results

    def test_backend_endpoints(self) -> Dict:
        """Test backend API endpoints"""
        results = {}
        base_url = self.base_urls['backend']
        
        # Test health endpoint
        try:
            response = requests.get(f"{base_url}/health")
            if response.status_code == 200:
                results['health'] = True
                print(f"✅ Backend: Health check passed")
            else:
                results['health'] = False
                print(f"❌ Backend: Health check failed")
        except Exception as e:
            results['health'] = False
            print(f"❌ Backend: Health check error: {e}")

        return results

    def test_chatbot_service(self) -> bool:
        """Test chatbot service"""
        try:
            response = requests.get(f"{self.base_urls['chatbot']}/", timeout=5)
            if response.status_code == 200:
                print(f"✅ Chatbot: Service responding")
                return True
            else:
                print(f"❌ Chatbot: Service returned status {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"❌ Chatbot: Service not responding: {e}")
            return False

    def run_all_tests(self) -> Dict:
        """Run all integration tests"""
        print("🚀 Starting Integration Tests...")
        print("=" * 50)

        # Test service health
        for service_name, url in self.base_urls.items():
            if service_name != 'frontend':  # Skip frontend for now
                self.results[f"{service_name}_health"] = self.test_service_health(service_name, url)

        print("\n" + "=" * 50)
        print("Testing ML Service Endpoints...")
        self.results['ml_endpoints'] = self.test_ml_service_endpoints()

        print("\n" + "=" * 50)
        print("Testing Backend Endpoints...")
        self.results['backend_endpoints'] = self.test_backend_endpoints()

        print("\n" + "=" * 50)
        print("Testing Chatbot Service...")
        self.results['chatbot_service'] = self.test_chatbot_service()

        return self.results

    def generate_report(self) -> str:
        """Generate a test report"""
        report = []
        report.append("📊 Integration Test Report")
        report.append("=" * 50)
        
        # Service health summary
        health_services = [k for k, v in self.results.items() if k.endswith('_health') and v]
        report.append(f"✅ Healthy Services: {len(health_services)}/3")
        
        # ML service summary
        if 'ml_endpoints' in self.results:
            ml_results = self.results['ml_endpoints']
            report.append(f"🧠 ML Service Features:")
            report.append(f"  - Departments: {ml_results.get('departments', 0)}")
            report.append(f"  - Data Sources: {ml_results.get('chatbot_context', 0)}")
            report.append(f"  - Chat Function: {'✅' if ml_results.get('chat_response') else '❌'}")
        
        # Backend summary
        if 'backend_endpoints' in self.results:
            backend_results = self.results['backend_endpoints']
            report.append(f"🔧 Backend Features:")
            report.append(f"  - Health Check: {'✅' if backend_results.get('health') else '❌'}")
        
        # Chatbot summary
        report.append(f"🤖 Chatbot Service: {'✅' if self.results.get('chatbot_service') else '❌'}")
        
        # Overall status
        total_tests = len([k for k in self.results.keys() if not k.endswith('_endpoints')])
        passed_tests = len([k for k, v in self.results.items() if not k.endswith('_endpoints') and v])
        report.append(f"\n📈 Overall: {passed_tests}/{total_tests} tests passed")
        
        return "\n".join(report)

def main():
    tester = IntegrationTester()
    
    # Wait a bit for services to start
    print("⏳ Waiting for services to start...")
    time.sleep(2)
    
    # Run tests
    results = tester.run_all_tests()
    
    # Generate and print report
    print("\n" + "=" * 50)
    print(tester.generate_report())
    
    # Exit with appropriate code
    total_tests = len([k for k in results.keys() if not k.endswith('_endpoints')])
    passed_tests = len([k for k, v in results.items() if not k.endswith('_endpoints') and v])
    
    if passed_tests == total_tests:
        print("\n🎉 All tests passed! System is ready.")
        sys.exit(0)
    else:
        print(f"\n⚠️  {total_tests - passed_tests} tests failed. Please check the services.")
        sys.exit(1)

if __name__ == "__main__":
    main()
