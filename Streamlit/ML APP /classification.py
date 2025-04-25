import streamlit as st
import pandas as pd
import sklearn.datasets as load_ris
import sklearn.ensemble as RFC


def load():
    iris = load()
    df = pd.DataFrame(iris.data,columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names