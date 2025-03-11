import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    df = pd.read_excel("(PNM) DATA TAHUNAN 2024 (EDIT T).xlsx", header=1)  # Adjust header if needed
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

# Correlation Heatmap
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Interactive Bar Chart
st.subheader("Bar Chart of a Numeric Column")
numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
if numeric_columns:
    selected_column = st.selectbox("Select Column", numeric_columns)
    fig, ax = plt.subplots()
    df[selected_column].hist(bins=20, ax=ax)
    st.pyplot(fig)
else:
    st.warning("No numeric columns found.")

# Run with: streamlit run app.py

