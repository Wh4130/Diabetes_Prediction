# Diabetes Prediction Machine Learning Project

📌 See the slides for this ML project through:
1. ***diabetes_prediction_slides.pdf*** in this repository
2. this link:  https://drive.google.com/file/d/1N1FDC8_X5NVb7IlQOKq5wGQYHsGd48E7/view?usp=drive_link

### Streamlit Interactive Platform (Output) and my social media

📍 Test the probability of having diabetes: https://diabetesdetection-2e2nvdfhxvzucsbd3kvrfw.streamlit.app/

📍 Visit my Linked in: https://www.linkedin.com/in/chun-huang-lin-960552262

📍 Visit my instagram account for Japanese Education: @haruki_japanese_

### Motivation

Taiwanese people are proud of being the citizens of the country of "bubble tea". However, consequently, Taiwan is also one of few countries with highest rate of Diabetes. According to the government's report, diabetes patients account for 9% of total adults (18 - 64) in 2019, and this astonishingly high amount keeps increasing.

In light of this, I was inspired to establish a data analysis and machine learning project based on Diabetes survey data on Kaggle.com and build up an interactive user interface to make the public more aware of the risk and consequence of diabetes.

Via the interactive user interface built on Streamlit, user could input their age, height, weight, and their basic health condition and the model would return the probability of diagnosed as diabetes. 

🔗 link: https://diabetesdetection-2e2nvdfhxvzucsbd3kvrfw.streamlit.app/

### Work Flow and Summary

Basic classification machine learning prediction framework is adopted in this project. Detail information could be found in the following two files in this repository:

- ***1_machine_learning/eda_training_selection.ipynb***
  
- ***1_machine_learning/final_model.ipynb***

- ***streamlit_code/myapp.py***

The work flow of this project is as follow:

- Data and required modules import
  
- Data preprocessing (Outlier analysis)
  
- Exploratory Data Analysis & Feature Selection
  - EDA for binary features
  - EDA for non-binary features
  - Correlation Analysis
  - Feature Importance
  - Feature Selection
  
- Model Selection
  - Cross-Validation
  - Precision-Recall Curve Analysis
  - ROC Analysis

- Model Evaluation & Hyper Parameter Tuning

- Final Model Training & Model Output

- User Interface Establishment by Streamlit

### Reflections

- The possible reasons why the test score is not good:
  
  - features are represented as “level” → less precise (eg: age level instead of real age)
  
  - there are many skewed features → might exist selection bias
  
  - many features are based on subjective evaluation rather than objective clinical evidence (eg: General Health is based on  subjective opinions of health condition)

  - too many binary features

- Issues faced when I was trying to deploy my output:

  - Due to the lack of front-end and back-end knowledge, I did not know well about how to deploy and design the UI through HTML, CSS, and Javascript, and how to deploy the project to the internet.

  - Ensemble based models (Random Forest, GBDT) seem not compatible to the application deployment platform such as ***GCP***, ***Heroku***, and ***Streamlit***

- Questions that I started thinking after this project:

  - If there are multiple feature-selection methods and their outcomes differ, how should I select features for the final model.

  - Is it reasonable to perform feature normalization and scaling for binary features? (I did not agree with it so I did not perform)

  - If most of the features are not balanced, what should we do?

- Skillsets that I would start learning after this project:

  - Accumulate more knowledge though practical projects

  - Operation System

  - Git & Github

  - Streamlit
