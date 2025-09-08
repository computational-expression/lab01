# Lab 1: Digital Sensor Simulation Dashboard

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Discord](https://img.shields.io/discord/872320492936257537?logo=discord)](https://discord.gg/mfrngq3S)

## Introduction

Welcome to your first CMPSC 100 Lab! You will create a **Digital Sensor Simulation Dashboard** that introduces IoT concepts and vocabulary we will use with the Pico 2W starting next week, while practicing Python fundamentals.

## Learning Objectives

Practice **Python programming concepts** through IoT simulation:
- **Variables & Data Types**: Working with `int`, `float`, `str`, `bool` for sensor data
- **Arithmetic Operations**: Using +, -, *, /, //, %, ** for calculations  
- **String Operations**: Concatenation, formatting for dashboard display
- **Type Conversion**: Converting between data types for sensor input
- **Input/Output**: Creating interactive programs

*This assignment aligns with CMPSC 100 Learning Outcomes 1 and 2, focusing on Python programming fundamentals and industry-standard practices. It also introduces IoT concepts that prepare students for physical computing with the Pico 2W in upcoming labs.*

**� Note**: This lab uses two additional functions:
- `round(number, places)` - rounds decimals (e.g., `round(22.666, 1)` → `22.7`)
- `string.upper()` - converts to uppercase (e.g., `"normal".upper()` → `"NORMAL"`)

### Sample Output

Your program should create a concise sensor dashboard like this:

```
🔬 DIGITAL SENSOR SIMULATION DASHBOARD 🔬
==========================================

🤖 Welcome to IoT Sensor Simulation!
This program simulates the sensor readings we'll collect with real hardware next week.

📊 SIMULATED SENSOR SETUP
==========================================
Device Name: Jasmine's Room Monitor
Location: dorm room
Monitoring Duration (hours): 8
Temperature Sensor Reading: 72
Light Level Reading: 450
Soil Moisture Reading: 65
Motion Detected Count: 12

==========================================
� SENSOR DATA ANALYSIS
==========================================

🌡️ TEMPERATURE ANALYSIS:
Temperature: 72°F
Temperature in Celsius: 22.2°C
Status: NORMAL (within 68-78°F range)
Hours above 75°F: 2 hours

💡 LIGHT SENSOR ANALYSIS:
Light Level: 450 lux
Status: BRIGHT (above 400 lux threshold)
Percentage of daylight: 75%
Average hourly light: 56.25 lux/hour

💧 MOISTURE SENSOR ANALYSIS:
Soil Moisture: 65%
Status: OPTIMAL (50-70% range)
Watering needed: NO
Days since last watering: 2

🏃 MOTION SENSOR ANALYSIS:
Motion events: 12 detections
Average per hour: 1.5 detections/hour
Peak activity hour: Hour 7 (3 detections)
Room occupancy: ACTIVE

🚨 SENSOR ALERTS & RECOMMENDATIONS:
Alert Level: LOW
All sensors within normal ranges
Next check recommended: 4 hours
Device ID: ARM_dorm_8h_72

==========================================
Thanks for using the Sensor Dashboard!
Generated on September 7, 2025
==========================================
```

## Technical Requirements

Your program must include:

### Core Components
- **Welcome message** introducing the IoT sensor simulation
- **Five sensor inputs** (device name, location, temperature, light, moisture, motion)
- **Calculations** using arithmetic operations for sensor analysis
- **String operations** for device IDs, status messages, and formatting
- **Type conversions** between strings and numbers for sensor data
- **Formatted output** displaying a professional sensor dashboard

### Required Calculations
- **Temperature conversion**: `(fahrenheit - 32) * 5 / 9` (F to C)
- **Averages**: `total_reading / monitoring_hours`
- **Percentages**: `(current_value / max_value) * 100`
- **Status determination**: Compare readings to thresholds
- **Device ID creation**: String concatenation and slicing

### Code Quality Expectations
- **Descriptive variable names**: Use IoT-appropriate names like `temperature_f`, `device_status`
- **Clear comments**: Explain sensor thresholds and calculation logic
- **Professional formatting**: Organize code with proper spacing and sections
- **Be prepared to explain**: Your variable choices, calculations, and program logic during code review

## Getting Started

1. **Accept the GitHub Classroom assignment** and clone your repository
2. **Open `src/main.py`** and follow the TODO sections
3. **Test frequently** as you add each sensor section

```bash
cd src
python main.py
```

## Assessment Criteria - Total: 4.5 Points

### Technical Implementation (3.0 points)

**Grading is based on GatorGrade automated checks:**
- **33 automated checks = 3.0 points (100%)**
- **Partial credit:** Your score = (checks passed ÷ 33) × 3.0 points
- **Example:** 30/33 checks passed = (30÷33) × 3.0 = 2.73 points

*The automated checks verify all technical requirements including:*
- *Program execution without errors (includes file structure, syntax, runtime testing)*
- *Input collection (6 required inputs with proper prompts)*  
- *Calculations (arithmetic operations, temperature conversion, averages, status logic)*
- *Type conversion (string to int conversions, int to string for output)*
- *String operations (concatenation, slicing, method calls like .upper())*

### Code Quality and Style (1.0 point)  
- **Descriptive variable names** (0.3 pts)
- **Clean, readable code organization** (0.3 pts)
- **Appropriate comments** (0.4 pts)

### Reflection and Engagement (0.5 points)
- **Thoughtful reflection** on learning and IoT concepts

## Code Review (Separate Grading Component)

**This is a separate grading component: 2.2 points per code review. Not part of the 4.5-point lab grade. See the syllabus for more details.**

### Topics You May Need to Explain:
- **Variable types and naming conventions** for sensor data (Python programming concepts)
- **Arithmetic operations** used in sensor calculations like temperature conversion, averages, percentages (Python programming concepts) 
- **String operations** for device IDs, status messages, and dashboard formatting (Python programming concepts)
- **Type conversion** between strings and numbers for sensor data processing (Python programming concepts)
- **Program logic** and flow for IoT simulation and sensor analysis

## Submission Instructions

Submit to GitHub frequently! The version submitted last before the due date will be the one that is graded. 

### Git Workflow
```bash

# Add your completed files
git add src/main.py writing/reflection.md or git add .

# Commit with a descriptive message
git commit -m "Complete sensor simulation dashboard"

# Push to GitHub
git push
```

### Verification
- Go to your GitHub repository online
- Verify your files show your latest changes
- Check that GatorGrade passes (automated testing will run)

## Getting Help

### During Lab
- Ask TLs or instructor for help with specific questions or issues
- Work with classmates on understanding concepts (but write your own code)
- Use the lab time to understand the requirements and get started with your program

### Outside Lab  
- Post questions in Discord
- Attend 
- Attend [TL office hours](https://www.cis.allegheny.edu/teaching/technicalleaders/) and/or [instructor office hours](https://janyljumadinova.com/schedule/) to seek help outside of class
- Review the Python programming slides for concept reinforcement

### Resources
- [Python Documentation](https://docs.python.org/3/)
- Course slides: [Python Basics](https://computational-expression.github.io/course_information/week02/python_basics.html), [Types & Operations](https://computational-expression.github.io/course_information/week03/types_operations.html)
- Examples from class activities
