from flask import Flask, render_template, request
from meal_planner import generate_meal_plan
from nutrition_tracker import track_nutrition
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
