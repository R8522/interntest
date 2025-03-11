import streamlit as st
import pandas as pd

# GitHub Raw URL (Replace this with your actual file URL)
GITHUB_RAW_URL = "https://github.com/R8522/interntest/blob/main/STATISTIK%201%20-%20Kumulatif%20Keahlian.xlsx"

@st.cache_data
def load_data():
    """Load dataset from GitHub."""
    df = pd.read_excel(GITHUB_RAW_URL)

    # Fill missing numerical values with mean
    for col in df.select_dtypes(include=['number']):
        df[col] = df[col].fillna(df[col].mean())

    # Fill missing categorical values with mode
    for col in df.select_dtypes(include=['object']):
        df[col] = df[col].fillna(df[col].mode()[0])

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    return df

# Streamlit App Layout
st.title("📊 Statistik 1 - Kumulatif Keahlian Dashboard")

# Display dataframe
st.subheader("Cleaned Data Preview")
st.dataframe(df)

# Display missing values count
st.subheader("Missing Values Summary")
st.write(df.isnull().sum())

# Display summary statistics
st.subheader("Dataset Summary Statistics")
st.write(df.describe())

# Additional Filters (Optional)
st.subheader("Filter Data by Location")
selected_location = st.selectbox("Choose a location:", df["LOKASI PARLIMEN"].unique())
filtered_df = df[df["LOKASI PARLIMEN"] == selected_location]
st.dataframe(filtered_df)
