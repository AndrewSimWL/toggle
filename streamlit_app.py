import streamlit as st

backgroundColor = '#273346'

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

on = st.toggle("Activate feature")

if on:
    st.write("Feature activated!")
