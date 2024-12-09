# **Personalized Meal Planning and Nutrition Tracker**

## **Overview**

The **Personalized Meal Planning and Nutrition Tracker** app helps users generate meal plans, track nutrition, and integrate fitness data from Fitbit. With a user-friendly interface and comprehensive health insights, the app makes managing health goals simple and effective.

---

## **Installation and Setup**

### **Requirements**
- Python 3.8 or higher
- Internet connection (for API calls)

### **Dependencies**
Install required libraries:

pip install -r requirements.txt

### **Setup Steps**
Clone the Repository:


git clone https://github.com/Mayuri9808/personalized-meal-planner.git
cd personalized-meal-planner
Set Up API Keys:

Obtain API keys:
Edamam API for meal plan generation: Edamam API
Fitbit API for activity data: Fitbit API
Create a .env file in the root directory:

CLIENT_ID=your_fitbit_client_id
CLIENT_SECRET=your_fitbit_client_secret
REDIRECT_URI=http://127.0.0.1:5000/callback
EDAMAM_APP_ID=your_edamam_app_id
EDAMAM_APP_KEY=your_edamam_app_key
Run the Application: Start the Flask application:


python main.py
Open your browser and navigate to http://127.0.0.1:5000.

Using the App
Step 1: Home Page
Navigate to the home page (http://127.0.0.1:5000).
Enter your dietary preferences and health goals, then click Generate Meal Plan.

Step 2: View Meal Plan
Once generated, the app will provide a meal plan.
Click on Nutrition Summary to view the nutritional breakdown.

Step 3: Fitbit Integration
Click on Connect Fitbit to link your Fitbit account.
After successful authentication, navigate to the Dashboard to view your fitness and nutrition data.

Step 4: Dashboard
The dashboard displays:
Fitbit activity metrics (steps, calories burned).
Nutritional insights (macronutrient breakdown, total calories).

### **Common Errors and Fixes**

1. Meal Plan Not Found
Error: "Meal plan not found. Please generate a meal plan first."
Fix: Navigate to the home page and generate a meal plan.
2. Fitbit Authentication Failure
Error: "Failed to connect Fitbit."
Fix: Ensure your API keys are correct in the .env file.
3. Slow API Response
Cause: API rate limits or slow network.
Fix: Try again after some time.

### **Caveats and Limitations**

Multi-User Support:
The app currently does not support multiple user sessions.
Scalability:
The SQLite database may not handle a large number of users.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any changes.

### **License**

This project is licensed under the MIT License. See the LICENSE file for details.



