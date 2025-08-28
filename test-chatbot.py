#!/usr/bin/env python3
"""
Test script for chatbot and ML service functionality
"""

import requests
import json
import time

def test_ml_service():
    """Test ML service endpoints"""
    base_url = "http://localhost:8000"
    
    print("🧪 Testing ML Service...")
    
    # Test basic connectivity
    try:
        response = requests.get(f"{base_url}/docs", timeout=5)
        if response.status_code == 200:
            print("✅ ML Service is running and accessible")
        else:
            print("⚠️ ML Service responded but with unexpected status")
    except requests.exceptions.RequestException as e:
        print(f"❌ ML Service is not accessible: {e}")
        return False
    
    # Test chat endpoint
    try:
        chat_data = {
            "query": "What is my attendance status?",
            "context": "timetable_attendance_system"
        }
        response = requests.post(f"{base_url}/api/chat", json=chat_data, timeout=10)
        
        if response.status_code == 200:
            content_type = response.headers.get('content-type', '')
            if 'image' in content_type:
                print("✅ Chat endpoint working - received image response")
            else:
                result = response.json()
                print(f"✅ Chat endpoint working - received text response: {result.get('response', 'No response')[:100]}...")
        else:
            print(f"❌ Chat endpoint failed with status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Chat endpoint test failed: {e}")
        return False
    
    # Test routine image generation
    try:
        routine_data = {
            "query": "Show me today's routine",
            "context": "timetable_attendance_system"
        }
        response = requests.post(f"{base_url}/api/chat", json=routine_data, timeout=15)
        
        if response.status_code == 200:
            content_type = response.headers.get('content-type', '')
            if 'image' in content_type:
                print("✅ Routine image generation working")
                # Save the image for verification
                with open("test_routine.jpg", "wb") as f:
                    f.write(response.content)
                print("💾 Saved routine image as 'test_routine.jpg'")
            else:
                print("⚠️ Routine query didn't return image")
        else:
            print(f"❌ Routine image generation failed with status {response.status_code}")
            
    except Exception as e:
        print(f"❌ Routine image test failed: {e}")
    
    return True

def test_backend():
    """Test backend API endpoints"""
    base_url = "http://localhost:4000"
    
    print("\n🧪 Testing Backend API...")
    
    # Test basic connectivity
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Backend is running and accessible")
        else:
            print("⚠️ Backend responded but with unexpected status")
    except requests.exceptions.RequestException as e:
        print(f"❌ Backend is not accessible: {e}")
        return False
    
    # Test departments endpoint
    try:
        response = requests.get(f"{base_url}/api/departments", timeout=5)
        if response.status_code == 200:
            data = response.json()
            depts = data.get('data', [])
            print(f"✅ Departments endpoint working - found {len(depts)} departments")
            for dept in depts[:3]:  # Show first 3
                print(f"   - {dept['name']} ({dept['code']})")
        else:
            print(f"❌ Departments endpoint failed with status {response.status_code}")
            
    except Exception as e:
        print(f"❌ Departments test failed: {e}")
    
    # Test subjects endpoint
    try:
        response = requests.get(f"{base_url}/api/subjects", timeout=5)
        if response.status_code == 200:
            data = response.json()
            subjects = data.get('data', [])
            print(f"✅ Subjects endpoint working - found {len(subjects)} subjects")
            for subject in subjects[:3]:  # Show first 3
                print(f"   - {subject['name']} ({subject['code']})")
        else:
            print(f"❌ Subjects endpoint failed with status {response.status_code}")
            
    except Exception as e:
        print(f"❌ Subjects test failed: {e}")
    
    return True

def test_frontend():
    """Test frontend accessibility"""
    base_url = "http://localhost:3000"
    
    print("\n🧪 Testing Frontend...")
    
    try:
        response = requests.get(base_url, timeout=10)
        if response.status_code == 200:
            print("✅ Frontend is accessible")
            if "Smart TimeTracker Dashboard" in response.text:
                print("✅ Frontend content loaded correctly")
            else:
                print("⚠️ Frontend loaded but content may be incomplete")
        else:
            print(f"❌ Frontend responded with status {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Frontend is not accessible: {e}")
        return False
    
    return True

def main():
    """Run all tests"""
    print("🚀 Starting comprehensive system test...")
    print("=" * 50)
    
    # Wait a bit for services to start
    print("⏳ Waiting for services to start...")
    time.sleep(5)
    
    # Test each service
    ml_ok = test_ml_service()
    backend_ok = test_backend()
    frontend_ok = test_frontend()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)
    
    if ml_ok:
        print("✅ ML Service: Working")
    else:
        print("❌ ML Service: Failed")
    
    if backend_ok:
        print("✅ Backend API: Working")
    else:
        print("❌ Backend API: Failed")
    
    if frontend_ok:
        print("✅ Frontend: Working")
    else:
        print("❌ Frontend: Failed")
    
    if all([ml_ok, backend_ok, frontend_ok]):
        print("\n🎉 All systems are working correctly!")
        print("You can now use the application.")
    else:
        print("\n⚠️ Some systems have issues.")
        print("Please check the error messages above.")
    
    print("\nPress Enter to exit...")
    input()

if __name__ == "__main__":
    main()
