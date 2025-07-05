from typing import Tuple,Any
import streamlit as st
import joblib
import os
import pandas as pd
from constants import categorical_options,insurance_plan_dict,risk_score_dict

# Switching to the source directory

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../"))

def load_predict_page() -> Tuple[dict, bool]:

    # Define the page layout
    st.markdown("""##### Provide input for the prediction""")

    # Create four rows of three columns each
    row1 = st.columns(3)
    row2 = st.columns(3)
    row3 = st.columns(3)
    row4 = st.columns(3)

    # Assign inputs to the grid
    with row1[0]:
        ip_age = st.number_input('Age', min_value=18, step=1, max_value=100)
    with row1[1]:
        ip_number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
    with row1[2]:
        ip_income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)
    
    with row2[0]:
        ip_insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
    with row2[1]:
        ip_genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
    with row2[2]:
        ip_medical_history = st.selectbox('Medical History', categorical_options['Medical History'])
        
    
    with row3[0]:
        ip_gender = st.selectbox('Gender', categorical_options['Gender'])   
    with row3[1]:
        ip_region = st.selectbox('Region', categorical_options['Region']) 
    with row3[2]:
        ip_marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
        
    with row4[0]:
        ip_bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])
    with row4[1]:
        ip_smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
    with row4[2]:
        ip_employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])
    
    # Create a dictionary for input values
    input_dict = {
        'Age': ip_age,
        'Number of Dependants': ip_number_of_dependants,
        'Income in Lakhs': ip_income_lakhs,
        'Genetical Risk': ip_genetical_risk,
        'Insurance Plan': ip_insurance_plan,
        'Employment Status': ip_employment_status,
        'Gender': ip_gender,
        'Marital Status': ip_marital_status,
        'BMI Category': ip_bmi_category,
        'Smoking Status': ip_smoking_status,
        'Region': ip_region,
        'Medical History': ip_medical_history
    }

    ip_estimate = st.button(
        "Predict",
    )

    return input_dict,ip_estimate

def load_artifacts(model_name: str) -> object:

    # Define artifacts path

    artifact_folder = 'artifacts'
    artifact_name = 'insurance_premium_pipeline'
    artifact_extension = 'joblib'

    print('Project Root Path ->',project_root)

    # Construct the path to the artifact file
    artifacts_path = os.path.join(project_root, artifact_folder, f'{artifact_name}_{model_name}.{artifact_extension}')
    
    print('Artifacts Path->',artifacts_path)

    # Load artifacts and return them
    artifacts = joblib.load(artifacts_path)

    return artifacts

def dict_to_dataframe(input_dict: dict, feature_names : list) -> pd.DataFrame:

    # Create a DataFrame with 1 row all values initialized to 0
    df = pd.DataFrame(0, index=[0], columns=feature_names)
    df["age"] = input_dict["Age"]
    df["number_of_dependants"] = input_dict["Number of Dependants"]
    df["income_lakhs"] = input_dict["Income in Lakhs"]
    df["genetical_risk"] = input_dict["Genetical Risk"]
    df["insurance_plan"] = insurance_plan_dict[input_dict["Insurance Plan"]]
    print(input_dict["Medical History"])
    df["total_risk_score"] = get_risk_score(input_dict["Medical History"])
    
    if input_dict["Employment Status"] == "Salaried":
        df["employment_status_Salaried"] = 1
    if input_dict["Employment Status"] == "Self-Employed":
        df["employment_status_Self-Employed"] = 1
    
    if input_dict["Gender"] == "Male":
        df["gender_Male"] = 1
    
    if input_dict["Marital Status"] == "Unmarried":
        df["marital_status_Unmarried"] = 1

    if input_dict["BMI Category"] == "Obesity":
        df["bmi_category_Obesity"] = 1
    if input_dict["BMI Category"] == "Overweight":
        df["bmi_category_Overweight"] = 1
    if input_dict["BMI Category"] == "Underweight":
        df["bmi_category_Underweight"] = 1

    if input_dict["Smoking Status"] == "Occasional":
        df["smoking_status_Occasional"] = 1
    if input_dict["Smoking Status"] == "Regular":
        df["smoking_status_Regular"] = 1

    if input_dict["Region"] == "Northwest":
        df["region_Northwest"] = 1
    if input_dict["Region"] == "Southeast":
        df["region_Southeast"] = 1
    if input_dict["Region"] == "Southwest":
        df["region_Southwest"] = 1

    return df

def get_risk_score(medical_history : str) -> int:
    # Split the 'medical_history' column into 'disease1' and 'disease2' using '&' as the delimiter
    disease_list = medical_history.lower().split(' & ')
    score = 0
    for disease in disease_list:
        score += risk_score_dict[disease]

    return score

def scale_features(df: pd.DataFrame, scaler_object : object, scaled_columns : list) -> pd.DataFrame:
    df['income_level'] = None
    df[scaled_columns] = scaler_object.transform(df[scaled_columns])
    df.drop('income_level',axis=1,inplace=True)
    return df