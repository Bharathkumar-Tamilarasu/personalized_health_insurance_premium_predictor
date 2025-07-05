import streamlit as st
from utils import load_predict_page, load_artifacts, dict_to_dataframe, scale_features

def predictor():
    input_dict,ip_estimate = load_predict_page()
    if ip_estimate:
        if input_dict['Age'] > 25:
            artifacts = load_artifacts('rest')
        else: 
            artifacts = load_artifacts('young')
        # st.write(input_dict)
        # st.write(artifacts)
        feature_names = artifacts['model_data']['feature_names']
        trained_model = artifacts['model_data']['trained_model']
        scaler_object = artifacts['scaler_data']['scaler_object']
        scaled_columns = artifacts['scaler_data']['scaled_columns']
        input_df = dict_to_dataframe(input_dict,feature_names)
        scaled_input_df = scale_features(input_df,scaler_object,scaled_columns)
        predicted_value = trained_model.predict(scaled_input_df.iloc[[0]])

        st.success(f'Estimated Annual Premium: ₹ {int(predicted_value[0])}')
