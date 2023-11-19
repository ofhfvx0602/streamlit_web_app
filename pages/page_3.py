import streamlit as st
import pandas as pd

# Data analysis related
df = pd.read_csv('./data/平均月気温.txt', index_col='月')
st.line_chart(df)
st.bar_chart(df['2021年'])