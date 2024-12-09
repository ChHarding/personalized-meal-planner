# Overview

    "The Personalized Meal Planning and Nutrition Tracker app combines meal planning, nutrition tracking, "
    "and fitness data integration. It allows users to generate personalized meal plans, track nutritional intake, "
    "and visualize Fitbit activity data on a unified dashboard."


# Final Specifications

    "Implemented Features:\n"
    "1. Meal Plan Generation: Uses Edamam API to create personalized meal plans based on user input.\n"
    "2. Nutrition Tracking: Tracks calories and macronutrients (protein, carbs, fats) stored in an SQLite database.\n"
    "3. Fitbit Integration: Connects to Fitbit for activity data (steps, calories burned).\n"
    "4. Unified Dashboard: Combines fitness and nutrition data with visualizations using Chart.js.\n"
    "5. Responsive Design: Mobile-friendly user interface."


# Installation

    "Dependencies:\n"
    "- Python 3.8 or higher.\n"
    "- Required Python libraries: Flask, Pandas, SQLite3, Requests.\n\n"
    "Steps:\n"
    "1. Install dependencies:\n"
    "   pip install -r requirements.txt\n\n"
    "2. Set environment variables in a .env file:\n"
    "   CLIENT_ID=your_fitbit_client_id\n"
    "   CLIENT_SECRET=your_fitbit_client_secret\n"
    "   REDIRECT_URI=http://127.0.0.1:5000/callback\n\n"
    "3. Run the application:\n"
    "   python main.py"


# Code Walkthrough

    "Core Files:\n"
    "1. main.py: Entry point for routing and rendering templates.\n"
    "2. meal_planner.py: Interacts with Edamam API for meal plan generation.\n"
    "3. nutrition_tracker.py: Processes meal plans to calculate nutritional summaries.\n"
    "4. fitness_tracker_integration.py: Manages Fitbit authentication and data fetching.\n\n"
    "User Flow:\n"
    "1. Home Page: Collects user input for dietary preferences and health goals.\n"
    "2. Generate Meal Plan: Processes input and creates a personalized meal plan.\n"
    "3. Dashboard: Displays combined activity and nutrition data."

# Known Issues

    "Minor:\n"
    "- Fitbit API rate limits can cause delays in data fetching.\n\n"
    "Major:\n"
    "- SQLite database may not scale for a large user base.\n"
    "- App currently does not support multiple user sessions.\n"


# Future Work

    "1. Enhance Fitness Data: Add long-term trends for activity metrics.\n"
    "2. Scalable Database: Transition from SQLite to PostgreSQL.\n"
    "3. User Profiles: Implement user authentication and multi-user support.\n"
    "4. Advanced Nutrition Insights: Add meal substitution options and dietary recommendations."





