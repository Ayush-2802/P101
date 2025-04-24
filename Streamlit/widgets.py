import streamlit as st
import pandas as pd 

st.title("Text Input")
name = st.text_input("Enter your name: ")

if name == "hehe":
    st.write("hehehehehhe :) ")
else:
    st.write("no hehe :(")

age = st.slider("Select age :",0,100,25)
st.write(age)

opt = ['python','cpp','java','javascript','rust']
choice = st.selectbox("Select language : ",opt)
st.write(choice)


#file uploader
file = st.file_uploader("Chose a csv file",type='csv')

if file is not None:
    f = pd.read_csv(file)
    st.write(f)