# 🩺 Diabetes Risk Prediction – Machine Learning & Streamlit App
This repository contains an end-to-end Machine Learning project designed to predict whether a patient is likely to have diabetes based on diagnostic health attributes.
The project includes Exploratory Data Analysis (EDA), Feature Engineering, Model Development, Evaluation, and Deployment using a Streamlit Web App.

## 📌 1. Project Overview
Diabetes is a fast-growing global health concern. Early detection can help prevent severe complications.
This project aims to build an ML-based prediction system that enables doctors and healthcare professionals to quickly assess diabetes risk using basic medical inputs.

The solution includes:
* Data Cleaning & Preprocessing
* EDA & Feature Insights
* Multiple ML model comparisons
* Final model: Random Forest Classifier
* Deployment using Streamlit
* A fully documented end-to-end workflow

## 📊 2. Dataset Information
The dataset contains 2768 patient records and the following features:
* <b> Pregnancies </b>	- Number of pregnancies
* <b> Glucose </b>	- Plasma glucose concentration
* <b> BloodPressure </b> -	Diastolic blood pressure
* <b> SkinThickness </b>	- Skin fold thickness
* <b> Insulin </b>	- 2-Hour serum insulin
* <b> BMI </b>	- Body Mass Index
* <b> DiabetesPedigreeFunction </b> - Genetic diabetes likelihood
* <b> Age </b>	- Age of the patient
* <b> Outcome </b>	- 1 = Diabetic, 0 = Non-diabetic

## 🔍 3. Exploratory Data Analysis (EDA)
Key steps included:

* Identification of missing & zero values
* Visualization of data distributions
* Outlier detection
* Correlation heatmap
* Pair-plots & feature importance
* Insights on which features impact diabetes risk most

EDA findings helped improve the quality and accuracy of the model.

## ⚙️ 4. Data Preprocessing
Steps performed:

✔ Replacement of medical-zero values with median values  
✔ Handling missing values  
✔ Normalization & scaling where required  
✔ Train-test split (80/20)  
✔ Class imbalance check  
✔ Outlier handling for Insulin, SkinThickness & BMI  

## 🤖 5. Machine Learning Models Used
The following models were trained and compared:

* Logistic Regression
* Decision Tree
* Random Forest (Selected Model)
* AdaBoost
* XGBoost

📈 Final Model Performance (Random Forest)
* Accuracy: ~92–96%
* High recall for diabetic patients
* Strong generalization
* Best balance of interpretability & performance

## 🖥️ 6. Streamlit Web App
The Streamlit application allows users to input patient health details and instantly receive:

✔ Diabetes prediction (Diabetic / Not Diabetic)  
✔ Probability of diabetes  

## 📂 7. Repository Structure
📁 diabetes-risk-prediction  
│── 📄 README.md  
│── 📄 Diabetes Risk Prediction App.py  
│── 📄 Final_RandomForest_Model.pkl  
│── 📄 requirements.txt  
│── 📄 Healthcare-Diabetes.csv  

## 🚀 8. Future Enhancements
Some potential upgrades:

* Hyperparameter tuning with RandomizedSearchCV / GridSearchCV
* SHAP-based explainability dashboard
* Cloud deployment (AWS / Azure / Streamlit Cloud)
* Larger dataset integration
* Database connectivity for storing prediction logs

## 👨‍💻 9. Author
<b><i>Naveen Gupta - Machine Learning & Data Science Enthusiast</i></b>  
📬 Feel free to reach out for collaborations or feedback!
