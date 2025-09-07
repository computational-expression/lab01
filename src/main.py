#!/usr/bin/env python3
"""
Digital Sensor Simulation Dashboard
CMPSC 100 Computational Expression - Lab 1

This program simulates collecting and analyzing sensor data like we'll do with the
Pico 2W next week! It demonstrates Week 2-3 concepts while introducing IoT vocabulary
and thinking patterns we'll use with real sensors.

Week 2 Concepts: Variables, data types, input/output, basic Python structure
Week 3 Concepts: Arithmetic operations, string operations, type conversion
Bridge to Week 4: IoT concepts, sensor terminology, data analysis thinking

Author: [Your Name]
Date: September 2025
"""

# =============================================================================
# WELCOME SECTION - Week 2: Basic print statements and program structure
# =============================================================================

# TODO: Create a welcome message for your Digital Sensor Simulation Dashboard
# Use print() statements with decorative characters or emoji
# This demonstrates basic output from Week 2 + introduces IoT concepts

print("🔬 DIGITAL SENSOR SIMULATION DASHBOARD 🔬")
print("==========================================")
print()
print("🤖 Welcome to IoT Sensor Simulation!")
print("This program simulates the sensor readings we'll collect with real hardware next week.")
print("Think like an IoT developer as you analyze your 'sensor data'!")
print()

# =============================================================================
# SENSOR DATA COLLECTION - Week 2: input() and Week 3: Type conversion
# =============================================================================

# TODO: Collect sensor setup and reading information from the user
# This simulates setting up an IoT device and taking sensor readings
# Demonstrates input() from Week 2 and type conversion from Week 3

# Device setup information (keep as strings - Week 2 data types)
device_name = ""  # TODO: Replace with input("Device Name (e.g., 'Alice's Room Monitor'): ")
location = ""     # TODO: Replace with input("Location being monitored (e.g., 'dorm room'): ")

# Monitoring duration (convert to integer - Week 3 type conversion)
duration_input = ""  # TODO: Replace with input("Monitoring duration in hours: ")
monitoring_hours = 0 # TODO: Convert duration_input to integer using int()

# Sensor readings (convert to appropriate types - Week 3 type conversion)
temp_input = ""     # TODO: Replace with input("Temperature sensor reading (°F): ")
temperature_f = 0   # TODO: Convert temp_input to integer using int()

light_input = ""    # TODO: Replace with input("Light level reading (0-1000 lux): ")
light_level = 0     # TODO: Convert light_input to integer using int()

moisture_input = "" # TODO: Replace with input("Soil moisture reading (0-100%): ")
moisture_percent = 0 # TODO: Convert moisture_input to integer using int()

motion_input = ""   # TODO: Replace with input("Motion detection count: ")
motion_count = 0    # TODO: Convert motion_input to integer using int()

print()  # Add blank line for spacing (Week 2: output formatting)

# =============================================================================
# SENSOR DATA PROCESSING - Week 3: Arithmetic operations for IoT analysis
# =============================================================================

# TODO: Process sensor data using arithmetic operations
# These calculations simulate real IoT data analysis we'll do with the Pico 2W

# Temperature analysis (Week 3: arithmetic operations + IoT conversion)
temperature_c = 0.0    # TODO: Calculate (temperature_f - 32) * 5 / 9 (F to C conversion)
hours_above_75 = 0     # TODO: Calculate monitoring_hours // 3 (simulate time above threshold)

# Light sensor analysis (Week 3: arithmetic with percentages)
daylight_percentage = 0  # TODO: Calculate (light_level / 600) * 100 (simulate daylight %)
avg_hourly_light = 0.0   # TODO: Calculate light_level / monitoring_hours

# Moisture sensor analysis (Week 3: arithmetic for plant care)
days_since_watering = 0  # TODO: Calculate monitoring_hours // 24 + 1
moisture_status_level = 0 # TODO: Calculate moisture_percent + 10 (buffer calculation)

