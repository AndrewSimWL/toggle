import streamlit as st

backgroundColor = '#273346'

st.title("🎈 Saint Chongers Life")
ego_unlock = False
if happiness:
    ego_unlock = True

col1, col2, col3 = st.columns(3)
with col1:
    happiness = st.toggle("Happiness")
    giving = st.toggle("Giving")
with col2:
    optimism = st.toggle("Optimism")
    respect = st.toggle("Respect")
with col3:
    kindness = st.toggle("Kindness")
    ego = st.toggle("Ego", disabled=ego_unlock)
