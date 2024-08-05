import streamlit as st
import pandas as pd
import pickle

# Function to load the trained model
def load_model():
    with open('best_lr_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Function to encode teams (dummy implementation, replace with actual encoding logic)
def encode_team(team, team_mapping):
    return team_mapping.get(team, -1)

# Load the team names and mappings (replace with actual data and mappings)

teams = ['Coventry City' 'Southampton' 'Everton' 'Ipswich Town' 'Chelsea'
 'Crystal Palace' 'Sheffield Utd' 'Leeds United' 'Arsenal'
 "Nott'ham Forest" 'Manchester City' 'Blackburn' 'Wimbledon' 'QPR'
 'Sheffield Weds' 'Manchester Utd' 'Norwich City' 'Tottenham'
 'Oldham Athletic' 'Aston Villa' 'Liverpool' 'Middlesbrough' 'West Ham'
 'Newcastle Utd' 'Swindon Town' 'Leicester City' 'Bolton' 'Derby County'
 'Sunderland' 'Barnsley' 'Charlton Ath' 'Watford' 'Bradford City' 'Fulham'
 'West Brom' 'Birmingham City' 'Portsmouth' 'Wolves' 'Wigan Athletic'
 'Reading' 'Hull City' 'Stoke City' 'Burnley' 'Blackpool' 'Swansea City'
 'Cardiff City' 'Bournemouth' 'Brighton' 'Huddersfield' 'Brentford']
teams_mapping =  {
    'Coventry City': 0, 'Southampton': 1, 'Everton': 2, 'Ipswich Town': 3,
    'Chelsea': 4, 'Crystal Palace': 5, 'Sheffield Utd': 6, 'Leeds United': 7,
    'Arsenal': 8, "Nott'ham Forest": 9, 'Manchester City': 10, 'Blackburn': 11,
    'Wimbledon': 12, 'QPR': 13, 'Sheffield Weds': 14, 'Manchester Utd': 15,
    'Norwich City': 16, 'Tottenham': 17, 'Oldham Athletic': 18, 'Aston Villa': 19,
    'Liverpool': 20, 'Middlesbrough': 21, 'West Ham': 22, 'Newcastle Utd': 23,
    'Swindon Town': 24, 'Leicester City': 25, 'Bolton': 26, 'Derby County': 27,
    'Sunderland': 28, 'Barnsley': 29, 'Charlton Ath': 30, 'Watford': 31,
    'Bradford City': 32, 'Fulham': 33, 'West Brom': 34, 'Birmingham City': 35,
    'Portsmouth': 36, 'Wolves': 37, 'Wigan Athletic': 38, 'Reading': 39,
    'Hull City': 40, 'Stoke City': 41, 'Burnley': 42, 'Blackpool': 43,
    'Swansea City': 44, 'Cardiff City': 45, 'Bournemouth': 46, 'Brighton': 47,
    'Huddersfield': 48, 'Brentford': 49
}

# Streamlit App
st.title("Match Predictions App")

# User Input: Select teams
home_team = st.selectbox("Select Home Team", teams)
away_team = st.selectbox("Select Away Team", teams)

# Predict and Display Results
if st.button("Predict Outcome"):
    if home_team != away_team:
        model = load_model()

        # Encode the selected teams
        home_encoded = encode_team(home_team, team_mapping)
        away_encoded = encode_team(away_team, team_mapping)

        # Prepare input data for prediction
        input_data = pd.DataFrame([[home_encoded, away_encoded]], columns=['home_team', 'away_team'])

        # Prediction
        prediction = model.predict(input_data)

        # Display the predicted result
        result = "Home Win" if prediction == 1 else "Away Win" if prediction == 0 else "Draw"
        st.write(f"Predicted Outcome: {result}")
    else:
        st.write("Home team and away team cannot be the same.")
