import streamlit as st
import pandas as pd
import joblib

# Load the trained XGBoost model for predicting the mean well-being score
model = joblib.load('WellBeing_Mean_Score_model.pkl')

# Set up the page configuration
st.set_page_config(page_title="Sydney (New Group 47)", page_icon=":sparkles:", layout="centered")

# Streamlit App Title and Introduction
st.markdown("""
    <div style='background-color: #f0f8ff; padding: 10px; border-radius: 10px; margin-top: -30px;'>
        <h1 style='text-align: center; color: #333333;'>Sydney (New Group 47) - Well-Being Mean Score Predictor</h1>
        <p style='color: #666666; text-align: center;'>
            This application uses your screen time and demographic information to predict the average well-being score 
            based on the XGBoost model. Use the sidebar to enter your details. The screen time inputs should be in hours, and 
            the demographic inputs are binary values where:
        </p>
        <ul style='color: #666666;'>
            <li><strong>Gender:</strong> 1 = Male, 0 = Female</li>
            <li><strong>Minority Status:</strong> 1 = Minority, 0 = Majority</li>
            <li><strong>Deprived Area:</strong> 1 = Yes, 0 = No</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Sidebar Input Section
st.sidebar.header('🔧 Input Parameters')

def user_input_features():
    # Collect screen time inputs
    C_we = st.sidebar.slider('Computer Time (Weekend hours)', 0, 24, 2, help="Hours spent on computer during weekends")
    C_wk = st.sidebar.slider('Computer Time (Weekday hours)', 0, 24, 2, help="Hours spent on computer during weekdays")
    G_we = st.sidebar.slider('Gaming Time (Weekend hours)', 0, 24, 1, help="Hours spent on gaming during weekends")
    G_wk = st.sidebar.slider('Gaming Time (Weekday hours)', 0, 24, 1, help="Hours spent on gaming during weekdays")
    S_we = st.sidebar.slider('Smartphone Time (Weekend hours)', 0, 24, 3, help="Hours spent on smartphone during weekends")
    S_wk = st.sidebar.slider('Smartphone Time (Weekday hours)', 0, 24, 4, help="Hours spent on smartphone during weekdays")
    T_we = st.sidebar.slider('TV Time (Weekend hours)', 0, 24, 2, help="Hours spent watching TV during weekends")
    T_wk = st.sidebar.slider('TV Time (Weekday hours)', 0, 24, 2, help="Hours spent watching TV during weekdays")

    
    # Calculate additional features based on input
    total_screen_time_weekdays = C_wk + G_wk + S_wk + T_wk
    total_screen_time_weekends = C_we + G_we + S_we + T_we
    avg_screen_time = (total_screen_time_weekdays * 5 + total_screen_time_weekends * 2) / 7

    # Collect demographic inputs
    gender = st.sidebar.selectbox('Gender', (0, 1), format_func=lambda x: 'Male' if x == 1 else 'Female')
    minority = st.sidebar.selectbox('Minority Status', (0, 1), format_func=lambda x: 'Minority' if x == 1 else 'Majority')
    deprived = st.sidebar.selectbox('Deprived Area', (0, 1), format_func=lambda x: 'Yes' if x == 1 else 'No')
    
    # Create a DataFrame for model input with features in the expected order
    data = {
        'C_we': C_we, 'C_wk': C_wk, 'G_we': G_we, 'G_wk': G_wk,
        'S_we': S_we, 'S_wk': S_wk, 'T_we': T_we, 'T_wk': T_wk,
        'Total_Screen_Time_Weekdays': total_screen_time_weekdays,
        'Total_Screen_Time_Weekends': total_screen_time_weekends,
        'Avg_Screen_Time': avg_screen_time,
        'gender': gender, 'minority': minority, 'deprived': deprived,
    }
    
    # Arrange columns to match the expected order of the model
    column_order = ['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk',
                    'Total_Screen_Time_Weekdays', 'Total_Screen_Time_Weekends', 'Avg_Screen_Time','gender', 'minority', 'deprived', ]
    features = pd.DataFrame(data, index=[0])[column_order]
    return features

# Collect user input
input_df = user_input_features()

# Minimal spacing between sections
st.markdown("<br>", unsafe_allow_html=True)

# Display user input
st.subheader('User Input Summary')
st.write("""
    The parameters you have provided will be used to calculate the mean well-being score.
    Please review them below:
""")
st.dataframe(input_df)

# Minimal spacing before the prediction button
st.markdown("<br>", unsafe_allow_html=True)

# Perform prediction
if st.button('Predict Mean Well-Being Score'):
    try:
        prediction = model.predict(input_df)
        st.markdown(f"""
            <div style='background-color: #dff0d8; padding: 10px; border-radius: 10px; margin-top: 10px;'>
                <h3 style='color: #3c763d;'>Predicted Mean Well-Being Score</h3>
                <p style='font-size: 20px; color: #3c763d;'>The predicted mean well-being score is: <strong>{round(prediction[0], 2)}</strong></p>
            </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error in prediction: {e}")
