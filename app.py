import streamlit as st
import pandas as pd

st.title("📊 Suicide Data Analysis Dashboard")

df = pd.read_csv(r"C:\Users\vemir\Downloads\suicide_data.csv")

st.write(df.head())

country = st.selectbox("Select Country", df["country"].unique())

filtered = df[df["country"] == country]

st.write(filtered)