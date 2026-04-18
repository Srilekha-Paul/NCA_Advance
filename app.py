# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# import time

# st.set_page_config(page_title="NCA AI Project", layout="wide")

# st.sidebar.title("🧠 NCA Controls")

# signal = st.sidebar.selectbox("Choose Action",[
#     "Grow Heart",
#     "Grow Gecko",
#     "Damage",
#     "Heal",
#     "Accuracy Graph"
# ])

# st.title("🧬 Adaptive Neural Cellular Automata")
# st.subheader("Self-Healing Morphogenesis with AI Signals")

# # ---------------- Heart ----------------
# def heart():
#     x=np.linspace(-2,2,400)
#     y=np.linspace(-2,2,400)
#     X,Y=np.meshgrid(x,y)
#     Z=(X**2+Y**2-1)**3-X**2*Y**3

#     fig,ax=plt.subplots(figsize=(6,6))
#     ax.contourf(X,Y,Z,levels=[-1,0],colors=['red'])
#     ax.axis("off")
#     st.pyplot(fig)

# # ---------------- Gecko ----------------
# def gecko(color=[0,1,0]):
#     img=np.zeros((300,300,3))
#     img[100:220,130:170]=color
#     img[80:120,90:210]=color
#     img[210:260,110:130]=color
#     img[210:260,170:190]=color
#     st.image(img,width=400)

# # ---------------- Graph ----------------
# def graph():
#     x=[0,50,100,150,200,250,300]
#     y=[45,17,8,5,3,2,1]

#     fig,ax=plt.subplots()
#     ax.plot(x,y,marker='o')
#     ax.set_title("Training Loss Reduction")
#     ax.set_xlabel("Epoch")
#     ax.set_ylabel("Loss")
#     st.pyplot(fig)

# # ---------------- MAIN ----------------
# if st.button("Run Project"):

#     if signal=="Grow Heart":
#         st.success("Heart Generated")
#         heart()

#     elif signal=="Grow Gecko":
#         st.success("Gecko Generated")
#         gecko()

#     elif signal=="Damage":
#         st.warning("Damage Applied")
#         gecko([1,0,0])

#     elif signal=="Heal":
#         st.success("Healing Completed")
#         gecko()

#     elif signal=="Accuracy Graph":
#         st.info("Training Performance")
#         graph()



import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="NCA AI Dashboard",
    layout="wide"
)

# ---------------- Sidebar ----------------
st.sidebar.title("🧠 NCA Controls")

signal = st.sidebar.selectbox("Choose Action",[
    "Grow Heart",
    "Grow Gecko",
    "Damage",
    "Heal",
    "Accuracy Graph"
])

# ---------------- Main ----------------
st.title("🧬 Adaptive Neural Cellular Automata")
st.subheader("Self-Healing Morphogenesis with AI Signals")

# ---------------- Heart ----------------
def heart():
    x=np.linspace(-2,2,300)
    y=np.linspace(-2,2,300)
    X,Y=np.meshgrid(x,y)

    Z=(X**2+Y**2-1)**3 - X**2*Y**3

    fig,ax=plt.subplots(figsize=(4,4))
    fig.patch.set_facecolor("#0E1117")
    ax.set_facecolor("#0E1117")

    ax.contourf(X,Y,Z,levels=[-1,0],colors=['red'])
    ax.axis("off")

    st.pyplot(fig,use_container_width=False)

# ---------------- Gecko ----------------
def gecko(color=[0,1,0]):
    img=np.zeros((220,220,3))

    img[70:160,95:125]=color
    img[50:80,60:160]=color
    img[160:200,80:95]=color
    img[160:200,125:140]=color

    st.image(img,width=300)

# ---------------- Graph ----------------
def graph():
    x=[0,50,100,150,200,250,300]
    y=[45,17,8,5,3,2,1]

    fig,ax=plt.subplots(figsize=(6,3))
    ax.plot(x,y,marker='o',linewidth=3,color='cyan')
    ax.set_title("Training Loss")
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    st.pyplot(fig)

# ---------------- Button ----------------
if st.button("🚀 Run Project"):

    st.markdown("---")

    col1,col2,col3 = st.columns([1,2,1])

    with col2:

        if signal=="Grow Heart":
            st.success("Heart Generated Successfully")
            heart()

        elif signal=="Grow Gecko":
            st.success("Gecko Generated Successfully")
            gecko()

        elif signal=="Damage":
            st.warning("Damage Applied")
            gecko([1,0,0])

        elif signal=="Heal":
            st.success("Healing Completed")
            gecko()

        elif signal=="Accuracy Graph":
            st.info("Training Performance")
            graph()