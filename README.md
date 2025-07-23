# House Price Prediction – Deployment Project

This repository contains a machine learning project focused on predicting house prices using regression models. The main goal was to deploy the best-performing model as a simple web app for user-friendly interaction.

---

## Project Overview

- **Task:** Regression (house price prediction)  
- **Dataset:** Ames Housing Dataset  
- **Language:** Python  
- **Libraries:** scikit-learn, pandas, NumPy, joblib, Streamlit  

---

## Models Evaluated

- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor (best performing)  

---

## Workflow

1. Data cleaning and preprocessing  
2. Model training and hyperparameter tuning using GridSearchCV  
3. Model serialization with joblib  
4. Deployment of the Random Forest model via a Streamlit app  

---

## Folder Structure

Housepricing Model/  
├── AmesHousing.csv  
├── datacleaninghousepricing.py  
├── decisiontree_pricing.py  
├── housepricing_main.py  
├── linear_regression_housepricing.py  
└── randomforest_housepricing.py  

Deployment Housepricing/  
├── __pycache__/  
├── AmesHousing.csv  
├── datacleaninghousepricing.py  
├── Deployment.py  
├── Housepricing_in_Ames_model.pkl  
└── housepricing_model.py  

requirements.txt  
README.md  
LICENSE  
.gitignore  

---

## Aim

This project marks the transition from model development to deployment. It demonstrates:  
- Building multiple regression models and selecting the best-performing one  
- Saving and loading models with joblib  
- Creating a simple web interface using Streamlit for end-user interaction  

---

## Live Demo

Test the web app online and interact with the model in real-time:  
[https://deployed-housepricing-model-g6avzurvxasca8owxtqrea.streamlit.app/](https://deployed-housepricing-model-g6avzurvxasca8owxtqrea.streamlit.app/)
