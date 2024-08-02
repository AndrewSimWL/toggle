import streamlit as st

backgroundColor = '#273346'

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

col1, col2, col3 = st.columns(3)
with col1:
    happiness = st.toggle("Happiness")
with col2:
    optimism = st.toggle("Optimism")
with col3:
    kindness = st.toggle("Kindness")
    
col4, cold5, col6 = st.column(3)
with col4:
    giving = st.toggle("Giving")
with col5:
    respect = st.toggle("Respect")
with col6:
    ego = st.toggle("Ego")
