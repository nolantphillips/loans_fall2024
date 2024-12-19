import json
import streamlit as st
import requests

st.title('Loan Acceptance Prediction')
user_options = {}

streamlit_options = json.load(open('streamlit_options.json'))
for field_name, range in streamlit_options['slider_fields'].items():
    min_val, max_val = range
    current_value = round((min_val + max_val)/2)
    if field_name == 'PercentIncome':
        user_options[field_name] = st.sidebar.slider(field_name, float(min_val), float(max_val), value = float(current_value), step=0.05)
        continue
    user_options[field_name] = st.sidebar.slider(field_name, min_val, max_val, value = current_value)

for field_name, values in streamlit_options['single_select_fields'].items():
    user_options[field_name] = st.sidebar.selectbox(field_name, values)

user_options

if st.button('Predict'):
    data = json.dumps(user_options, indent=2)
    print(data)
    r = requests.post('http://127.0.0.1:8000/predict', data = data)
    st.write(r.json())