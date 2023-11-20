#!/usr/bin/env python
# coding: utf-8



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import types

# Load your data using st.cache_data
@st.cache_data(hash_funcs={types.FunctionType: lambda _: None})
def load_data():
    data = pd.read_csv('Preprocessed World University Rankings 2023 Dataset.csv')
    # Ensure the columns are numeric and drop NaNs
    data['No of student per staff'] = pd.to_numeric(data['No of student per staff'], errors='coerce')
    data['University Rank'] = pd.to_numeric(data['University Rank'], errors='coerce')
    return data.dropna(subset=['No of student per staff', 'University Rank'])

data = load_data()

# Streamlit application layout
st.title('World University Rankings 2023 Analysis')

# Enhanced Visualization
st.subheader('University Rank vs Student-Staff Ratio')
plt.figure(figsize=(12, 8))
scatter = sns.scatterplot(
    data=data, 
    x='No of student per staff', 
    y='University Rank', 
    alpha=0.6
)

# Adding a regression line
sns.regplot(
    data=data, 
    x='No of student per staff', 
    y='University Rank', 
    scatter=False, 
    color='blue'
)

plt.title('University Rank vs Student-Staff Ratio')
plt.xlabel('Number of Students per Staff')
plt.ylabel('University Rank')
plt.gca().invert_yaxis()  # Invert y-axis for better rank representation
st.pyplot(plt)

# Subset of data
st.subheader('Data Subset View')
st.dataframe(data.head())  # Change .head() to display a different subset





