Here's the updated README file, including information about the pickle file and `requirements.txt` file:

---

# Well-Being Score Prediction Project

## Overview

This project aims to build a predictive model that estimates well-being scores based on screen time data and demographic information collected from a cohort of adolescents. We explore various machine learning models, including Linear Regression and XGBoost, and deploy the best-performing model through a user-friendly Streamlit application for real-time predictions.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Model Evaluation](#model-evaluation)
- [Contributors](#contributors)

## Project Structure

The repository contains the following files and directories:
```
├── WellBeing_Mean_Score_model.pkl
├── well-being-score_prediction.ipynb
│   ├── wellbeing_streamlit_app.py
├── requirements.txt
├── README.md
```
- **data/**: Contains all the datasets used in the project.
- **WellBeing_Mean_Score_model.pkl**: Contains the trained model saved as a pickle file for deployment.
- **well-being-score_prediction.ipynb**: Jupyter notebooks used for data analysis and model training.
- **wellbeing_streamlit_app.py**: Contains the Streamlit application script.
- **requirements.txt**: List of required Python packages.
- **README.md**: This file, which contains information about the project.

## Features

- **Data Analysis**: Exploratory Data Analysis (EDA) using Pandas and Matplotlib.
- **Model Development**: Training and testing of different models (Linear Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost).
- **Model Evaluation**: Evaluating models using Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared values.
- **Streamlit App**: A user-friendly interface for real-time well-being score predictions based on user input.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/well-being-score-prediction.git
   ```

2. Navigate to the project directory:
   ```bash
   cd well-being-score-prediction
   ```

3. Install the required Python packages using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:
   ```bash
   streamlit run scripts/wellbeing_streamlit_app.py
   ```

> Note: Ensure you have Python 3.7+ installed in your environment.

## Usage

- **Jupyter Notebook**: Explore the `notebooks/well-being-score_prediction.ipynb` file to see the data analysis, model training, and evaluation steps.
- **Streamlit Application**: Input your screen time and demographic details through the app to receive a predicted well-being score. The application dynamically calculates the results based on your input values.
- **Pickle File**: The trained model (`WellBeing_Mean_Score_model.pkl`) is stored in the `models/` directory and is loaded in the Streamlit application to provide predictions.

## Technologies Used

- **Python**: Programming language used for analysis and modeling.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For data visualization.
- **Scikit-learn**: For model development and evaluation.
- **XGBoost**: For building advanced gradient boosting models.
- **Streamlit**: For developing an interactive web application.

## Model Evaluation

The following models were evaluated based on Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared values:

| Model                | Mean CV R-squared | Test R-squared | MAE       | MSE       |
|---------------------|------------------|---------------|-----------|-----------|
| Linear Regression    | 0.011901         | 0.088653      | 0.510548  | 0.420212  |
| Decision Tree        | -1.179938        | -0.828633     | 0.724027  | 0.843162  |
| Random Forest        | -0.080622        | -0.040031     | 0.545453  | 0.479547  |
| Gradient Boosting    | 0.036934         | 0.102705      | 0.506324  | 0.413732  |
| XGBoost              | 0.037385         | 0.102771      | 0.506328  | 0.413702  |

Based on these results, **XGBoost** was chosen as the best-performing model for this project.

## Contributors

- **Angshu Bikash Mandal** - Lead Developer
- **Md Ahanaf Uz Zaman** - Data Analyst
- **Tasin Al Nahian Khan** - Visualization Specialist
- **Sadman Saki Shohan** - Application Developer
- **Koushik Sarker** - Report Writer
