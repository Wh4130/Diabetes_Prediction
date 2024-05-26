import streamlit as st
import numpy as np 
import pandas as pd
import gzip, pickle, joblib
import sklearn
#----------------------------
# Header
#----------------------------
st.set_page_config(layout="wide")


st.write("""
    # Diabetes Prediction Machine Learning Project
    #### Please input your information to obtain the probability of having diabetes.
            """)
st.divider()


#----------------------------
# --- Sidebar
#----------------------------

with st.sidebar:
    st.write('''
    ## 🇹🇼 Huang Lin, Chun, Wally 🇯🇵
             ''')
    st.code(body = '''
    def Welcome_to_my_page(): 
        print("Nice to meet you")''', language='python')

    st.write(f'''

    A Taiwanese college student studying in Japan. Ambitious to become a data scientist.
    
    📍 NTU Economics | Waseda SPSE
    
    
    🔗 Visit my :orange[Github] https://github.com/Wh4130
            
    🔗 Visit my :green[Linkedin]: https://www.linkedin.com/in/chun-huang-lin-960552262

    ''')
    
    
#----------------------------
# --- Define columns
#----------------------------
col_11, col_12= st.columns((5,5))
with col_11:
    x1 = int(st.checkbox('Do you have High Blood Pressure?'))
    x2 = int(st.checkbox('Do you have High Cholesterol?'))
    x4 = int(st.checkbox('Do you smoke?'))
    
    x6 = int(st.checkbox('Do you have heart diseaseor attack?'))
    x7 = int(st.checkbox('Did you conduct any physical activity these past 30 days?'))
    
    
with col_12:
    x5 = int(st.checkbox('Have you ever got stroke?'))
    x8 = int(st.checkbox('Do you have fruits per day?'))
    x9 = int(st.checkbox('Do you have vegetable per day?'))
    x14 = int(st.checkbox("Check if you are biological male"))
    x13 = int(st.checkbox("Do you have serious difficulty walking or climbing stairs?"))


col_21, col_22, col_23 = st.columns((1/3, 1/3, 1/3))
with col_21:
    x12 = int(col_21.slider("How many days during the past 30 days was your physical health not good?", 0, 30))
with col_22:
    x11 = int(col_22.slider("How many days during the past 30 days was your mental health not good?", 0, 30))
with col_23:
    x10 = int(col_23.slider("Rate your General Health for the past 30 days (The higher the better)", 1, 5, value = 3))


x15 = int(st.slider("Select your age", 1, 100, value = 25))


col_31, col_32 = st.columns((5, 5))
with col_31:
    x = st.text_input("Please input your height in cm", value = 170)
with col_32:
    y = st.text_input("Please input your weight in kg", value = 50)

#----------------------------
# Transform inputs into values
# that would be fed into the model
#----------------------------
# Health Level
for health, mapped_health in zip([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]):
    if x10 == health:
        x10 = mapped_health
        break
# Age Scaling
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

# BMI Calculation
bmi = round(float(y) / (float(x)/100)**2, 2)
st.write(f'''Your :orange[BMI] is {bmi}''')

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

#----------------------------
# Define function for output
# and render the result
#----------------------------
def renderOutput():
     return round(predictProba([[x1, x2, bmi, x4, x5, x6, x7, x8, x9, x10, x11, x12,
                        x13, x14, x15]])[0], 5)
if st.button("Submit", type = 'primary'):
    result = renderOutput()
    output = "You are likely to have diabetes! Please take care of your health 🙌"
    if result < 0.5:
        output = "You don't have diabetes. Please keep your healthy life style 👏"
        
    st.write(f'''
        ### {output}
        ##### Probability of having Diabetes =  {result}
                ''')

st.button("Clear", type="secondary")

#----------------------------
# Final section
#----------------------------

st.divider()
st.write("""
            
    This is an interactive application of :orange[diabetes prediction] based on your life-style and health condition. 
            
    The application is build on :blue[***Gradient Boosting Decision Tree***] in sci-kit learn (sklearn) package for machine learning, based on 69891 instances and 15 features as training data. 
         
    For the detailed training procedure and the fulfill report, please visit this github repository.
         
    https://github.com/Wh4130/Diabetes_Prediction
    """)