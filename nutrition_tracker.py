import pandas as pd

def track_nutrition(meal_plan):
    if meal_plan.empty:
        print("Meal plan is empty. Nutrition tracking aborted.")
        return {}

    # Calculate nutritional summaries
    total_calories = meal_plan['calories'].sum()
    average_calories = meal_plan['calories'].mean()

    # Create summary data
    nutrition_summary = {
        'Total Calories': total_calories,
        'Average Calories per Meal': average_calories
    }

    # Save nutritional summary to CSV file
    nutrition_summary_df = pd.DataFrame([nutrition_summary])
    nutrition_summary_df.to_csv('./data/nutritional_data.csv', index=False)

    return nutrition_summary_df
