
import streamlit as st

st.title("🎈 Saint Chongers Life")

st.session_state.disabled = True
col1, col2, col3 = st.columns(3)

with col1:
    toggle1 = st.toggle("Happiness", disabled=st.session_state.disabled)
    toggle2 = st.toggle("Giving", disabled=st.session_state.disabled)
with col2:
    toggle3 = st.toggle("Optimism", disabled=st.session_state.disabled)
    toggle4 = st.toggle("Respect", disabled=st.session_state.disabled)
with col3:
    toggle5 = st.toggle("Kindness", disabled=st.session_state.disabled)
    toggle6 = st.toggle("Ego")

if toggle6:
    st.session_state.disabled = False
