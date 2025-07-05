# Personalized Health Insurance Premium Predictor

## **Introduction**

* In the health insurance industry, accurately predicting premiums is essential for both insurers and policyholders.
* This project, the **Personalized Health Insurance Premium Predictor**, uses machine learning and Python to predict health insurance premiums based on various individual characteristics such as age, gender, BMI, smoking status, dependents, region and medical history.. 
* By analyzing historical health insurance data, our model learns patterns that allow it to estimate personalized premiums for individuals. This tool can benefit both insurance companies in refining pricing strategies and policyholders in obtaining fair, personalized quotes.
* The system uses advanced algorithms to capture essential details about an individual’s health, lifestyle, and demographics, providing an accurate estimation of insurance premiums.

## **Objective** 

* The primary goal of this project is to build a **robust machine learning model** capable of predicting health insurance premiums based on individual health, demographic, and lifestyle factors.
* This system aims to provide personalized, data-driven premium estimates that promote fairness and transparency in health insurance pricing.

## **Data Collection**

The data for this project was collected from **Shield** health insurance providers to ensure comprehensive coverage of various demographics and health profiles.

## **About the Dataset**

### Dataset Information:
* The dataset provides in-depth information about individuals' health insurance policies, incorporating personal health details and premium data.
* Including a variety of risk profiles such as smokers, non-smokers, different age groups, regional variations, and various health conditions, the dataset offers insights into the diverse health insurance landscape.
* This dataset is valuable for understanding the broader insurance landscape and for building predictive models that offer personalized premium estimates.

### Attribute Information:
* **Age**: The age of the individual.
* **Gender**: The gender of the individual.
* **Region**: The geographic area where the individual resides (e.g., Northeast, Southwest).
* **Marital Status**: The individual's marital status (e.g., Married, Single).
* **Number of Dependents**: The number of dependents to be covered by the insurance policy.
* **BMI Category**: Body Mass Index (BMI) classification indicating body fat (e.g., Normal, Underweight, Overweight).
* **Smoking Status**: Frequency of smoking (e.g., Regular, Occasional, Non-Smoker).
* **Employment Status**: The individual's employment status (e.g., Self-Employed, Salaried).
* **Income Level**: The income level of the individual, categorized into ranges (e.g., ₹10L - ₹25L, ₹>40L).
* **Annual Income (in Lakhs)**: The individual's annual income in Lakhs.
* **Medical History**: Pre-existing medical conditions such as diabetes, hypertension, thyroid issues, etc.
* **Insurance Plan**: The type of insurance plan selected by the individual (e.g., Bronze, Gold, Platinum).
* **Annual Premium Amount**: The amount billed for health insurance, which is the target variable for prediction.


## **Libraries Used**

This project utilizes several powerful libraries and tools for data manipulation, machine learning, and visualization:

- **Pandas**: For data manipulation and analysis, handling datasets efficiently.
- **NumPy**: For numerical operations and efficient handling of arrays.
- **Scikit-Learn**: For building machine learning models, preprocessing, and evaluation.
- **Matplotlib** & **Seaborn**: For creating visualizations and performing exploratory data analysis (EDA).
- **XGBoost**: For advanced boosting techniques and optimization of machine learning models.
- **Statsmodels**: For statistical modeling and multicollinearity analysis.
- **Streamlit**: For creating interactive web applications to deploy machine learning models.
- **Streamlit Option Menu**: For adding navigation options to the Streamlit interface.

These libraries enable seamless data processing, visualization, model building, and deployment for the health insurance premium prediction project.

## Project Workflow

**1. Data Import & Exploration**
- Loaded the dataset and conducted an initial audit to understand data types, distributions, and missing values.
- Explored feature relationships and identified potential quality issues through visualizations and descriptive statistics.

**2. Data Preprocessing**
- Applied data cleaning techniques to enhance reliability:
- Imputed missing values using statistical and contextual methods
- Removed duplicate entries
- Standardized numeric formats and consistent encoding of categorical features
- Detected and treated outliers using IQR and z-score methods

**3. Exploratory Data Analysis (EDA)**
- Performed structured EDA to extract meaningful insights:
- **Univariate analysis** of individual features
- **Bivariate analysis** between features and the target variable
- Visual segmentation by region, age group, and other risk factors

**4. Feature Engineering & Selection**
- Created new variables based on domain knowledge (e.g., interaction terms, custom risk indicators)
- Encoded categorical features using one-hot or label encoding as appropriate
- Removed multicollinearity using Variance Inflation Factor (VIF)
- Selected the most relevant features using correlation analysis and predictive contribution

**5. Model Selection & Training**
- Built and evaluated multiple regression models:
- Linear Regression, Decision Trees, Random Forest, and XGBoost
- Tuned hyperparameters via cross-validation
- Assessed models using **MAE**, **RMSE**, and **R² score** for balanced evaluation

**6. Error Analysis**
- Analyzed prediction residuals to ensure robustness:
- Verified that 95% of predictions fall within ±10% of actual premium values
- Investigated underperforming segments for potential retraining or feature adjustments

**7. Final Prediction & Evaluation**
- Applied the final model to unseen test data
- Evaluated consistency and flagged anomalies for manual review
- Prepared model for deployment in both batch and real-time environments

## **Limitations**

* **Bias in Dataset**: The dataset may underrepresent certain demographic or socio-economic groups, which can reduce model accuracy and fairness for those segments.
* **Missing Health Data**: Absence of detailed medical history, pre-existing conditions, and lifestyle information (beyond smoking status) limits the model’s ability to assess true health risk.
* **Overweight on BMI**: Relying heavily on BMI may lead to misleading conclusions, as it doesn’t distinguish between fat and muscle mass or consider body composition.
* **Regional Assumptions**: Using only four broad regional categories may fail to reflect local healthcare cost differences and socio-economic diversity, impacting premium prediction accuracy.
* **Extreme Premium Values**: Presence of outliers in premium amounts can skew model training, leading to poorer generalization on more common or moderate cases.

## Conclusions

- Developed a complete ML pipeline to predict insurance premiums accurately using structured demographic and behavioral data.
- Identified key features influencing premium amounts — notably **age**, **genetical risk** and **income**.
- Final model delivered strong performance, with 95% of predictions within ±10% of actual premiums, meeting business targets.
- Insights from feature importance can assist underwriting teams in customer segmentation and risk assessment.
- The solution is scalable and modular, enabling easy retraining and seamless integration into production systems.

"""