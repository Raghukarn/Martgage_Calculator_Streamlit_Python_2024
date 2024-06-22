import streamlit as st
import pandas as pd
import numpy as np

st.title(":blue[Top IMDB Movies]")

data = pd.read_csv("/pages/movies.csv")
st.write(data)

n = st.number_input("Tell me your number", value = 20)

data_sorted = data.sort_values(by=['imdb_score'], ascending=False)
data_sorted = data_sorted.head(n) 

st.write(n, ":orange[Movies & Shows with highest IMDB rating]")

st.bar_chart(data_sorted, x="title", y="imdb_score", color="type")
