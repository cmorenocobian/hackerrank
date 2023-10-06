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
date_range = st.slider("Select Date Range", min_value=data['Date'].min(), max_value=data['Date'].max(), value=(data['Date'].min(), data['Date'].max()))

# Filter data based on selected date range
filtered_data = data[(data['Date'] >= date_range[0]) & (data['Date'] <= date_range[1])]

# Line plot
st.subheader("Line Plot")
st.line_chart(filtered_data.set_index('Date')[['Value1', 'Value2', 'Value3']])

# Bar chart
st.subheader("Bar Chart")
st.bar_chart(filtered_data.set_index('Date')[['Value1', 'Value2', 'Value3']])

# Histogram
st.subheader("Histogram")
sns.histplot(data=data[(data['Date'] >= date_range[0]) & (data['Date'] <= date_range[1])], x='Value1', bins=20, kde=True, label='Value1', color='blue')
sns.histplot(data=data[(data['Date'] >= date_range[0]) & (data['Date'] <= date_range[1])], x='Value2', bins=20, kde=True, label='Value2', color='green')
sns.histplot(data=data[(data['Date'] >= date_range[0]) & (data['Date'] <= date_range[1])], x='Value3', bins=20, kde=True, label='Value3', color='red')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
st.pyplot()

# Summary statistics
st.subheader("Summary Statistics")
st.write(filtered_data.describe())

# You can add more plots and content as needed
