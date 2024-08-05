import streamlit as st
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression




# Load the trained model
def load_model():
    mdl = "C:\\Users\\rayba\\Downloads\\best_lr_model.pkl"
    with open(mdl, 'rb') as file:
        model = pickle.load(file)
    return model
    

# Function to encode teams (dummy implementation, replace with actual encoding logic)
def encode_team(team, team_mapping):
    return team_mapping.get(team, -1)

# Load the team names and mappings
teams = ['Coventry City', 'Southampton', 'Everton', 'Ipswich Town', 'Chelsea',
         'Crystal Palace', 'Sheffield Utd', 'Leeds United', 'Arsenal',
         "Nott'ham Forest", 'Manchester City', 'Blackburn', 'Wimbledon', 'QPR',
         'Sheffield Weds', 'Manchester Utd', 'Norwich City', 'Tottenham',
         'Oldham Athletic', 'Aston Villa', 'Liverpool', 'Middlesbrough', 
         'West Ham', 'Newcastle Utd', 'Swindon Town', 'Leicester City', 'Bolton',
         'Derby County', 'Sunderland', 'Barnsley', 'Charlton Ath', 'Watford', 
         'Bradford City', 'Fulham', 'West Brom', 'Birmingham City', 'Portsmouth', 
         'Wolves', 'Wigan Athletic', 'Reading', 'Hull City', 'Stoke City', 'Burnley', 
         'Blackpool', 'Swansea City', 'Cardiff City', 'Bournemouth', 'Brighton', 
         'Huddersfield', 'Brentford']

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

teams_sorted = sorted(teams)

# Streamlit App
st.title("Match Predictions App")

# User Input: Select teams
home_team = st.selectbox("Select Home Team", teams_sorted)
away_team = st.selectbox("Select Away Team", teams_sorted)

points_last_5_home = st.number_input("Points gained in the last 5 games (Home)", min_value=0, max_value=15)
points_last_5_away = st.number_input("Points gained in the last 5 games (Away)", min_value=0, max_value=15)
points_home = st.number_input("Total points for Home Team", min_value=0, max_value=100)
points_away = st.number_input("Total points for Away Team", min_value=0, max_value=100)
games_played_home = st.number_input("Number of games played (Home)", min_value=0, max_value=38)
games_played_away = st.number_input("Number of games played (Away)", min_value=0, max_value=38)
wins_home = st.number_input("Wins (Home)", min_value=0, max_value=38)
losses_home = st.number_input("Losses (Home)", min_value=0, max_value=38)
draws_home = st.number_input("Draws (Home)", min_value=0, max_value=38)
wins_away = st.number_input("Wins (Away)", min_value=0, max_value=38)
losses_away = st.number_input("Losses (Away)", min_value=0, max_value=38)
draws_away = st.number_input("Draws (Away)", min_value=0, max_value=38)
goals_scored_last_5_home = st.number_input("Goals scored in last 5 games (Home)", min_value=0, max_value=100)
goals_conceded_last_5_home = st.number_input("Goals conceded in last 5 games (Home)", min_value=0, max_value=100)
goals_scored_last_5_away = st.number_input("Goals scored in last 5 games (Away)", min_value=0, max_value=100)
goals_conceded_last_5_away = st.number_input("Goals conceded in last 5 games (Away)", min_value=0, max_value=100)

# Predict and Display Results
if st.button("Predict Outcome"):
    if home_team != away_team:
        model = load_model()

        # Encode the selected teams
        home_encoded = encode_team(home_team, teams_mapping)
        away_encoded = encode_team(away_team, teams_mapping)

        features = {
            'diffFormPts': points_last_5_home - points_last_5_away,
            'home_team_formPts': points_last_5_home,
            'home_team_GDform': goals_scored_last_5_home - goals_conceded_last_5_home,
            'away_team_formPts': points_last_5_away,
            'away_team_draw_ratio': draws_away / (games_played_away if games_played_away > 0 else 1),
            'away_team_GDform': goals_scored_last_5_away - goals_conceded_last_5_away,
            'home_team_draw_ratio': draws_home / (games_played_home if games_played_home > 0 else 1),
            'diffPts': points_home - points_away,
            'away_team_loss_ratio': losses_away / (games_played_away if games_played_away > 0 else 1),
            'home_team_win_ratio': wins_home / (games_played_home if games_played_home > 0 else 1),
            'away_team_win_ratio': wins_away / (games_played_away if games_played_away > 0 else 1),
            'home_team_loss_ratio': losses_home / (games_played_home if games_played_home > 0 else 1),
            'away_team_avg_goals_conceded': goals_conceded_last_5_away / 5,
            'away_team_avg_goals_scored': goals_scored_last_5_away / 5,
            'home_team_avg_goals_scored': goals_scored_last_5_home / 5
        }

        # Prepare input data for prediction
        input_data = pd.DataFrame([features])

        # Prediction
        prediction = model.predict(input_data)

        # Display the predicted result
        result = "Home Win" if prediction == 1 else "Away Win" if prediction == 0 else "Draw"
        st.write(f"Predicted Outcome: {result}")
    else:
        st.write("Home team and away team cannot be the same.")
