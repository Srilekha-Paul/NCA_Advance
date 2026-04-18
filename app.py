import streamlit as st

st.set_page_config(layout="wide")

st.title("🧠 Neural Cellular Automata Dashboard")

signal = st.selectbox("Choose Signal",[
"Grow Heart",
"Grow Gecko",
"Damage",
"Heal",
"Change Color"
])

if st.button("Run"):
    st.success(f"Signal Activated: {signal}")