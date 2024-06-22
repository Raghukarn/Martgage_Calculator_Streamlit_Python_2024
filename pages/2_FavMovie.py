import streamlit as st

st.title(":blue[Hello Welcome to Streamlit project]")

x = st.text_input("What's Your Favourite Movie?")
st.write(f"Nice choice, I like :orange[{x}] too!")
