import streamlit as st
import pandas as pd
import helper
@st.cache
def load_data():
    df=pd.read_csv('EDA_DATA.csv')
    df=df.dropna(subset=['Country'])
    return df
df=load_data()

#about data
st.title('About Data')
st.header('Data')
if st.checkbox('Show Data'):
    st.write(df)