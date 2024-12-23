import streamlit as st
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

# Set page config
st.set_page_config(
    page_title="Premier League Predictor",
    page_icon="⚽",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #37003c;
        font-size: 3rem !important;
        padding-bottom: 2rem;
    }
    .stSelectbox label {
        color: #37003c;
        font-weight: 500;
    }
    .stButton button {
        background-color: #37003c;
        color: white;
        padding: 0.5rem 2rem;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Load the trained model
def load_model():
    mdl = "best_lr_model.pkl"
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

# App Layout
st.title("Premier League Match Predictor 🏆")
st.markdown("---")

# Create three columns for better layout
col1, col2, col3 = st.columns([1, 0.2, 1])

with col1:
    st.subheader("🏠 Home Team")
    home_team = st.selectbox("Select Home Team", teams_sorted, key="home")
    
    # Home team metrics in a card-like container
    with st.container():
        st.markdown("### Home Team Statistics")
        col1_1, col1_2 = st.columns(2)
        
        with col1_1:
            points_last_5_home = st.number_input("Last 5 Games Points", min_value=0, max_value=15, key="h1")
            points_home = st.number_input("Total Points", min_value=0, max_value=100, key="h2")
            games_played_home = st.number_input("Games Played", min_value=0, max_value=38, key="h3")
            
        with col1_2:
            wins_home = st.number_input("Wins", min_value=0, max_value=38, key="h4")
            losses_home = st.number_input("Losses", min_value=0, max_value=38, key="h5")
            draws_home = st.number_input("Draws", min_value=0, max_value=38, key="h6")
        
        st.markdown("#### Goal Statistics")
        col1_3, col1_4 = st.columns(2)
        with col1_3:
            goals_scored_last_5_home = st.number_input("Goals Scored (Last 5)", min_value=0, max_value=100, key="h7")
        with col1_4:
            goals_conceded_last_5_home = st.number_input("Goals Conceded (Last 5)", min_value=0, max_value=100, key="h8")

with col3:
    st.subheader("✈️ Away Team")
    away_team = st.selectbox("Select Away Team", teams_sorted, key="away")
    
    # Away team metrics in a card-like container
    with st.container():
        st.markdown("### Away Team Statistics")
        col3_1, col3_2 = st.columns(2)
        
        with col3_1:
            points_last_5_away = st.number_input("Last 5 Games Points", min_value=0, max_value=15, key="a1")
            points_away = st.number_input("Total Points", min_value=0, max_value=100, key="a2")
            games_played_away = st.number_input("Games Played", min_value=0, max_value=38, key="a3")
            
        with col3_2:
            wins_away = st.number_input("Wins", min_value=0, max_value=38, key="a4")
            losses_away = st.number_input("Losses", min_value=0, max_value=38, key="a5")
            draws_away = st.number_input("Draws", min_value=0, max_value=38, key="a6")
        
        st.markdown("#### Goal Statistics")
        col3_3, col3_4 = st.columns(2)
        with col3_3:
            goals_scored_last_5_away = st.number_input("Goals Scored (Last 5)", min_value=0, max_value=100, key="a7")
        with col3_4:
            goals_conceded_last_5_away = st.number_input("Goals Conceded (Last 5)", min_value=0, max_value=100, key="a8")

# Center the predict button
st.markdown("---")
col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
with col_btn2:
    predict_btn = st.button("🎯 Predict Match Outcome")

# Prediction logic
if predict_btn:
    if home_team != away_team:
        model = load_model()
        
        # Show a spinner while predicting
        with st.spinner('Analyzing match outcome...'):
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

            input_data = pd.DataFrame([features])
            prediction = model.predict(input_data)

            # Display the predicted result with styling
            result = "Home Win 🏠" if prediction == 1 else "Away Win ✈️" if prediction == 0 else "Draw 🤝"
            st.markdown("---")
            st.markdown(f"""
                <div style='text-align: center; background-color: #f0f2f6; padding: 2rem; border-radius: 10px;'>
                    <h2 style='color: #37003c;'>Predicted Outcome</h2>
                    <h1 style='color: #37003c; font-size: 3rem;'>{result}</h1>
                    <p style='color: #666;'>{home_team} vs {away_team}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.error("⚠️ Home team and away team cannot be the same!")

# Add footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Premier League Match Predictor | Made with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)
