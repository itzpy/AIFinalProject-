import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Title of the app
st.title("Match Predictions App")

# Upload CSV file
uploaded_file = st.file_uploader("C:\\Users\\rayba\\Downloads\\premier-league-matches.csv", type="csv")
if uploaded_file is not None:
    # Load the data
    final_dataset = pd.read_csv(uploaded_file)
    st.write(final_dataset.head())
    
    # Show data information
    st.write("Data Information:")
    st.write(final_dataset.info())
    
    # Select features and target
    if st.checkbox("Select features and target"):
        features = st.multiselect("Select features", final_dataset.columns.tolist())
        target = st.selectbox("Select target variable", final_dataset.columns.tolist())

        # Split the data
        X = final_dataset[features]
        y = final_dataset[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a model
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        # Show model accuracy
        accuracy = model.score(X_test, y_test)
        st.write(f"Model Accuracy: {accuracy:.2f}")

# Visualizations
if st.checkbox("Show Visualizations"):
    st.subheader("Home Goals Distribution")
    sns.histplot(final_dataset['HomeGoals'], kde=True)
    st.pyplot(plt)

    st.subheader("Away Goals Distribution")
    sns.histplot(final_dataset['AwayGoals'], kde=True)
    st.pyplot(plt)