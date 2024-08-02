import streamlit as st

backgroundColor = '#273346'

st.title("🎈 Saint Chongers Life")
toggle6_unlock = True

col1, col2, col3 = st.columns(3)
with col1:
    toggle1 = st.toggle("Happiness", disabled=toggle6_unlock)
    toggle2 = st.toggle("Giving")
with col2:
    toggle3 = st.toggle("Optimism")
    toggle4 = st.toggle("Respect")
with col3:
    toggle5 = st.toggle("Kindness")
    toggle6 = st.toggle("Ego")

if toggle6:
    toggle6_unlock = False
