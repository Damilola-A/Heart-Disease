import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import joblib
import streamlit as st


# load the Model
model = joblib.load(open('LinReg.pkl', 'rb'))




st.title('HEART RATE MONITOR')
st.subheader('Built By Gomycode Scions')



st.image('pngwing.com(7).png', width= 250)




st.write('please register your name for record of usage')
username = st.text_input('Enter your name')
if st.button('submit your name'):
   st.success(f"Welcome {username}. please use according to usage guidelines")


st.sidebar.image('pngwing.com(5).png', caption = username, use_column_width= True) 

input_type = st.sidebar.selectbox('Choose your preffered input type',['Number Input', 'slider'])


if input_type == 'Number Input':
   biking = st.sidebar.number_input('Biking', 1.1, 75.0, 38.0)
   smoking = st.sidebar.number_input('Smoking', 0.5, 30.0, 15.4)
else:
   biking = st.sidebar.slider('Biking', 1.1, 75.0, 38.0)
   smoling = st.sidebar.slider('Smoking', 0.5, 30.0, 15.4)

# Aggregate the input values for our test

input_values = [[biking, smoking]]
frame = ({'biking': [biking],'smoking': [smoking]})

st.markdown('<hr>', unsafe_allow_html= True)
st.write('These are your input variables')
frame = pd.DataFrame(frame)
frame= frame.rename(index= {0: 'Value'})
frame =frame.transpose()
st.write(frame)


# Testing the model

prediction = model.predict(input_values)


