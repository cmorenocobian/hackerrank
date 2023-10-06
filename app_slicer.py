import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=365, freq='D'),
    'Value': np.random.randn(365).cumsum()
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

# Line plot
st.subheader("Line Plot")
st.line_chart(filtered_data.set_index('Date')['Value'])

# Scatter plot
st.subheader("Scatter Plot")
st.scatter_chart(filtered_data)

# Histogram
st.subheader("Histogram")
sns.histplot(filtered_data['Value'], bins=20, kde=True)
st.pyplot()

# Summary statistics
st.subheader("Summary Statistics")
st.write(filtered_data.describe())

# You can add more plots and content as needed
