
import streamlit as st

st.title("🎈 Saint Chongers Life")

if st.session_state.get("t6", False):
    st.session_state.disabled = True
elif st.session_state.get("t6", False):
    st.session_state.disabled = False
col1, col2, col3 = st.columns(3)

with col1:
    toggle1 = st.toggle("Happiness", disabled=st.session_state.get("disabled", True))
    toggle2 = st.toggle("Giving", disabled=st.session_state.get("disabled", True))
with col2:
    toggle3 = st.toggle("Optimism", disabled=st.session_state.get("disabled", True))
    toggle4 = st.toggle("Respect", disabled=st.session_state.get("disabled", True))
with col3:
    toggle5 = st.toggle("Kindness", disabled=st.session_state.get("disabled", True))
    toggle6 = st.toggle("Ego", key="t6")

if toggle6:
    st.session_state.disabled = False
