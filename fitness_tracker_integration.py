import requests
from requests_oauthlib import OAuth2Session

# Fitbit API credentials (replace with your credentials)
CLIENT_ID = 'your_fitbit_client_id'
CLIENT_SECRET = 'your_fitbit_client_secret'
REDIRECT_URI = 'http://127.0.0.1:5000/callback'

# Fitbit OAuth2 authorization
def fitbit_auth():
    fitbit = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=['activity', 'nutrition'])
    authorization_url, state = fitbit.authorization_url('https://www.fitbit.com/oauth2/authorize')
    return authorization_url

# Fetch data from Fitbit API
def fetch_fitbit_data(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("https://api.fitbit.com/1/user/-/activities/date/today.json", headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None
