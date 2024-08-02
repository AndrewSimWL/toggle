import streamlit as st

backgroundColor = '#273346'

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

happiness = st.toggle("Happiness")
optimism = st.toggle("Optimism")
kindness = st.toggle("Kindness")
giving = st.toggle("Giving")
respect = st.toggle("Respect")
ego = st.toggle("Ego")
