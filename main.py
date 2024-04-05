import streamlit as st
import pandas as pd
import numpy as np

# Title and Description
st.title('BWH Egg Freezing Counseling Tool')
st.write('This tool helps you understand your options for egg freezing based on your personal health information and age. It\'s designed to empower you with information for planning your reproductive future.')

# User Input
st.header('Your Information')
age = st.slider('What is your age?', 18, 45, 30)
smoker = st.radio('Do you smoke?', ('Yes', 'No'))
history_of_ovarian_issues = st.radio('Do you have a history of ovarian issues?', ('Yes', 'No'))

# Basic advice model (Placeholder for a more complex model)
st.header('Your Egg Freezing Advice')
if age <= 35 and history_of_ovarian_issues == 'No':
    advice = 'Your age and health history suggest you are in a good position to consider egg freezing. Discussing further with a healthcare professional is advised.'
elif age > 35 and history_of_ovarian_issues == 'No':
    advice = 'Considering egg freezing sooner rather than later is recommended due to age-related declines in fertility.'
else:
    advice = 'Given the provided information, a detailed discussion with a fertility specialist is highly recommended to understand your options.'

st.write(advice)

# Disclaimer
st.write('**Disclaimer:** This app is for informational purposes only and does not substitute for professional medical advice, diagnosis, or treatment.')