# Motion sensor analysis (Week 3: rate calculations)
motion_per_hour = 0.0   # TODO: Calculate motion_count / monitoring_hours
peak_hour_detections = 0 # TODO: Calculate motion_count // 4 (simulate peak activity)

# =============================================================================
# IoT STATUS DETERMINATION - Week 3: String operations for device status
# =============================================================================

# TODO: Determine sensor statuses using Week 3 string operations
# This simulates how IoT devices determine and display operational status

# Temperature status (Week 3: string operations for IoT status)
temp_status = ""     # TODO: Set to "NORMAL" using string assignment
temp_status_upper = "" # TODO: Convert temp_status to uppercase using .upper()

# Light status (Week 3: string operations)
light_status = ""    # TODO: Set to "BRIGHT" if light_level > 400, else "DIM"

# Moisture status (Week 3: string concatenation)
moisture_status = "" # TODO: Set to "OPTIMAL" using string assignment
watering_needed = "" # TODO: Set to "NO" or "YES" based on your choice

# Device ID creation (Week 3: string slicing and concatenation like IoT device naming)
# Format: First letters of name + "_" + location + "_" + duration + "h"
device_initials = "" # TODO: Get first 3 characters of device_name using [0:3]
device_id = ""       # TODO: Create device_initials + "_" + location + "_" + str(monitoring_hours) + "h"

# =============================================================================
# IoT DASHBOARD OUTPUT - Week 2: print() and Week 3: string formatting
# =============================================================================

# TODO: Display the professional sensor monitoring dashboard
# This simulates real IoT device dashboard displays

print("==========================================")
# TODO: Create a personalized header using the device name (Week 3: string operations)
print("� [DEVICE NAME] - SENSOR DATA ANALYSIS")  # Replace [DEVICE NAME] with actual device_name
print("==========================================")
print()

# Temperature Sensor Section (Week 2: organized output, Week 3: displaying calculations)
print("🌡️ TEMPERATURE ANALYSIS:")
# TODO: Print temperature_f, temperature_c, temp_status_upper, hours_above_75
# Use string concatenation or f-strings (Week 3 concepts)
# Example: print("Temperature: " + str(temperature_f) + "°F")

print()

# Light Sensor Section (Week 3: displaying calculated sensor values)
print("� LIGHT SENSOR ANALYSIS:")
# TODO: Print light_level, light_status, daylight_percentage, avg_hourly_light

print()

# Moisture Sensor Section (Week 3: IoT plant monitoring display)
print("💧 MOISTURE SENSOR ANALYSIS:")
# TODO: Print moisture_percent, moisture_status, watering_needed, days_since_watering

print()

# Motion Sensor Section (Week 3: security/activity monitoring display)
print("� MOTION SENSOR ANALYSIS:")
# TODO: Print motion_count, motion_per_hour, peak_hour_detections

print()

# IoT Alerts and Recommendations (Week 3: smart device decision making)
print("� SENSOR ALERTS & RECOMMENDATIONS:")
# TODO: Print device_id, alert level, recommendations for next actions

print()

# Closing Section (Week 2: program conclusion + bridge to next week)
print("==========================================")
print("Thanks for using the Sensor Dashboard!")
print("Next week: We'll collect REAL sensor data with the Pico 2W! 🎛️")
print("Generated on September 7, 2025")
print("==========================================")

# =============================================================================
# BONUS IoT FEATURES (OPTIONAL) - Prepare for next week's hardware work
# =============================================================================

# TODO: Add your own creative sensor analysis or IoT features!
# Ideas that build on Week 2-3 concepts AND prepare for Pico 2W:
# - Additional sensor types (humidity, CO2, sound level)
# - More sophisticated threshold checking (Week 3: comparison operations)
# - Time-based analysis (Week 3: arithmetic with time)
# - Multi-room monitoring simulation (Week 2: variables, Week 3: calculations)
# - Energy efficiency calculations (Week 3: arithmetic for sustainability)
# - Predictive maintenance suggestions (Week 3: string formatting)

# Add your bonus IoT features here: