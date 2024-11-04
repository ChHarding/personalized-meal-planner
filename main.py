from flask import Flask, render_template, request
from meal_planner import generate_meal_plan
from nutrition_tracker import track_nutrition
from flask import Flask, render_template, redirect, request, session, url_for
from fitness_tracker import fitbit_auth, fetch_fitbit_data
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_meal_plan', methods=['POST'])
def generate_meal():
    dietary_preferences = request.form.get('dietary_preferences')
    health_goals = request.form.get('health_goals')

    meal_plan = generate_meal_plan(dietary_preferences, health_goals)
    if meal_plan.empty:
        return "Failed to generate a meal plan. Please try again."
   
    return render_template('meal_plan.html', meal_plan=meal_plan.to_dict(orient='records'))

@app.route('/nutrition_summary')
def nutrition_summary():
    try:
        meal_plan = pd.read_csv('./data/meal_plan.csv')  # Load the meal plan from the CSV file
        nutrition_summary = track_nutrition(meal_plan)
        return render_template('nutrition_summary.html', nutrition_summary=nutrition_summary.to_dict(orient='records')[0])
    except FileNotFoundError:
        return "Meal plan not found. Please generate a meal plan first."

if __name__ == "__main__":
    app.run(debug=True)

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Route to initiate Fitbit authentication
@app.route('/fitbit_auth')
def fitbit_auth_route():
    auth_url = fitbit_auth()
    return redirect(auth_url)

# Callback route for Fitbit OAuth2
@app.route('/callback')
def callback():
    fitbit = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    token = fitbit.fetch_token('https://api.fitbit.com/oauth2/token', 
                               client_secret=CLIENT_SECRET, 
                               authorization_response=request.url)
    session['fitbit_token'] = token['access_token']
    return redirect(url_for('fitbit_data'))

# Display Fitbit data
@app.route('/fitbit_data')
def fitbit_data():
    if 'fitbit_token' in session:
        data = fetch_fitbit_data(session['fitbit_token'])
        return render_template('fitbit_data.html', data=data)
    else:
        return redirect(url_for('fitbit_auth_route'))