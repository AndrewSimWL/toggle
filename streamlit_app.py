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
    
giving = st.toggle("Giving")
respect = st.toggle("Respect")
ego = st.toggle("Ego")
