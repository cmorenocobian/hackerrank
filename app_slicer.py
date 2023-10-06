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
st.title("Interactive Streamlit App")

# Date slicer
start_date = st.date_input("Start Date", min_value=data['Date'].min(), max_value=data['Date'].max())
end_date = st.date_input("End Date", min_value=data['Date'].min(), max_value=data['Date'].max())

# Convert the selected date inputs to datetime if needed
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter data based on selected dates
filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

# Line plot with multiple data series
st.subheader("Line Plot with Multiple Data Series")
st.line_chart(filtered_data.set_index('Date')[['Value1', 'Value2', 'Value3']])

# Bar chart with multiple data series
st.subheader("Bar Chart with Multiple Data Series")
st.bar_chart(filtered_data.set_index('Date')[['Value1', 'Value2', 'Value3']])

# Histogram with multiple data series
st.subheader("Histogram with Multiple Data Series")
sns.histplot(data=filtered_data, x='Value1', bins=20, kde=True, label='Value1', color='blue')
sns.histplot(data=filtered_data, x='Value2', bins=20, kde=True, label='Value2', color='green')
sns.histplot(data=filtered_data, x='Value3', bins=20, kde=True, label='Value3', color='red')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
st.pyplot()

# Summary statistics for multiple data series
st.subheader("Summary Statistics for Multiple Data Series")
st.write(filtered_data[['Value1', 'Value2', 'Value3']].describe())

# You can add more plots and content as needed
