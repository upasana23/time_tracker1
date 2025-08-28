#!/usr/bin/env python3
"""
Test Script for Routine Image Generation Functionality
Tests the chatbot's ability to generate and return JPG images of today's routine
"""

import requests
import json
import os
from datetime import datetime

def test_routine_image_generation():
    """Test the routine image generation functionality"""
    print("🧪 Testing Routine Image Generation...")
    
    # Test URLs
    ml_service_url = "http://localhost:8000"
    
    # Test queries that should trigger image generation
    routine_queries = [
        "What's my today's routine?",
        "Show me today's schedule",
        "What classes do I have today?",
        "Today's timetable",
        "My routine for today"
    ]
    
    successful_tests = 0
    total_tests = len(routine_queries)
    
    for i, query in enumerate(routine_queries, 1):
        print(f"\n📝 Test {i}/{total_tests}: '{query}'")
        
        try:
            # Make request to ML service
            response = requests.post(
                f"{ml_service_url}/api/chat",
                json={
                    "query": query,
                    "context": "timetable_attendance_system"
                },
                timeout=30
            )
            
            if response.status_code == 200:
                # Check if response is an image
                content_type = response.headers.get('content-type', '')
                
                if 'image' in content_type:
                    print(f"   ✅ SUCCESS: Image response received")
                    print(f"   📊 Content-Type: {content_type}")
                    print(f"   📏 Response Size: {len(response.content)} bytes")
                    
                    # Save the image for inspection
                    filename = f"routine_test_{i}_{datetime.now().strftime('%H%M%S')}.jpg"
                    with open(filename, 'wb') as f:
                        f.write(response.content)
                    print(f"   💾 Image saved as: {filename}")
                    
                    successful_tests += 1
                    
                else:
                    print(f"   ⚠️  WARNING: Expected image but got: {content_type}")
                    try:
                        json_response = response.json()
                        print(f"   📄 JSON Response: {json_response.get('response', 'No response field')[:100]}...")
                    except:
                        print(f"   📄 Raw Response: {response.text[:100]}...")
                        
            else:
                print(f"   ❌ FAILED: HTTP {response.status_code}")
                print(f"   📄 Error: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"   ❌ FAILED: Connection error - {str(e)}")
        except Exception as e:
            print(f"   ❌ FAILED: Unexpected error - {str(e)}")
    
    # Summary
    print(f"\n📊 Test Summary:")
    print(f"   Total Tests: {total_tests}")
    print(f"   ✅ Successful: {successful_tests}")
    print(f"   ❌ Failed: {total_tests - successful_tests}")
    print(f"   Success Rate: {(successful_tests/total_tests*100):.1f}%")
    
    if successful_tests == total_tests:
        print(f"\n🎉 ALL TESTS PASSED! Routine image generation is working perfectly!")
    elif successful_tests > 0:
        print(f"\n⚠️  PARTIAL SUCCESS: Some tests passed, but there are issues to investigate.")
    else:
        print(f"\n❌ ALL TESTS FAILED: Routine image generation is not working.")
    
    return successful_tests == total_tests

def test_non_routine_queries():
    """Test that non-routine queries still return text responses"""
    print(f"\n🧪 Testing Non-Routine Queries...")
    
    ml_service_url = "http://localhost:8000"
    
    # Test queries that should NOT trigger image generation
    non_routine_queries = [
        "What is the attendance rate?",
        "How many students are enrolled?",
        "Show me the risk analysis",
        "What are the ML model metrics?"
    ]
    
    successful_tests = 0
    total_tests = len(non_routine_queries)
    
    for i, query in enumerate(non_routine_queries, 1):
        print(f"\n📝 Test {i}/{total_tests}: '{query}'")
        
        try:
            response = requests.post(
                f"{ml_service_url}/api/chat",
                json={
                    "query": query,
                    "context": "timetable_attendance_system"
                },
                timeout=30
            )
            
            if response.status_code == 200:
                content_type = response.headers.get('content-type', '')
                
                if 'application/json' in content_type:
                    print(f"   ✅ SUCCESS: JSON response received")
                    json_response = response.json()
                    print(f"   📄 Response: {json_response.get('response', 'No response field')[:100]}...")
                    successful_tests += 1
                else:
                    print(f"   ⚠️  WARNING: Expected JSON but got: {content_type}")
                    
            else:
                print(f"   ❌ FAILED: HTTP {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ FAILED: Error - {str(e)}")
    
    print(f"\n📊 Non-Routine Test Summary:")
    print(f"   Total Tests: {total_tests}")
    print(f"   ✅ Successful: {successful_tests}")
    print(f"   Success Rate: {(successful_tests/total_tests*100):.1f}%")
    
    return successful_tests == total_tests

def main():
    print("🚀 Starting Routine Image Generation Tests...")
    print("This will test the chatbot's ability to generate JPG images for routine queries")
    print("Make sure the ML service is running on http://localhost:8000")
    
    try:
        # Test routine image generation
        routine_success = test_routine_image_generation()
        
        # Test non-routine queries
        non_routine_success = test_non_routine_queries()
        
        # Final summary
        print(f"\n" + "="*60)
        print("🎯 FINAL TEST RESULTS")
        print("="*60)
        print(f"✅ Routine Image Generation: {'PASSED' if routine_success else 'FAILED'}")
        print(f"✅ Non-Routine Text Responses: {'PASSED' if non_routine_success else 'FAILED'}")
        
        if routine_success and non_routine_success:
            print(f"\n🎉 ALL FUNCTIONALITY WORKING!")
            print(f"   • Routine queries return JPG images")
            print(f"   • Other queries return text responses")
            print(f"   • System is ready for production use!")
        else:
            print(f"\n⚠️  SOME ISSUES DETECTED")
            print(f"   Please check the test results above for details.")
            
    except KeyboardInterrupt:
        print(f"\n⚠️  Tests interrupted by user")
    except Exception as e:
        print(f"\n❌ Test failed with error: {str(e)}")

if __name__ == "__main__":
    main()

