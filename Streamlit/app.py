import streamlit as st
import numpy as np
import pandas as pd 

# title
st.title("Hello Streamlit")
st.write("This is a simple text")

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[6,7,8,9]
})

st.write(df)

#line chart
ch = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(ch)