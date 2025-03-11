import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    df = pd.read_excel((PNM) DATA TAHUNAN 2024 (EDIT T).xlsx)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')  # Clean column names
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
if 'year' in df.columns:
    years = df['year'].dropna().unique()
    selected_year = st.sidebar.selectbox("Select Year", years)
    df = df[df['year'] == selected_year]

# Dashboard Title
st.title("📊 Data Dashboard")

# Show Data Preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Show Summary Statistics
st.subheader("Summary Statistics")
st.write(df.describe())

