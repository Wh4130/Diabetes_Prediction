import streamlit as st
import numpy as np 
import pandas as pd
import gzip, pickle
import sklearn
#----------------------------
# Header
#----------------------------
st.set_page_config(layout="wide")
st.write("""
# Diabetes Prediction Machine Learning Project
        
This is an interactive application of pre-detecting diabetes based on your life-style and health condition. All input information would not be saved, so no need to worry about the privacy problem!
         
The application is build on Logistic Regression in sci-kit learn (sklearn) package for machine learning, based on 69891 instances and 15 features as training data. 
         
‼️ Note: during the model selection process, four models, including **Logistic Regression, Random Forest, Gradient Boosting Decision Tree, and Neural Network** were candidates. At the phase of model validation, Gradient Boosting Decision Tree performs the best, therefore selected as the final model. However, scikit-learn GBDT seems not compatiable with Streamlit, so Logistic Regression version was built for this user interface. As a result, the prediction result might not be as good as expected. (For example, if we increase only the days of Physical Health illness, the probability would go down, which is counterintuitive.)
         
#### Please input your information to obtain the probability of having diabetes.
""")


#----------------------------
# --- Define columns
#----------------------------
col1, col2, col3 = st.columns(3)


#----------------------------
# --- Define input boxes
#----------------------------

# Col1
x1 = int(col1.checkbox('Do you have High Blood Pressure?'))
x2 = int(col1.checkbox('Do you have High Cholesterol?'))
x4 = int(col1.checkbox('Do you smoke?'))
x5 = int(col1.checkbox('Have you ever got stroke?'))
x6 = int(col1.checkbox('Do you have heart diseaseor attack?'))
x7 = int(col1.checkbox('Did you conduct any physical activity these past 30 days?'))
x8 = int(col1.checkbox('Do you have fruits per day?'))
x9 = int(col1.checkbox('Do you have vegetable per day?'))
x13 = int(col1.checkbox("Do you have serious difficulty walking or climbing stairs?"))
x14 = int(col1.checkbox("Are you male or female? (Check if you are biological male)"))
x10 = int(col2.slider("Rate your General Health for the past 30 days", 1, 5, value = 3))


# Col2
for health, mapped_health in zip([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]):
    if x10 == health:
        x10 = mapped_health
        break
x11 = int(col2.slider("How many days during the past 30 days was your mental health not good?", 1, 30))
x12 = int(col2.slider("How many days during the past 30 days was your physical health not good?", 1, 30))
x15 = int(col2.slider("Select your age", 1, 100, value = 25))
def ageSlicing(real_age):
        age_list = [[0, 24], [25, 29], [30, 34], [35, 39], [40, 44], [45, 49],
                    [50, 54], [55, 59], [60, 64], [65, 69], [70, 74], [75, 79],
                    [80, 2000]]
        scaled_age = 0
        for scale, ages in enumerate(age_list):
            if (real_age >= ages[0]) and (real_age <= ages[1]):
                scaled_age = scale + 1
                break
        return scaled_age
x15 = ageSlicing(x15)

# Col3
x = col3.text_input("Please input your height in cm", value = 170)
y = col3.text_input("Please input your weight in kg", value = 50)

bmi = round(float(y) / (float(x)/100)**2, 2)

col3.write(f'''
Your BMI is {bmi}
         ''')

#----------------------------
# Load in trained model
#----------------------------
with gzip.open("./1_machine_learning/model.pgz", "rb") as f:
    clf = pickle.load(f)

#----------------------------
# Define Prediction Function
#----------------------------
def predictProba(input):
    prediction = clf.predict_proba(input)[:, 1]
    print(prediction)
    
    return prediction

result = round(predictProba([[x1, x2, bmi, x4, x5, x6, x7, x8, x9, x10, x11, x12,
                        x13, x14, x15]])[0], 5)
print(x11)

#----------------------------
# Render Results
#----------------------------
output = "You are likely to have diabetes 🫣 Please take care of your health 🙌"
if result < 0.5:
     output = "You might not have diabetes. Please keep your healthy life style 👏"
    
col3.write(f'''
### {output}
##### Probability of having Diabetes: {result}
         ''')
