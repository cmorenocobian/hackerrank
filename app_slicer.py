import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=365, freq='D'),
    'Value1': np.random.randn(365).cumsum(),
    'Value2': np.random.randn(365).cumsum(),
    'Value3': np.random.randn(365).cumsum()
})

# Set app title
st.title("Enhanced Interactive Streamlit App")

# Date range slider
date_range_slider = st.slider("Select Date Range", 0, len(data) - 1, (0, len(data) - 1))

# Convert the selected slider values to date range
start_index, end_index = date_range_slider
start_date, end_date = data.iloc[start_index]['Date'], data.iloc[end_index]['Date']

# Filter data based on selected date range
filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

# Line plot
st.subheader("Line Plot")
st.line_chart(filtered_data.set_index('Date')[['Value1', 'Value2', 'Value3']])

# Bar chart
st.subheader("Bar Chart")
st.bar_chart(filtered_data.set_index('Date')[['Value1', 'Value2', 'Value3']])

# Histogram
st.subheader("Histogram")
sns.histplot(data=filtered_data, x='Value1', bins=20, kde=True, label='Value1', color='blue')
sns.histplot(data=filtered_data, x='Value2', bins=20, kde=True, label='Value2', color='green')
sns.histplot(data=filtered_data, x='Value3', bins=20, kde=True, label='Value3', color='red')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
st.pyplot()

# Summary statistics
st.subheader("Summary Statistics")
st.write(filtered_data.describe())

# You can add more plots and content as needed
