# English Premier League Match Predictor

## Authors

This project is developed by AI Group 36. The members of this group are:
- Victor Ako-Adounvo
- Papa Yaw Badu

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Create Your Own Predictor App](#create-your-own-predictor-app)
- [Acknowledgements](#acknowledgements)

## Overview

The **English Premier League Match Predictor** is a project designed to predict the outcome of English football Premier League matches. The application predicts whether the Home or Away team is likely to win or if the game will end in a draw. The predictions are based on various features entered by the user, such as rolling averages and form points, which represent the points gained across the last 5 games for each team.

The project uses a dataset from Kaggle:
[Premier League Matches Dataset](https://www.kaggle.com/datasets/evangower/premier-league-matches-19922022?select=premier-league-matches.csv)

For a demonstration, you can watch the video here: [YouTube Link](https://youtu.be/SGYAfRdQ8xw)

You can also access the Colab notebook here: [Colab Link](https://colab.research.google.com/drive/1AxI6M3t5prdrhImI5FPA7VkGblpPqIiu?usp=sharing)

## Installation

### Prerequisites

Ensure the following packages are installed:
- `numpy`
- `pandas`
- `scikit-learn`
- `streamlit`
- `Python 3.5 or higher`

## Features

- **Match Outcome Prediction**: Predicts whether the Home or Away team will win, or if the match will end in a draw.
- **Feature Inputs**: Allows users to input various features such as team form points, total points, number of games played, wins, losses, drawn matches, and goals scored and conceded.
- **Rolling Averages Calculation**: Computes rolling averages to assess team performance over recent matches in the current season.
- **User-Friendly Interface**: Provides an interactive interface for easy data entry.

## Usage

### To Use the Application on a Cloud Server

1. Visit the deployed app: [Click Here](https://yhtevmflrdzz9wtdfdckmt.streamlit.app/)
2. Select the teams (Home and Away).
3. Fill in the values for the required features.
4. Press "Predict Outcome" to get your results.

### To Use the Application on a Local Server

1. Download the `best_lr_model.pkl` file.
2. Download the `app.py` file.
3. Install the required packages on your local machine.
4. Ensure the `.pkl` file is loaded from the correct directory.
5. Run the application with:
   ```bash
   streamlit run path/to/app.py
6. Then a link would be generated, and if it does not automatically launch on your browser click the link to open it.
7. Select the teams (Home and Away).
8. Fill in the values for the required features.
9. Press "Predict Oucome" to get your results.


   

## Create your own Predictor App
To create your own app:

1. Fork the repository.
2. Create a Streamlit account and link your GitHub account.
3. Go to [Streamlit Sharing](https://share.streamlit.io/) and click on "Create an app."
4. Select "Yes, I already have an app."
5. Paste the GitHub repository link where necessary.
6. Select the branch as `main`.
7. Set the main file path as `app.py`.

**Note:** The required packages will be downloaded automatically. After installation, clear the `requirements.txt` file if necessary.



## Acknowledgements

- Thanks to the Streamlit team for providing an easy-to-use framework.
- Special thanks to the scikit-learn team for their powerful machine learning tools.

