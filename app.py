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
teams = ['Team A', 'Team B', 'Team C', 'Team D']
team_mapping = {team: idx for idx, team in enumerate(teams)}

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
