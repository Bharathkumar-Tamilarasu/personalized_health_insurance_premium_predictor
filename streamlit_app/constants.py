# Options for streamlit app

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [ 'No Disease', 'Diabetes', 'High Blood Pressure', 'Thyroid', 
                        'Heart Disease', 'Diabetes & High Blood Pressure', 'Diabetes & Thyroid', 
                        'Diabetes & Heart Disease', 'High Blood Pressure & Heart Disease'],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Insurance Plan dictionary to map the values as per the input

insurance_plan_dict = {
    'Bronze' : 1,
    'Silver' : 2,
    'Gold' : 3,
}

# Risk Score Dictionary

risk_score_dict = {
    'heart disease' : 8,
'diabetes' : 6,
'high blood pressure' : 6,
'thyroid' : 5,
'no disease' : 0,
None : 0
}
