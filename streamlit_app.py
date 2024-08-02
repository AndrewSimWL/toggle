
import streamlit as st

st.title("🎈 Saint Chongers Life")

col1, col2, col3 = st.columns(3)
disable = True
if toggle6:
    disable=False

with col1:
    toggle1 = st.toggle("Happiness", disabled=disable)
    toggle2 = st.toggle("Giving", disabled=disable)
with col2:
    toggle3 = st.toggle("Optimism", disabled=disable)
    toggle4 = st.toggle("Respect", disabled=disable)
with col3:
    toggle5 = st.toggle("Kindness", disabled=disable)
    toggle6 = st.toggle("Ego")
