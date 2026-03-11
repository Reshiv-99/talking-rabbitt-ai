import streamlit as st
import pandas as pd

st.title("Talking Rabbitt – AI Data Assistant")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Dataset Preview")
    st.dataframe(df)

question = st.text_input("Ask a question about the data")

if question:
    st.write("AI Insight:")
    st.write("Example AI insight based on uploaded data.")
