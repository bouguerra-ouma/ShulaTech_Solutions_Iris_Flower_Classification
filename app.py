import streamlit as st

# Title and Description
st.title("Iris Flower Classification App")
st.write("""
This web app predicts the **Iris flower species** based on user input for:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width
""")

# Input Fields
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)

# Placeholder for Prediction Button
if st.button("Predict Species"):
    st.write("Prediction logic will be added here.")
