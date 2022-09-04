import pandas as pd
import streamlit as st
import joblib
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../models/model.pkl')
model = joblib.load(filename)

#########################
#       Front Page      #
#########################
st.markdown('<style>description{color:blue;}</style>', unsafe_allow_html=True)
st.title('Titanic survival prediction')
st.markdown("<description> The sinking of the Titanic is one of the most infamous shipwrecks in history. " + 
"While there was some element of luck involved in surviving, it seems some" +
" groups of people were more likely to survive than others. Find out if you would have sourvived. </description>", unsafe_allow_html=True)
#######################
#       Side Bar      #
#######################
st.sidebar.title('Select the parameters to analyze survival prediction')
image = os.path.join(dirname, '../assets/RMS_Titanic_3.jpg')
st.image(image, caption = "RMS Titanic departing Southampton on April 10, 1912. Photographer Francis Godolphin Osbourne Stuart (1843-1923) wikidata:Q5481096", use_column_width=True)
Age = st.sidebar.slider("Enter your Age", 1, 65, 30)
Fare = st.sidebar.slider("Fare (in 1992)", 1, 66, 32)
relatives = st.sidebar.selectbox("How many relatives are traveling with you?", range(0,6))
gender = st.sidebar.radio("Select your Gender:",['Female', 'Male'])
if gender == 'Male':
    Sex = 0
else:
    Sex = 1 
Pclass = st.sidebar.selectbox("Select your passenger class:",[1, 2, 3])
emb = st.sidebar.radio("Select your boarded location:",['Cherbourg', 'Queenstown', 'Southhampton'])
if emb == 'Cherbourg':
    Embarked = 1
elif emb == 'Queenstown':
    Embarked = 2
else:
    Embarked = 0

#########################
#       Predictions     #
#########################
if st.sidebar.button("Predict"):
    result = model.predict([[Pclass, Sex, Age, Fare, Embarked, relatives]])
    if result[0] == 1:
        st.success("You probably would have survived!")
    else:
        st.error("You probably would have not survived!")


