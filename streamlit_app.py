import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("Simple Streamlit App with Graph and KPI")

# Sidebar
st.sidebar.header("Options")

# Data generation
data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Value': np.random.randint(0, 100, size=10)
})

# Display KPI
st.sidebar.subheader("Key Performance Indicator")
kpi_value = st.sidebar.empty()

# Display graph
st.subheader("Graph")

# Create a line plot using Matplotlib
fig, ax = plt.subplots()
ax.plot(data['Date'], data['Value'])
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.set_title('Random Data')

# Display the Matplotlib plot using Streamlit
st.pyplot(fig)

# Update KPI with the maximum value from the data
max_value = data['Value'].max()
kpi_value.text(f"Max Value: {max_value}")

# About section
st.sidebar.header("About")
st.sidebar.markdown("This is a simple Streamlit app with a graph and a Key Performance Indicator.")
st.sidebar.markdown("Built by Your Name")
