import streamlit as st
import pandas as pd
import joblib

st.title("Houseprice prediction")

st.markdown("""
         This is a Machine Learning Model to predict houseprices
         based on various features.
         ### Modelmetric
         - **MAE (Mean Absolute Error)**: 18.725 $
         - **R²-Score**: 0,8""")

year_built = st.number_input("Year Built", min_value=1900, max_value=2025)
property_area = st.number_input("Property Area (ft²)", min_value=10, max_value=100000)
last_renovation = st.number_input("Last Renovation (year)", min_value=1900, max_value=2025)
living_area = st.number_input("Living Area without Basement (ft²)", min_value=10, max_value=100000)
basement_area = st.number_input("Basement Area (ft²)", min_value=10, max_value=100000)
beds = st.number_input("Number of Bedrooms", min_value=1, max_value=10)
kitchens = st.number_input("Number of Kitchens", min_value=1, max_value=5)
baths = st.number_input("Number of Bathrooms", min_value=1, max_value=5)
garage_capacity = st.number_input("Garage Capacity", min_value=0, max_value=10)

location = st.selectbox(
    "In which area is the building located?",
    options=["rich", "normal", "poor"]
)
quality = st.selectbox(
    "What condition is the building in?",
    options=["good", "medium", "bad"]
)
basement_available = st.selectbox(
    "Has the building a basement?",
    options=["yes", "no"]
)
air_conditioning_input = st.selectbox(
    "Has the building air conditioning?",
    options=["yes", "no"]
)
if air_conditioning_input == "yes":
    air_conditioning = "Y"
else:
    air_conditioning = "N"
    
input_data = pd.DataFrame({
    "Year Built": [year_built],
    "Property Area (ft²)": [property_area],
    "last Renovation (year)": [last_renovation],
    "Living Area without Basement (ft²)": [living_area],
    "Basement Area (ft²)": [basement_area],
    "Beds": [beds],
    "Kitchens": [kitchens],
    "Baths": [baths],
    "Garage Capacity": [garage_capacity],
    "Location": [location],
    "Quality": [quality],
    "Basement available": [basement_available],
    "Air Conditioning available": [air_conditioning]
})

@st.cache_resource
def load_model():
    return joblib.load("Housepricing_in_Ames_model.pkl")
model = load_model()

if st.button("Print prediction"):
    prediction = model.predict(input_data)
    st.success(f"estimated house price: {prediction[0]:,.2f} $")