import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt 

# Sample data
data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=365, freq='D'),
    'Value': np.random.randn(365).cumsum(),
    'Value2': np.random.randn(365).cumsum(),
    'Value3': np.random.randn(365).cumsum()
})

# Set app title
st.title("Interactive Streamlit App")

# Set initial values for start_date and end_date
start_date = dt.date(2023, 9, 1)
end_date = dt.date(2023, 10, 1)

# Date slicer
start_date = st.date_input("Start Date", min_value=data['Date'].min(), max_value=data['Date'].max(), value=start_date)
end_date = st.date_input("End Date", min_value=data['Date'].min(), max_value=data['Date'].max(), value=end_date)

print('fecha inicio', start_date)

# Convert the selected date inputs to datetime if needed
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter data based on selected dates
filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

st.set_option('deprecation.showPyplotGlobalUse', False)

# Line plot
st.subheader("Line Plot - Value, Value2, and Value3")
st.line_chart(filtered_data.set_index('Date')[['Value', 'Value2', 'Value3']])

# Bar chart
st.subheader("Bar Chart - Value, Value2, and Value3")
st.bar_chart(filtered_data.set_index('Date')[['Value', 'Value2', 'Value3']])

# Histogram
st.subheader("Histogram - Value, Value2, and Value3")
sns.histplot(filtered_data[['Value', 'Value2', 'Value3']], bins=20, kde=True)
st.pyplot()  # Pass the figure to st.pyplot()

# Summary statistics
st.subheader("Summary Statistics")
st.write(filtered_data[['Value', 'Value2', 'Value3']].describe())
