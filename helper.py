import pandas as pd
import streamlit as st
import plotly.express as px
#load data
@st.cache
def load_data():
    df=pd.read_csv('EDA_DATA.csv')
    df=df.dropna(subset=['Country'])
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    return df
df=load_data()
def countryplot(countries):
    if countries!='All Countries':
        data=df[(df['Country'].isin(countries))]
    else:
        data=df
    mean_country = data.groupby('Country')['Salary'].mean().reset_index()
    fig = px.bar(mean_country, x='Country', y='Salary', color='Country') 
    return fig
def expyplot(countries):
    if countries!='All Countries':
        data=df[(df['Country'].isin(countries))]
    else:
        data=df
    #mean_exp = data.groupby('Experience')['Salary'].mean().reset_index()
    #fig = px.bar(mean_exp, x='Experience', y='Salary', color='Country') 
    #aggregated_data = data.groupby(['YearsExperience', 'Country'])['Salary'].mean().reset_index()
    fig = px.bar(data, x='YearsExperience', y='Salary', color='Country')
    return fig
def Ageyplot(countries):
    if countries!='All Countries':
        data=df[(df['Country'].isin(countries))]
    else:
        data=df
    #mean_exp = data.groupby('Experience')['Salary'].mean().reset_index()
    #fig = px.bar(mean_exp, x='Experience', y='Salary', color='Country') 
    aggregated_data = data.groupby(['Age', 'Country'])['Salary'].mean().reset_index()
    fig = px.bar(aggregated_data, x='Age', y='Salary', color='Country')
    return fig

