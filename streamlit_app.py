import streamlit as st

# Define the state of the sixth toggle
toggle6 = st.checkbox('Toggle 6')

# Define the first five toggles and disable them if the sixth toggle is not enabled
toggle1 = st.checkbox('Toggle 1', disabled=not toggle6)
toggle2 = st.checkbox('Toggle 2', disabled=not toggle6)
toggle3 = st.checkbox('Toggle 3', disabled=not toggle6)
toggle4 = st.checkbox('Toggle 4', disabled=not toggle6)
toggle5 = st.checkbox('Toggle 5', disabled=not toggle6)

# Display the states of all toggles for debugging
st.write("Toggle 6:", toggle6)
st.write("Toggle 1:", toggle1)
st.write("Toggle 2:", toggle2)
st.write("Toggle 3:", toggle3)
st.write("Toggle 4:", toggle4)
st.write("Toggle 5:", toggle5)
