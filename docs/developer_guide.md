# **Developer's Guide for Personalized Meal Planning and Nutrition Tracker**

---

## **Overview**

The Personalized Meal Planning and Nutrition Tracker app combines meal planning, nutrition tracking, and fitness data integration. It allows users to generate personalized meal plans, track nutritional intake, and visualize Fitbit activity data on a unified dashboard.

---

## **Final Specifications**

### **Implemented Features**
1. **Meal Plan Generation**:
   - Uses Edamam API to create personalized meal plans based on user input.
2. **Nutrition Tracking**:
   - Tracks calories and macronutrients (protein, carbs, fats) stored in an SQLite database.
3. **Fitbit Integration**:
   - Connects to Fitbit for activity data (steps, calories burned).
4. **Unified Dashboard**:
   - Combines fitness and nutrition data with visualizations using Chart.js.
5. **Responsive Design**:
   - Mobile-friendly user interface.

---

## **Installation**

### **Dependencies**
- Python 3.8 or higher.
- Required Python libraries: Flask, Pandas, SQLite3, Requests.

### **Steps**
1. **Install dependencies**:

   pip install -r requirements.txt
2. **Set environment variables in a .env file**:
   CLIENT_ID=your_fitbit_client_id
CLIENT_SECRET=your_fitbit_client_secret
REDIRECT_URI=http://127.0.0.1:5000/callback
EDAMAM_APP_ID=your_edamam_app_id
EDAMAM_APP_KEY=your_edamam_app_key
 3. **Run the application**:
    python main.py




----


# Code Walkthrough

    "Core Files:"
    "1. main.py: Entry point for routing and rendering templates."
    "2. meal_planner.py: Interacts with Edamam API for meal plan generation."
    "3. nutrition_tracker.py: Processes meal plans to calculate nutritional summaries."
    "4. fitness_tracker_integration.py: Manages Fitbit authentication and data fetching."
    "User Flow:"
    "1. Home Page: Collects user input for dietary preferences and health goals."
    "2. Generate Meal Plan: Processes input and creates a personalized meal plan."
    "3. Dashboard: Displays combined activity and nutrition data."

 --------

# Known Issues

    "Minor:"
    "- Fitbit API rate limits can cause delays in data fetching."
    "Major:"
    "- SQLite database may not scale for a large user base."
    "- App currently does not support multiple user sessions."

------


# Future Work

    "1. Enhance Fitness Data: Add long-term trends for activity metrics."
    "2. Scalable Database: Transition from SQLite to PostgreSQL."
    "3. User Profiles: Implement user authentication and multi-user support."
    "4. Advanced Nutrition Insights: Add meal substitution options and dietary recommendations."

-----





