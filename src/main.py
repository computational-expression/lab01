#!/usr/bin/env python3
"""
Digital Sensor Simulation Dashboard
CMPSC 100 Computational Expression - Lab 1

This program simulates sensor data collection and analysis like we'll do with the
Pico 2W this semester!

Author: Your Name
Date: September 2025
"""

# =============================================================================
# WELCOME SECTION - Basic print statements and program structure
# =============================================================================

# Create a welcome message for the Digital Sensor Simulation Dashboard
# Use print() statements with decorative characters or emoji
# This demonstrates basic output + introduces IoT concepts

print("🔬 DIGITAL SENSOR SIMULATION DASHBOARD 🔬")
print("==========================================")
print()
print("🤖 Welcome to IoT Sensor Simulation!")
print("This program simulates the sensor readings we'll collect with the Pico 2W this semester.")
print()

# =============================================================================
# SENSOR DATA COLLECTION - input() and Type conversion
# =============================================================================

# Collect sensor setup and reading information from the user
# This simulates setting up an IoT device and taking sensor readings
# Demonstrates input() and type conversion

print("📊 SIMULATED SENSOR SETUP")
print("==========================================")

# Device setup information (keep as strings - string data types)
device_name = ""        # TODO: Get device name from user using input()
location = ""           # TODO: Get location from user using input()

# Monitoring duration (convert to integer - type conversion)
duration_input = ""     # TODO: Get monitoring duration from user using input()
monitoring_hours = 0    # TODO: Convert duration_input to integer using int()

# Sensor readings (convert to appropriate types - type conversion)
temp_input = ""         # TODO: Get temperature reading from user using input()
temperature_f = 0       # TODO: Convert temp_input to integer using int()

light_input = ""        # TODO: Get light level from user using input()
light_level = 0         # TODO: Convert light_input to integer using int()

moisture_input = ""     # TODO: Get moisture reading from user using input()
moisture_percent = 0    # TODO: Convert moisture_input to integer using int()

motion_input = ""       # TODO: Get motion count from user using input()
motion_count = 0        # TODO: Convert motion_input to integer using int()

print()  # Add blank line for spacing (output formatting)

# =============================================================================
# SENSOR DATA PROCESSING - Arithmetic operations for IoT analysis
# =============================================================================

# TODO: Process sensor data using arithmetic operations
# These calculations simulate real IoT data analysis we'll do with the Pico 2W

# Temperature analysis (arithmetic operations + IoT conversion)
temperature_c = 0.0    # TODO: Calculate (temperature_f - 32) * 5 / 9 (F to C conversion)
# Example: round(22.666666, 1) becomes 22.7 - clean display for sensors
hours_above_75 = 0     # TODO: Calculate monitoring_hours // 3 (simulate time above threshold)

# Light sensor analysis (arithmetic with percentages)
daylight_percentage = 0  # TODO: Calculate (light_level / 600) * 100 (simulate daylight %)
avg_hourly_light = 0.0   # TODO: Calculate light_level / monitoring_hours

# Moisture sensor analysis (arithmetic for plant care)
days_since_watering = 0  # TODO: Calculate monitoring_hours // 24 + 1
moisture_status_level = 0 # TODO: Calculate moisture_percent + 10 (buffer calculation)

# Motion sensor analysis (rate calculations)
motion_per_hour = 0.0    # TODO: Calculate motion_count / monitoring_hours
peak_hour_detections = 0 # TODO: Calculate motion_count // 4 (simulate peak activity)

# =============================================================================
# IoT STATUS DETERMINATION - String operations for device status
# =============================================================================

# Determine sensor statuses using string operations
# This simulates how IoT devices determine and display operational status

# Temperature status (string operations for IoT status)
temp_status = ""     # TODO: Set to "NORMAL" using string assignment
temp_status_upper = "" # TODO: Convert temp_status to uppercase using .upper()
# Example: "normal".upper() becomes "NORMAL" - useful for professional displays

# Light status (string operations)
light_status = ""    # TODO: Set to "BRIGHT" using string assignment

# Moisture status (string concatenation)
moisture_status = "" # TODO: Set to "OPTIMAL" using string assignment
watering_needed = "" # TODO: Set to "NO" or "YES" based on your choice

# Device ID creation (string slicing and concatenation like IoT device naming)
# Format: First letters of name + "_" + location + "_" + duration + "h"
device_initials = "" # TODO: Get first 3 characters of device_name using [0:3]
device_id = ""       # TODO: Create device_initials + "_" + location + "_" + str(monitoring_hours) + "h"

# =============================================================================
# IoT DASHBOARD OUTPUT - print() and string formatting
# =============================================================================

# Display the professional sensor monitoring dashboard
# This simulates real IoT device dashboard displays

print("==========================================")
print("📊 " + device_name.upper() + " - SENSOR DATA ANALYSIS")
print("==========================================")
print()

# Temperature Sensor Section (organized output, displaying calculations)
print("🌡️ TEMPERATURE ANALYSIS:")
# TODO: Print temperature_f, temperature_c (rounded to 1 decimal), temp_status_upper, hours_above_75
print()

# Light Sensor Section (displaying calculated sensor values)
print("💡 LIGHT SENSOR ANALYSIS:")
# TODO: Print light_level, light_status, daylight_percentage (rounded), avg_hourly_light (rounded)
print()

# Moisture Sensor Section (IoT plant monitoring display)
print("💧 MOISTURE SENSOR ANALYSIS:")
# TODO: Print moisture_percent, moisture_status, watering_needed, days_since_watering
print()

# Motion Sensor Section (security/activity monitoring display)
print("🏃 MOTION SENSOR ANALYSIS:")
# TODO: Print motion_count, motion_per_hour (rounded), peak_hour_detections
print()

# IoT Alerts and Recommendations (smart device decision making)
print("🚨 SENSOR ALERTS & RECOMMENDATIONS:")
# TODO: Print alert level, status message, next check time, device_id
print()

# Closing Section (program conclusion + bridge to future work)
print("==========================================")
print("Thanks for using the Sensor Dashboard!")
print("This semester: We'll collect REAL sensor data with the Pico 2W! 🎛️")
print("Generated on September 7, 2025")
print("==========================================")

# =============================================================================
# BONUS IoT FEATURES (OPTIONAL) - Prepare for semester's hardware work
# =============================================================================

# Additional sensor analysis - Energy efficiency calculation
print()
print("⚡ BONUS: ENERGY EFFICIENCY ANALYSIS:")
# TODO: Calculate energy_rating using (light_level/10 + moisture_percent + (100 - motion_count*5)) / 3
# TODO: Print energy_rating (rounded) and efficiency_status

# Multi-room comparison simulation
print()
print("🏠 BONUS: ROOM OPTIMIZATION SUGGESTIONS:")
# TODO: Calculate total_score = temperature_f + light_level + moisture_percent
# TODO: Print total_score and recommendation message

# Add your bonus IoT features here: