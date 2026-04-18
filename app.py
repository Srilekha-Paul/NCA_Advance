import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("🧠 Neural Cellular Automata Dashboard")
st.subheader("Signal Driven Self-Healing Morphogenesis")

signal = st.selectbox("Choose Signal",[
    "Grow Heart",
    "Grow Gecko",
    "Damage",
    "Heal",
    "Change Color"
])

# ---------------- Heart ----------------
def draw_heart():
    x = np.linspace(-2,2,400)
    y = np.linspace(-2,2,400)
    X,Y = np.meshgrid(x,y)

    Z = (X**2 + Y**2 -1)**3 - X**2 * Y**3

    fig, ax = plt.subplots(figsize=(6,6))
    ax.contourf(X,Y,Z,levels=[-10,0],colors=['red'])
    ax.axis("off")
    st.pyplot(fig)

# ---------------- Gecko ----------------
def draw_gecko():
    img = np.zeros((300,300,3))
    img[100:220,130:170] = [0,1,0]
    img[80:120,90:210] = [0,1,0]
    img[210:260,110:130] = [0,1,0]
    img[210:260,170:190] = [0,1,0]

    st.image(img,width=400)

# ---------------- Damage ----------------
def draw_damage():
    img = np.zeros((300,300,3))
    img[100:220,130:170] = [0,1,0]
    img[80:120,90:210] = [0,1,0]

    img[130:180,130:170] = [0,0,0]

    st.image(img,width=400)

# ---------------- Heal ----------------
def draw_heal():
    img = np.zeros((300,300,3))
    img[100:220,130:170] = [0,1,0]
    img[80:120,90:210] = [0,1,0]
    img[130:180,130:170] = [0,1,0]

    st.image(img,width=400)

# ---------------- Main ----------------
if st.button("Run Signal"):

    if signal=="Grow Heart":
        st.success("Heart Generated")
        draw_heart()

    elif signal=="Grow Gecko":
        st.success("Gecko Generated")
        draw_gecko()

    elif signal=="Damage":
        st.warning("Damage Applied")
        draw_damage()

    elif signal=="Heal":
        st.success("Self Healing Activated")
        draw_heal()

    elif signal=="Change Color":
        st.info("Color Mutation Applied")
        draw_gecko()