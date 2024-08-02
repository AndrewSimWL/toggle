import streamlit as st


# Define the state of the sixth toggle
toggle6 = st.checkbox('Toggle 6')

# Container for the first five toggles
if toggle6:
    toggle1 = st.checkbox('Toggle 1')
    toggle2 = st.checkbox('Toggle 2')
    toggle3 = st.checkbox('Toggle 3')
    toggle4 = st.checkbox('Toggle 4')
    toggle5 = st.checkbox('Toggle 5')
else:
    st.write("Enable Toggle 6 to see the other toggles.")

# Display the state of the sixth toggle
st.write("Toggle 6:", toggle6)

# Display the states of the first five toggles for debugging
if toggle6:
    st.write("Toggle 1:", toggle1)
    st.write("Toggle 2:", toggle2)
    st.write("Toggle 3:", toggle3)
    st.write("Toggle 4:", toggle4)
    st.write("Toggle 5:", toggle5)
'''
backgroundColor = '#273346'

st.title("🎈 Saint Chongers Life")

col1, col2, col3 = st.columns(3)
with col1:
    toggle1 = st.toggle("Happiness", disabled=not toggle6)
    toggle2 = st.toggle("Giving")
with col2:
    toggle3 = st.toggle("Optimism")
    toggle4 = st.toggle("Respect")
with col3:
    toggle5 = st.toggle("Kindness")
    toggle6 = st.toggle("Ego")
'''
