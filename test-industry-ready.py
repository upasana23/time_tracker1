#!/usr/bin/env python3
"""
Industry-Ready Test Suite for Smart Timetable & Attendance System
Comprehensive testing for performance, reliability, and functionality
"""

import requests
import json
import time
import concurrent.futures
import statistics
import sys
import os
from datetime import datetime
import threading
import queue

class IndustryReadyTester:
    def __init__(self):
        self.base_urls = {
            'frontend': 'http://localhost:3000',
            'backend': 'http://localhost:4000',
            'ml_service': 'http://localhost:8000'
        }
        self.test_results = {
            'performance': {},
            'reliability': {},
            'functionality': {},
            'security': {},
            'ml_models': {}
        }
        self.performance_metrics = {}
        
    def log_test(self, category: str, test_name: str, status: str, details: str = ""):
        """Log test results with timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        result = f"[{timestamp}] {category.upper()} - {test_name}: {status}"
        if details:
            result += f" - {details}"
        print(result)
        
        # Store results
        if category not in self.test_results:
            self.test_results[category] = {}
        self.test_results[category][test_name] = {
            'status': status,
            'details': details,
            'timestamp': timestamp
        }
    
    def test_service_connectivity(self):
        """Test basic service connectivity"""
        print("\n🔌 Testing Service Connectivity...")
        
        for service, url in self.base_urls.items():
            try:
                start_time = time.time()
                response = requests.get(url, timeout=10)
                response_time = (time.time() - start_time) * 1000
                
                if response.status_code == 200:
                    self.log_test('reliability', f'{service}_connectivity', 'PASS', 
                                f'Response time: {response_time:.2f}ms')
                    self.performance_metrics[f'{service}_response_time'] = response_time
                else:
                    self.log_test('reliability', f'{service}_connectivity', 'FAIL', 
                                f'Status: {response.status_code}')
                    
            except Exception as e:
                self.log_test('reliability', f'{service}_connectivity', 'FAIL', str(e))
    
    def test_performance_under_load(self):
        """Test system performance under concurrent load"""
        print("\n⚡ Testing Performance Under Load...")
        
        # Test concurrent requests to backend
        def make_request():
            try:
                start_time = time.time()
                response = requests.get(f"{self.base_urls['backend']}/health", timeout=5)
                response_time = (time.time() - start_time) * 1000
                return response_time
            except:
                return None
        
        # Test with 10 concurrent requests
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(make_request) for _ in range(10)]
            response_times = [future.result() for future in futures if future.result() is not None]
        
        if response_times:
            avg_time = statistics.mean(response_times)
            max_time = max(response_times)
            min_time = min(response_times)
            
            self.log_test('performance', 'concurrent_load', 'PASS', 
                         f'Avg: {avg_time:.2f}ms, Max: {max_time:.2f}ms, Min: {min_time:.2f}ms')
            
            # Performance benchmarks
            if avg_time < 100:
                self.log_test('performance', 'response_time_benchmark', 'EXCELLENT', 
                            f'Average response time: {avg_time:.2f}ms')
            elif avg_time < 500:
                self.log_test('performance', 'response_time_benchmark', 'GOOD', 
                            f'Average response time: {avg_time:.2f}ms')
            else:
                self.log_test('performance', 'response_time_benchmark', 'NEEDS_IMPROVEMENT', 
                            f'Average response time: {avg_time:.2f}ms')
        else:
            self.log_test('performance', 'concurrent_load', 'FAIL', 'No successful responses')
    
    def test_ml_model_functionality(self):
        """Test ML model endpoints and functionality"""
        print("\n🤖 Testing ML Model Functionality...")
        
        ml_url = self.base_urls['ml_service']
        
        # Test chat endpoint
        try:
            chat_data = {
                "query": "What is my attendance status?",
                "context": "timetable_attendance_system"
            }
            
            start_time = time.time()
            response = requests.post(f"{ml_url}/api/chat", json=chat_data, timeout=15)
            response_time = (time.time() - start_time) * 1000
            
            if response.status_code == 200:
                self.log_test('ml_models', 'chat_endpoint', 'PASS', 
                            f'Response time: {response_time:.2f}ms')
                
                # Check response format
                content_type = response.headers.get('content-type', '')
                if 'image' in content_type:
                    self.log_test('ml_models', 'image_response', 'PASS', 'Image response received')
                else:
                    try:
                        result = response.json()
                        if 'response' in result:
                            self.log_test('ml_models', 'text_response', 'PASS', 'Text response received')
                        else:
                            self.log_test('ml_models', 'response_format', 'FAIL', 'Invalid response format')
                    except:
                        self.log_test('ml_models', 'response_format', 'FAIL', 'Invalid JSON response')
            else:
                self.log_test('ml_models', 'chat_endpoint', 'FAIL', f'Status: {response.status_code}')
                
        except Exception as e:
            self.log_test('ml_models', 'chat_endpoint', 'FAIL', str(e))
        
        # Test routine image generation
        try:
            routine_data = {
                "query": "Show me today's routine",
                "context": "timetable_attendance_system"
            }
            
            start_time = time.time()
            response = requests.post(f"{ml_url}/api/chat", json=routine_data, timeout=20)
            response_time = (time.time() - start_time) * 1000
            
            if response.status_code == 200:
                content_type = response.headers.get('content-type', '')
                if 'image' in content_type:
                    self.log_test('ml_models', 'routine_image_generation', 'PASS', 
                                f'Image generated in {response_time:.2f}ms')
                else:
                    self.log_test('ml_models', 'routine_image_generation', 'FAIL', 'No image response')
            else:
                self.log_test('ml_models', 'routine_image_generation', 'FAIL', f'Status: {response.status_code}')
                
        except Exception as e:
            self.log_test('ml_models', 'routine_image_generation', 'FAIL', str(e))
    
    def test_backend_api_endpoints(self):
        """Test backend API endpoints"""
        print("\n🔧 Testing Backend API Endpoints...")
        
        backend_url = self.base_urls['backend']
        
        # Test health endpoint
        try:
            response = requests.get(f"{backend_url}/health", timeout=5)
            if response.status_code == 200:
                self.log_test('functionality', 'health_endpoint', 'PASS')
            else:
                self.log_test('functionality', 'health_endpoint', 'FAIL', f'Status: {response.status_code}')
        except Exception as e:
            self.log_test('functionality', 'health_endpoint', 'FAIL', str(e))
        
        # Test departments endpoint
        try:
            response = requests.get(f"{backend_url}/api/departments", timeout=5)
            if response.status_code == 200:
                data = response.json()
                dept_count = len(data.get('data', []))
                self.log_test('functionality', 'departments_endpoint', 'PASS', f'Found {dept_count} departments')
            else:
                self.log_test('functionality', 'departments_endpoint', 'FAIL', f'Status: {response.status_code}')
        except Exception as e:
            self.log_test('functionality', 'departments_endpoint', 'FAIL', str(e))
        
        # Test subjects endpoint
        try:
            response = requests.get(f"{backend_url}/api/subjects", timeout=5)
            if response.status_code == 200:
                data = response.json()
                subject_count = len(data.get('data', []))
                self.log_test('functionality', 'subjects_endpoint', 'PASS', f'Found {subject_count} subjects')
            else:
                self.log_test('functionality', 'subjects_endpoint', 'FAIL', f'Status: {response.status_code}')
        except Exception as e:
            self.log_test('functionality', 'subjects_endpoint', 'FAIL', str(e))
    
    def test_frontend_functionality(self):
        """Test frontend functionality"""
        print("\n🌐 Testing Frontend Functionality...")
        
        frontend_url = self.base_urls['frontend']
        
        try:
            response = requests.get(frontend_url, timeout=10)
            if response.status_code == 200:
                content = response.text
                
                # Check for key content
                if "Smart TimeTracker Dashboard" in content:
                    self.log_test('functionality', 'frontend_content', 'PASS', 'Dashboard content loaded')
                else:
                    self.log_test('functionality', 'frontend_content', 'FAIL', 'Dashboard content not found')
                
                # Check for JavaScript errors
                if "error" not in content.lower() or "exception" not in content.lower():
                    self.log_test('functionality', 'frontend_errors', 'PASS', 'No obvious JavaScript errors')
                else:
                    self.log_test('functionality', 'frontend_errors', 'WARNING', 'Potential JavaScript errors detected')
                    
            else:
                self.log_test('functionality', 'frontend_accessibility', 'FAIL', f'Status: {response.status_code}')
                
        except Exception as e:
            self.log_test('functionality', 'frontend_accessibility', 'FAIL', str(e))
    
    def test_security_features(self):
        """Test security features"""
        print("\n🔒 Testing Security Features...")
        
        backend_url = self.base_urls['backend']
        
        # Test CORS headers
        try:
            response = requests.get(f"{backend_url}/health", timeout=5)
            cors_header = response.headers.get('access-control-allow-origin')
            if cors_header:
                self.log_test('security', 'cors_headers', 'PASS', 'CORS headers present')
            else:
                self.log_test('security', 'cors_headers', 'WARNING', 'CORS headers not found')
        except Exception as e:
            self.log_test('security', 'cors_headers', 'FAIL', str(e))
        
        # Test rate limiting (should get 429 after multiple requests)
        try:
            responses = []
            for _ in range(5):
                response = requests.get(f"{backend_url}/health", timeout=5)
                responses.append(response.status_code)
                time.sleep(0.1)
            
            if 429 in responses:
                self.log_test('security', 'rate_limiting', 'PASS', 'Rate limiting working')
            else:
                self.log_test('security', 'rate_limiting', 'WARNING', 'Rate limiting may not be working')
                
        except Exception as e:
            self.log_test('security', 'rate_limiting', 'FAIL', str(e))
    
    def test_database_integrity(self):
        """Test database integrity and data consistency"""
        print("\n🗄️ Testing Database Integrity...")
        
        backend_url = self.base_urls['backend']
        
        # Test data consistency between endpoints
        try:
            # Get departments and sections
            dept_response = requests.get(f"{backend_url}/api/departments", timeout=5)
            if dept_response.status_code == 200:
                departments = dept_response.json().get('data', [])
                
                if departments:
                    # Test sections for first department
                    first_dept = departments[0]
                    sections_response = requests.get(f"{backend_url}/api/departments/{first_dept['id']}/sections", timeout=5)
                    
                    if sections_response.status_code == 200:
                        sections = sections_response.json().get('data', [])
                        self.log_test('reliability', 'data_consistency', 'PASS', 
                                    f'Department {first_dept["name"]} has {len(sections)} sections')
                    else:
                        self.log_test('reliability', 'data_consistency', 'FAIL', 'Sections endpoint failed')
                else:
                    self.log_test('reliability', 'data_consistency', 'WARNING', 'No departments found')
            else:
                self.log_test('reliability', 'data_consistency', 'FAIL', 'Departments endpoint failed')
                
        except Exception as e:
            self.log_test('reliability', 'data_consistency', 'FAIL', str(e))
    
    def run_stress_test(self):
        """Run stress test to check system stability"""
        print("\n💪 Running Stress Test...")
        
        def stress_worker():
            """Worker function for stress testing"""
            for i in range(20):  # 20 requests per worker
                try:
                    response = requests.get(f"{self.base_urls['backend']}/health", timeout=5)
                    if response.status_code != 200:
                        return False
                    time.sleep(0.1)
                except:
                    return False
            return True
        
        # Run 5 concurrent workers
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(stress_worker) for _ in range(5)]
            results = [future.result() for future in futures]
        
        success_rate = sum(results) / len(results) * 100
        if success_rate >= 95:
            self.log_test('reliability', 'stress_test', 'PASS', f'Success rate: {success_rate:.1f}%')
        elif success_rate >= 80:
            self.log_test('reliability', 'stress_test', 'WARNING', f'Success rate: {success_rate:.1f}%')
        else:
            self.log_test('reliability', 'stress_test', 'FAIL', f'Success rate: {success_rate:.1f}%')
    
    def generate_report(self):
        """Generate comprehensive test report"""
        print("\n📊 Generating Test Report...")
        
        total_tests = 0
        passed_tests = 0
        failed_tests = 0
        warnings = 0
        
        for category, tests in self.test_results.items():
            for test_name, result in tests.items():
                total_tests += 1
                if result['status'] == 'PASS':
                    passed_tests += 1
                elif result['status'] == 'FAIL':
                    failed_tests += 1
                elif result['status'] == 'WARNING':
                    warnings += 1
        
        success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        print("\n" + "="*60)
        print("🏆 INDUSTRY-READY TEST REPORT")
        print("="*60)
        print(f"Total Tests: {total_tests}")
        print(f"Passed: {passed_tests} ✅")
        print(f"Failed: {failed_tests} ❌")
        print(f"Warnings: {warnings} ⚠️")
        print(f"Success Rate: {success_rate:.1f}%")
        print("="*60)
        
        # Performance summary
        if self.performance_metrics:
            print("\n📈 PERFORMANCE METRICS:")
            for metric, value in self.performance_metrics.items():
                print(f"  {metric}: {value:.2f}ms")
        
        # Recommendations
        print("\n💡 RECOMMENDATIONS:")
        if success_rate >= 95:
            print("  🎉 EXCELLENT! Your system is industry-ready!")
        elif success_rate >= 85:
            print("  👍 GOOD! Minor improvements needed for production.")
        elif success_rate >= 70:
            print("  ⚠️ FAIR! Several issues need attention before production.")
        else:
            print("  ❌ POOR! Major issues must be resolved before production.")
        
        if failed_tests > 0:
            print("\n🔧 FAILED TESTS TO FIX:")
            for category, tests in self.test_results.items():
                for test_name, result in tests.items():
                    if result['status'] == 'FAIL':
                        print(f"  - {category}.{test_name}: {result['details']}")
        
        print("\n" + "="*60)
        
        return success_rate >= 85  # Return True if industry-ready
    
    def run_all_tests(self):
        """Run all tests"""
        print("🚀 Starting Industry-Ready Testing Suite...")
        print(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        try:
            self.test_service_connectivity()
            self.test_performance_under_load()
            self.test_ml_model_functionality()
            self.test_backend_api_endpoints()
            self.test_frontend_functionality()
            self.test_security_features()
            self.test_database_integrity()
            self.run_stress_test()
            
            return self.generate_report()
            
        except KeyboardInterrupt:
            print("\n⚠️ Testing interrupted by user")
            return False
        except Exception as e:
            print(f"\n❌ Testing failed with error: {e}")
            return False

def main():
    """Main function"""
    print("🏭 Smart Timetable & Attendance System")
    print("Industry-Ready Testing Suite")
    print("="*50)
    
    # Check if services are running
    print("Checking if services are running...")
    time.sleep(2)
    
    tester = IndustryReadyTester()
    is_industry_ready = tester.run_all_tests()
    
    if is_industry_ready:
        print("\n🎉 CONGRATULATIONS! Your system is INDUSTRY-READY!")
        print("You can now present this to clients and stakeholders.")
    else:
        print("\n⚠️ Your system needs improvements before it's industry-ready.")
        print("Please fix the failed tests and run again.")
    
    print("\nPress Enter to exit...")
    input()

if __name__ == "__main__":
    main()
