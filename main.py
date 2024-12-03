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
    
    # Determine the success message based on the outcome
    if not meal_plan.empty:
        success_message = "Meal plan generated successfully!"
    else:
        success_message = "Failed to generate a meal plan. Please try again."

    # Render the home page with the success message
    return render_template('index.html', success_message=success_message)
   


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
    try:
        auth_url = fitbit_auth()
        success_message = "Fitbit authentication initiated. Please complete the authorization process."
    except Exception as e:
        success_message = f"Failed to connect Fitbit: {str(e)}"
    
    return render_template('index.html', success_message=success_message)
   

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
    
    @app.route('/dashboard')
def dashboard():
    # Fetch Fitbit data
    fitbit_data = None
    if 'fitbit_token' in session:
        try:
            fitbit_data = fetch_fitbit_data(session['fitbit_token'])
        except Exception as e:
            fitbit_data = {"error": f"Failed to fetch Fitbit data: {e}"}


    # Fetch nutrition data from SQLite
    conn = sqlite3.connect('meal_planner.db')
    cursor = conn.cursor()
    cursor.execute('SELECT total_calories, avg_calories, protein, carbs, fats FROM nutrition_tracking WHERE user_id = 1')  # Replace 1 with dynamic user ID
    row = cursor.fetchone()
    conn.close()

    nutrition_data = None
    if row:
        nutrition_data = {
            'total_calories': row[0],
            'avg_calories': row[1],
            'protein': row[2],
            'carbs': row[3],
            'fats': row[4],
        }

    return render_template('dashboard.html', fitbit_data=fitbit_data, nutrition_data=nutrition_data)
