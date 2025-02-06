import streamlit as st
import pandas as pd
import plotly.express as px
import helper
df=helper.load_data()
#Country plot
country_options = st.selectbox('Select Country', ['All Countries', 'Select Countries'])
if country_options == 'All Countries':
    countries = 'All Countries'
else:
    countries = st.multiselect('Select', df['Country'].unique())
st.header('Avrege salary by country')
total_contry=helper.countryplot(countries)
st.plotly_chart(total_contry)

#EXP Plot
st.header('Avrege exp by country')
total_exp=helper.expyplot(countries)
st.plotly_chart(total_exp)

#AGE Plot
st.header('Avrege Age by country')
total_Age=helper.Ageyplot(countries)
st.plotly_chart(total_Age)