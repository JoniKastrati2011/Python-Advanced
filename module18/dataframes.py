import pandas as pd
import streamlit as st

st.header("Displaying dataframes")

data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [22, 27, 32, 29, 27],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Chicago', 'Phoenix']
})

st.dataframe(data)

