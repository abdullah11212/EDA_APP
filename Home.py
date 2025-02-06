import streamlit as st

# Title and Introduction
st.set_page_config(page_title="Data Analysis Web App", page_icon=":bar_chart:", layout="wide") # Optional: Set page configuration

st.title("Welcome to the Data Analysis For EDA")
st.markdown("""
Welcome to the Data Analysis Web App designed specifically for Exploratory Data Analysis (EDA).  
This application provides you with a suite of tools to effortlessly explore, visualize, and understand  data.
""")

st.write("---")  # Separator

# Section 1: Getting Started
st.header("Getting Started")
st.markdown("""
To begin  analysis, follow these simple steps:

1. To show Data Go to Data Section.
2. To show Analysis Go to Salary Section.
""")

st.write("---") # Separator


# Section 4: Contact (Optional)
st.header("Contact ")
st.markdown("""
Have questions or suggestions?  Feel free to reach out me at [asdmsr501@gmail.com](mailto:asdmsr501@gmail.com).
""")

st.markdown("[Visit my portfolio](https://abdullah11212.github.io/myprotofolio/)")
st.sidebar.title("Navigation")
# Sidebar for Navigation or Additional Information

st.sidebar.markdown("---")
st.sidebar.markdown("Developed by [Abdallah Aboutaleb]")
st.sidebar.markdown("Contact: [asdmsr501@gmail.com     https://abdullah11212.github.io/myprotofolio/]")

