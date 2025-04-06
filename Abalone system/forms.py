import streamlit as st
import requests

st.title("Abalone ring count prediction")

st.write("### Provide feature data")


sex = st.selectbox("Sex", options=["Male", "Female", "Infant"], index=0)


length = st.slider(
    "Length (mm)",
    min_value=0.100,
    max_value=1.000,
    value=0.550,  
    step=0.001
)

diameter = st.slider(
    "Diameter (mm)",
    min_value=0.055,
    max_value=1.000,
    value=0.425,  
    step=0.001
)

height = st.slider(
    "Height (mm)",
    min_value=0.000,
    max_value=1.500,
    value=0.140,  
    step=0.001
)

whole_weight = st.slider(
    "Whole Weight (g)",
    min_value=0.002,
    max_value=3.000,
    value=0.8000,  
    step=0.001
)

whole_weight_1 = st.slider(
    "Whole Weight 1 - Shucked weight (g)",
    min_value=0.001,
    max_value=1.500,
    value=0.300,  
    step=0.001
)

whole_weight_2 = st.slider(
    "Whole Weight 2 - Viscera weight (g)",
    min_value=0.001,
    max_value=1.000,
    value=0.400,  
    step=0.001
)

shell_weight = st.slider(
    "Shell Weight (g)",
    min_value=0.002,
    max_value=1.000,
    value=0.250,  
    step=0.001
)

# encoding 'sex' category
sex_encoded = 1 if sex == "Male" else 2 if sex == "Female" else 0

if st.button("Predict Ring Count"):
    # Prepare - data payload
    data = {
        'sex': sex_encoded,
        'length': length,
        'diameter': diameter,
        'height': height,
        'whole_weight': whole_weight,
        'whole_weight_1': whole_weight_1,
        'whole_weight_2': whole_weight_2,
        'shell_weight': shell_weight
    }

    # Sening input data to backend
    response = requests.post('http://127.0.0.1:5000/predict', json=data)
    result = response.json()

    # Display prediction
    st.write(f"### Predicted Ring Count: {result['prediction']}")
