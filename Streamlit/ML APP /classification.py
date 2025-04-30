import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load():
    iris = load_iris()
    df = pd.DataFrame(iris.data,columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df,target_name=load()

model = RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species'])

sepal_length = st.sidebar.slider(
    "Sepal length",
    float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max())
)
sepal_width = st.sidebar.slider(
    "Sepal width",
    float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max())
)
petal_length = st.sidebar.slider(
    "Petal length",
    float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max())
)
petal_width = st.sidebar.slider(
    "Petal width",
    float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max())
)

input = [[sepal_length, sepal_width, petal_length, petal_width]]

## prediction
prediction = model.predict(input)
predicted_species = target_name[prediction[0]]

st.write(prediction)
st.write(f'Predicted species is {predicted_species}')
