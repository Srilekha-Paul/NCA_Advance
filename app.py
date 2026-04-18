# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# import time
# from datetime import datetime

# # =========================================================
# # PAGE CONFIG
# # =========================================================
# st.set_page_config(
#     page_title="Adaptive Neural Cellular Automata",
#     page_icon="🧬",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # =========================================================
# # SESSION STATE
# # =========================================================
# if "signals" not in st.session_state:
#     st.session_state.signals = 5

# if "accuracy" not in st.session_state:
#     st.session_state.accuracy = 95.2

# if "healing" not in st.session_state:
#     st.session_state.healing = 89

# if "logs" not in st.session_state:
#     st.session_state.logs = [
#         ("15:55", "Heart generated OK", "#22c55e"),
#         ("15:54", "Signal executed", "#38bdf8"),
#         ("15:54", "Epoch 500 done", "#ffffff"),
#         ("15:53", "Model loaded", "#ffffff"),
#     ]

# # =========================================================
# # PREMIUM CSS
# # =========================================================
# st.markdown("""
# <style>

# html, body, [class*="css"]{
#     font-family: 'Segoe UI', sans-serif;
# }

# body{
#     background:#0a0d14;
# }

# .main{
#     background:#0a0d14;
#     color:white;
# }

# .block-container{
#     padding-top:0rem;
#     padding-bottom:0rem;
#     padding-left:0rem;
#     padding-right:0rem;
#     max-width:100%;
# }

# /* SIDEBAR */
# section[data-testid="stSidebar"]{
#     background:#10141f;
#     border-right:1px solid rgba(255,255,255,0.05);
# }

# /* CARDS */
# .card{
#     background:#141928;
#     border:1px solid rgba(255,255,255,0.06);
#     border-radius:14px;
#     padding:18px;
# }

# /* METRIC */
# .metric{
#     background:#141928;
#     border:1px solid rgba(255,255,255,0.06);
#     border-radius:14px;
#     padding:18px;
# }

# .metric-title{
#     color:#6b7280;
#     font-size:11px;
#     letter-spacing:2px;
# }

# .metric-value{
#     color:white;
#     font-size:28px;
#     font-weight:700;
# }

# /* BUTTON */
# .stButton>button{
#     width:100%;
#     height:48px;
#     border-radius:10px;
#     background:linear-gradient(90deg,#2563eb,#7c3aed);
#     color:white;
#     font-size:16px;
#     font-weight:700;
#     border:none;
# }

# /* SELECT */
# .stSelectbox label{
#     color:#94a3b8 !important;
# }

# hr{
#     margin:0.2rem;
# }

# </style>
# """, unsafe_allow_html=True)

# # =========================================================
# # SIDEBAR
# # =========================================================
# st.sidebar.markdown("## 🧠 NCA Controls")

# signal = st.sidebar.selectbox(
#     "Choose Action",
#     ["Grow Heart", "Grow Gecko", "Grow Emoji", "Heal", "Damage", "Analytics"]
# )

# run = st.sidebar.button("🚀 Execute Signal")

# st.sidebar.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
# st.sidebar.success("● Dashboard")

# # =========================================================
# # EXECUTION FUNCTIONALITY
# # =========================================================
# if run:
#     st.session_state.signals += 1
#     st.session_state.accuracy = round(np.random.uniform(92, 98), 1)
#     st.session_state.healing = int(np.random.uniform(84, 98))

#     now = datetime.now().strftime("%H:%M")
#     st.session_state.logs.insert(
#         0,
#         (now, f"{signal} signal executed", "#22c55e")
#     )

# # =========================================================
# # TOPBAR
# # =========================================================
# top1, top2, top3 = st.columns([8,1,1])

# with top1:
#     st.markdown("""
#     <div style='padding:18px 28px'>
#     <h1 style='font-size:34px;margin-bottom:0px;'>🧬 Adaptive Neural Cellular Automata</h1>
#     <p style='color:#64748b;margin-top:4px;font-size:16px'>
#     Self-Healing Morphogenesis with AI Signals
#     </p>
#     </div>
#     """, unsafe_allow_html=True)

# with top2:
#     st.markdown("""
#     <div style='margin-top:28px;
#     background:#052e16;
#     color:#22c55e;
#     padding:8px 15px;
#     border-radius:20px;
#     text-align:center;
#     font-weight:700'>
#     ● LIVE
#     </div>
#     """, unsafe_allow_html=True)

# with top3:
#     st.markdown("""
#     <div style='margin-top:28px;
#     background:#7c3aed;
#     color:white;
#     padding:8px 15px;
#     border-radius:10px;
#     text-align:center;
#     font-weight:700'>
#     Deploy
#     </div>
#     """, unsafe_allow_html=True)

# # =========================================================
# # METRICS
# # =========================================================
# m1,m2,m3,m4 = st.columns(4)

# metrics = [
#     ("ACCURACY", f"{st.session_state.accuracy}%"),
#     ("SIGNALS", str(st.session_state.signals)),
#     ("HEALING", f"{st.session_state.healing}%"),
#     ("EPOCHS", "500")
# ]

# for col,(title,val) in zip([m1,m2,m3,m4],metrics):
#     with col:
#         st.markdown(f"""
#         <div class='metric'>
#             <div class='metric-title'>{title}</div>
#             <div class='metric-value'>{val}</div>
#         </div>
#         """, unsafe_allow_html=True)

# # =========================================================
# # VISUAL FUNCTIONS
# # =========================================================
# def draw_heart():
#     x=np.linspace(-2,2,400)
#     y=np.linspace(-2,2,400)
#     X,Y=np.meshgrid(x,y)
#     Z=(X**2+Y**2-1)**3 - X**2*Y**3

#     fig,ax=plt.subplots(figsize=(10,5))
#     fig.patch.set_facecolor("#080b13")
#     ax.set_facecolor("#080b13")
#     ax.contourf(X,Y,Z,levels=[-1,0],colors=["#ef4444"])
#     ax.axis("off")
#     st.pyplot(fig,use_container_width=True)

# def draw_gecko(color=[0,1,0]):
#     img=np.zeros((420,800,3))
#     img[150:280,360:440]=color
#     img[120:170,250:560]=color
#     img[280:360,340:370]=color
#     img[280:360,430:460]=color
#     st.image(img,use_container_width=True)

# def draw_emoji():
#     fig,ax=plt.subplots(figsize=(7,5))
#     fig.patch.set_facecolor("#080b13")
#     ax.set_facecolor("#080b13")
#     circle=plt.Circle((0,0),1,color="gold")
#     ax.add_patch(circle)
#     ax.plot([-0.35,0.35],[0.35,0.35],'ko',markersize=12)
#     theta=np.linspace(-1,1,100)
#     ax.plot(theta,-0.4+0.25*(1-theta**2),color="black",linewidth=4)
#     ax.set_xlim(-1.4,1.4)
#     ax.set_ylim(-1.3,1.3)
#     ax.axis("off")
#     st.pyplot(fig,use_container_width=True)

# def analytics():
#     x=[0,50,100,150,200,250,300,400,500]
#     y=[45,18,8,5,3,2.2,1.8,1.3,1]
#     fig,ax=plt.subplots(figsize=(10,5))
#     fig.patch.set_facecolor("#080b13")
#     ax.set_facecolor("#080b13")
#     ax.plot(x,y,color="#38bdf8",linewidth=3,marker='o')
#     ax.tick_params(colors='white')
#     ax.set_title("Training Loss Curve",color="white")
#     st.pyplot(fig,use_container_width=True)

# # =========================================================
# # MAIN GRID
# # =========================================================
# left,right = st.columns([3.4,1.2])

# # ---------------------------------------------------------
# # MAIN CANVAS
# # ---------------------------------------------------------
# with left:
#     st.markdown("<div class='card'><h3>Morphogenesis Canvas</h3>", unsafe_allow_html=True)

#     if run:
#         with st.spinner("Executing Signal..."):
#             time.sleep(1)

#     if signal=="Grow Heart":
#         draw_heart()

#     elif signal=="Grow Gecko":
#         draw_gecko()

#     elif signal=="Damage":
#         draw_gecko([1,0,0])

#     elif signal=="Heal":
#         draw_gecko([0,0.8,1])

#     elif signal=="Grow Emoji":
#         draw_emoji()

#     elif signal=="Analytics":
#         analytics()

#     st.markdown("</div>", unsafe_allow_html=True)

# # ---------------------------------------------------------
# # RIGHT PANEL
# # ---------------------------------------------------------
# with right:

#     st.markdown(f"""
#     <div class='card'>
#     <h4>SIGNAL PARAMETERS</h4>
#     <p>Target Shape <b style='float:right'>{signal}</b></p>
#     <p>Grid Size <b style='float:right'>128 × 128</b></p>
#     <p>Cell States <b style='float:right'>16</b></p>
#     <p>Fire Rate <b style='float:right'>0.50</b></p>
#     <p>LR <b style='float:right'>2e-3</b></p>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("")

#     st.markdown("<div class='card'><h4>TRAINING PROGRESS</h4>", unsafe_allow_html=True)
#     st.progress(100)
#     st.caption("500 / 500 Epochs")

#     st.progress(st.session_state.healing)
#     st.caption("Loss Optimized")

#     st.markdown("</div>", unsafe_allow_html=True)

#     st.markdown("")

#     st.markdown("<div class='card'><h4>ACTIVITY LOG</h4>", unsafe_allow_html=True)

#     for t,msg,color in st.session_state.logs[:5]:
#         st.markdown(
#             f"<p style='color:{color};font-size:14px'>{t} &nbsp; {msg}</p>",
#             unsafe_allow_html=True
#         )

#     st.markdown("</div>", unsafe_allow_html=True)





# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# import time
# from datetime import datetime

# # =========================================================
# # PAGE CONFIG
# # =========================================================
# st.set_page_config(
#     page_title="Adaptive Neural Cellular Automata",
#     page_icon="🧬",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # =========================================================
# # SESSION STATE
# # =========================================================
# if "signals" not in st.session_state:
#     st.session_state.signals = 5

# if "accuracy" not in st.session_state:
#     st.session_state.accuracy = 95.2

# if "healing" not in st.session_state:
#     st.session_state.healing = 89

# if "shape" not in st.session_state:
#     st.session_state.shape = "Grow Heart"

# if "logs" not in st.session_state:
#     st.session_state.logs = [
#         ("15:55", "Heart generated OK"),
#         ("15:54", "Signal executed"),
#         ("15:54", "Epoch 500 completed"),
#         ("15:53", "Model loaded"),
#     ]

# # =========================================================
# # PREMIUM CSS
# # =========================================================
# st.markdown("""
# <style>

# html, body, [class*="css"]{
#     font-family: 'Segoe UI', sans-serif;
# }

# body{
#     background:#0a0d14;
# }

# .main{
#     background:#0a0d14;
#     color:white;
# }

# .block-container{
#     padding-top:0rem;
#     padding-bottom:0rem;
#     padding-left:0rem;
#     padding-right:0rem;
#     max-width:100%;
# }

# /* Sidebar */
# section[data-testid="stSidebar"]{
#     background:#10141f;
#     border-right:1px solid rgba(255,255,255,0.06);
#     width:270px !important;
# }

# /* Cards */
# .card{
#     background:#141928;
#     border:1px solid rgba(255,255,255,0.07);
#     border-radius:14px;
#     padding:18px;
# }

# /* Metric Cards */
# .metric{
#     background:#141928;
#     border:1px solid rgba(255,255,255,0.07);
#     border-radius:14px;
#     padding:20px;
# }

# .metric-title{
#     color:#64748b;
#     font-size:11px;
#     letter-spacing:2px;
# }

# .metric-value{
#     font-size:30px;
#     font-weight:700;
#     color:white;
# }

# /* Buttons */
# .stButton>button{
#     width:100%;
#     height:50px;
#     border:none;
#     border-radius:10px;
#     background:linear-gradient(90deg,#2563eb,#7c3aed);
#     color:white;
#     font-size:16px;
#     font-weight:700;
# }

# /* Select */
# .stSelectbox label{
#     color:#94a3b8 !important;
# }

# /* Progress */
# div[data-testid="stProgressBar"] > div > div{
#     background:linear-gradient(90deg,#38bdf8,#8b5cf6);
# }

# /* Remove top gap */
# header{
#     visibility:hidden;
# }

# </style>
# """, unsafe_allow_html=True)

# # =========================================================
# # SIDEBAR
# # =========================================================
# st.sidebar.markdown("## 🧠 NCA Controls")

# signal = st.sidebar.selectbox(
#     "Choose Action",
#     [
#         "Grow Heart",
#         "Grow Gecko",
#         "Grow Emoji",
#         "Heal",
#         "Damage",
#         "Analytics"
#     ]
# )

# run = st.sidebar.button("🚀 Execute Signal")

# st.sidebar.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
# st.sidebar.success("● Dashboard")

# # =========================================================
# # ACTION
# # =========================================================
# if run:
#     st.session_state.shape = signal
#     st.session_state.signals += 1
#     st.session_state.accuracy = round(np.random.uniform(92,98),1)
#     st.session_state.healing = int(np.random.uniform(84,98))

#     tm = datetime.now().strftime("%H:%M")
#     st.session_state.logs.insert(
#         0,
#         (tm, f"{signal} signal executed")
#     )

# # =========================================================
# # HEADER
# # =========================================================
# h1,h2,h3 = st.columns([8,1,1])

# with h1:
#     st.markdown("""
#     <div style='padding:18px 28px'>
#         <h1 style='font-size:34px;margin-bottom:0px;'>🧬 Adaptive Neural Cellular Automata</h1>
#         <p style='color:#64748b;margin-top:5px;font-size:16px'>
#         Self-Healing Morphogenesis with AI Signals
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

# with h2:
#     st.markdown("""
#     <div style='margin-top:30px;
#     background:#052e16;
#     color:#22c55e;
#     padding:8px 14px;
#     border-radius:20px;
#     text-align:center;
#     font-weight:700'>
#     ● LIVE
#     </div>
#     """, unsafe_allow_html=True)

# with h3:
#     st.markdown("""
#     <div style='margin-top:30px;
#     background:#7c3aed;
#     color:white;
#     padding:8px 14px;
#     border-radius:10px;
#     text-align:center;
#     font-weight:700'>
#     Deploy
#     </div>
#     """, unsafe_allow_html=True)

# # =========================================================
# # METRICS
# # =========================================================
# m1,m2,m3,m4 = st.columns(4)

# metrics = [
#     ("Accuracy", f"{st.session_state.accuracy}%"),
#     ("Signals", st.session_state.signals),
#     ("Healing", f"{st.session_state.healing}%"),
#     ("Epochs", "500")
# ]

# for col,(title,val) in zip([m1,m2,m3,m4],metrics):
#     with col:
#         st.markdown(f"""
#         <div class='metric'>
#             <div class='metric-title'>{title.upper()}</div>
#             <div class='metric-value'>{val}</div>
#         </div>
#         """, unsafe_allow_html=True)

# # =========================================================
# # DRAW FUNCTIONS
# # =========================================================
# def heart():
#     x=np.linspace(-2,2,400)
#     y=np.linspace(-2,2,400)
#     X,Y=np.meshgrid(x,y)
#     Z=(X**2+Y**2-1)**3 - X**2*Y**3

#     fig,ax=plt.subplots(figsize=(10,5))
#     fig.patch.set_facecolor("#080b13")
#     ax.set_facecolor("#080b13")
#     ax.contourf(X,Y,Z,levels=[-1,0],colors=["#ef4444"])
#     ax.axis("off")
#     st.pyplot(fig,use_container_width=True)

# def gecko(color=[0,1,0]):
#     img=np.zeros((420,800,3))
#     img[150:280,360:440]=color
#     img[120:170,240:560]=color
#     img[280:360,340:370]=color
#     img[280:360,430:460]=color
#     st.image(img,use_container_width=True)

# def emoji():
#     fig,ax=plt.subplots(figsize=(7,5))
#     fig.patch.set_facecolor("#080b13")
#     ax.set_facecolor("#080b13")
#     c=plt.Circle((0,0),1,color="gold")
#     ax.add_patch(c)
#     ax.plot([-0.35,0.35],[0.35,0.35],'ko',markersize=12)
#     t=np.linspace(-1,1,100)
#     ax.plot(t,-0.4+0.25*(1-t**2),color='black',linewidth=4)
#     ax.axis("off")
#     ax.set_xlim(-1.4,1.4)
#     ax.set_ylim(-1.3,1.3)
#     st.pyplot(fig,use_container_width=True)

# def analytics():
#     x=[0,50,100,150,200,250,300,400,500]
#     y=[45,18,8,5,3,2.2,1.8,1.3,1]

#     fig,ax=plt.subplots(figsize=(10,5))
#     fig.patch.set_facecolor("#080b13")
#     ax.set_facecolor("#080b13")
#     ax.plot(x,y,color="#38bdf8",linewidth=3,marker="o")
#     ax.tick_params(colors="white")
#     ax.set_title("Training Loss Curve",color="white")
#     st.pyplot(fig,use_container_width=True)

# # =========================================================
# # MAIN GRID
# # =========================================================
# left,right = st.columns([3.5,1.2])

# # ---------------- MAIN DISPLAY ----------------
# with left:

#     st.markdown("<div class='card'><h3>Morphogenesis Canvas</h3>", unsafe_allow_html=True)

#     if run:
#         with st.spinner("Executing Signal..."):
#             time.sleep(1)

#     choice = st.session_state.shape

#     if choice=="Grow Heart":
#         heart()

#     elif choice=="Grow Gecko":
#         gecko()

#     elif choice=="Damage":
#         gecko([1,0,0])

#     elif choice=="Heal":
#         gecko([0,0.8,1])

#     elif choice=="Grow Emoji":
#         emoji()

#     elif choice=="Analytics":
#         analytics()

#     st.markdown("</div>", unsafe_allow_html=True)

# # ---------------- RIGHT PANEL ----------------
# with right:

#     st.markdown(f"""
#     <div class='card'>
#     <h4>Signal Parameters</h4>
#     <p>Target Shape <b style='float:right'>{choice}</b></p>
#     <p>Grid Size <b style='float:right'>128 × 128</b></p>
#     <p>Cell States <b style='float:right'>16</b></p>
#     <p>Fire Rate <b style='float:right'>0.50</b></p>
#     <p>LR <b style='float:right'>2e-3</b></p>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("")

#     st.markdown("<div class='card'><h4>Training Progress</h4>", unsafe_allow_html=True)

#     st.progress(100)
#     st.caption("500 / 500 Epochs")

#     st.progress(st.session_state.healing)
#     st.caption("Loss 0.0021")

#     st.markdown("</div>", unsafe_allow_html=True)

#     st.markdown("")

#     st.markdown("<div class='card'><h4>Activity Log</h4>", unsafe_allow_html=True)

#     for tm,msg in st.session_state.logs[:6]:
#         st.markdown(
#             f"<p style='font-size:14px;color:#cbd5e1'>{tm} &nbsp;&nbsp; {msg}</p>",
#             unsafe_allow_html=True
#         )

#     st.markdown("</div>", unsafe_allow_html=True)







import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Adaptive Neural Cellular Automata",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SESSION STATE
# =========================================================
if "signals" not in st.session_state:
    st.session_state.signals = 5

if "accuracy" not in st.session_state:
    st.session_state.accuracy = 95.2

if "healing" not in st.session_state:
    st.session_state.healing = 89

if "shape" not in st.session_state:
    st.session_state.shape = "Grow Heart"

if "logs" not in st.session_state:
    st.session_state.logs = [
        ("15:55", "Heart generated OK"),
        ("15:54", "Signal executed"),
        ("15:53", "Epoch 500 completed"),
        ("15:52", "Model loaded"),
    ]

# =========================================================
# PREMIUM CSS + ANIMATION
# =========================================================
st.markdown("""
<style>

html, body, [class*="css"]{
    font-family: 'Segoe UI', sans-serif;
}

body{
    background:#0a0d14;
}

.main{
    background:#0a0d14;
    color:white;
}

.block-container{
    padding-top:0rem;
    padding-left:0rem;
    padding-right:0rem;
    max-width:100%;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#10141f;
    border-right:1px solid rgba(255,255,255,0.05);
}

/* -------------------------------- */
/* ANIMATED CARD STYLE */
/* -------------------------------- */

.card, .metric{
    background:linear-gradient(145deg,#141928,#101522);
    border:1px solid rgba(255,255,255,0.06);
    border-radius:16px;
    padding:20px;
    position:relative;
    overflow:hidden;
    transition:all .35s ease;
}

/* neon top border */
.card::before,
.metric::before{
    content:"";
    position:absolute;
    top:0;
    left:0;
    width:100%;
    height:2px;
    background:linear-gradient(90deg,#38bdf8,#8b5cf6,#22c55e,#f59e0b);
}

/* hover */
.card:hover,
.metric:hover{
    transform:translateY(-6px) scale(1.015);
    box-shadow:0 15px 35px rgba(0,0,0,.45),
               0 0 20px rgba(56,189,248,.08);
    border:1px solid rgba(56,189,248,.28);
}

/* fade animation */
@keyframes fadeUp{
    from{
        opacity:0;
        transform:translateY(18px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

.card,.metric{
    animation:fadeUp .7s ease;
}

/* metric text */
.metric-title{
    color:#64748b;
    font-size:11px;
    letter-spacing:2px;
}

.metric-value{
    color:white;
    font-size:30px;
    font-weight:800;
    transition:.3s;
}

.metric:hover .metric-value{
    color:#38bdf8;
    transform:scale(1.04);
}

/* button */
.stButton>button{
    width:100%;
    height:50px;
    border:none;
    border-radius:12px;
    background:linear-gradient(90deg,#2563eb,#7c3aed);
    color:white;
    font-size:16px;
    font-weight:700;
}

/* select label */
.stSelectbox label{
    color:#94a3b8 !important;
}

/* progress */
div[data-testid="stProgressBar"] > div > div{
    background:linear-gradient(90deg,#38bdf8,#8b5cf6);
}

header{visibility:hidden;}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.markdown("## 🧠 NCA Controls")

signal = st.sidebar.selectbox(
    "Choose Action",
    [
        "Grow Heart",
        "Grow Gecko",
        "Grow Emoji",
        "Heal",
        "Damage",
        "Analytics"
    ]
)

run = st.sidebar.button("🚀 Execute Signal")

st.sidebar.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
st.sidebar.success("● Dashboard")

# =========================================================
# BUTTON FUNCTION
# =========================================================
if run:
    st.session_state.shape = signal
    st.session_state.signals += 1
    st.session_state.accuracy = round(np.random.uniform(92,98),1)
    st.session_state.healing = int(np.random.uniform(84,98))

    tm = datetime.now().strftime("%H:%M")
    st.session_state.logs.insert(0,(tm,f"{signal} signal executed"))

# =========================================================
# HEADER
# =========================================================
h1,h2,h3 = st.columns([8,1,1])

with h1:
    st.markdown("""
    <div style='padding:18px 28px'>
    <h1 style='font-size:34px;margin-bottom:0'>🧬 Adaptive Neural Cellular Automata</h1>
    <p style='color:#64748b;margin-top:5px;font-size:16px'>
    Self-Healing Morphogenesis with AI Signals
    </p>
    </div>
    """, unsafe_allow_html=True)

with h2:
    st.markdown("""
    <div style='margin-top:28px;
    background:#052e16;
    color:#22c55e;
    padding:8px 15px;
    border-radius:20px;
    text-align:center;
    font-weight:700'>
    ● LIVE
    </div>
    """, unsafe_allow_html=True)

with h3:
    st.markdown("""
    <div style='margin-top:28px;
    background:#7c3aed;
    color:white;
    padding:8px 15px;
    border-radius:10px;
    text-align:center;
    font-weight:700'>
    Deploy
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# METRICS
# =========================================================
m1,m2,m3,m4 = st.columns(4)

metrics = [
    ("Accuracy",f"{st.session_state.accuracy}%"),
    ("Signals",st.session_state.signals),
    ("Healing",f"{st.session_state.healing}%"),
    ("Epochs","500")
]

for col,(title,val) in zip([m1,m2,m3,m4],metrics):
    with col:
        st.markdown(f"""
        <div class='metric'>
            <div class='metric-title'>{title.upper()}</div>
            <div class='metric-value'>{val}</div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# SHAPE FUNCTIONS
# =========================================================
def draw_heart():
    x=np.linspace(-2,2,400)
    y=np.linspace(-2,2,400)
    X,Y=np.meshgrid(x,y)
    Z=(X**2+Y**2-1)**3 - X**2*Y**3

    fig,ax=plt.subplots(figsize=(10,5))
    fig.patch.set_facecolor("#080b13")
    ax.set_facecolor("#080b13")
    ax.contourf(X,Y,Z,levels=[-1,0],colors=["#ef4444"])
    ax.axis("off")
    st.pyplot(fig,use_container_width=True)

def draw_gecko(color=[0,1,0]):
    img=np.zeros((420,800,3))
    img[150:280,360:440]=color
    img[120:170,240:560]=color
    img[280:360,340:370]=color
    img[280:360,430:460]=color
    st.image(img,use_container_width=True)

def draw_emoji():
    fig,ax=plt.subplots(figsize=(7,5))
    fig.patch.set_facecolor("#080b13")
    ax.set_facecolor("#080b13")
    c=plt.Circle((0,0),1,color="gold")
    ax.add_patch(c)
    ax.plot([-0.35,0.35],[0.35,0.35],'ko',markersize=12)
    t=np.linspace(-1,1,100)
    ax.plot(t,-0.4+0.25*(1-t**2),color='black',linewidth=4)
    ax.axis("off")
    ax.set_xlim(-1.4,1.4)
    ax.set_ylim(-1.3,1.3)
    st.pyplot(fig,use_container_width=True)

def analytics():
    x=[0,50,100,150,200,250,300,400,500]
    y=[45,18,8,5,3,2.2,1.8,1.3,1]

    fig,ax=plt.subplots(figsize=(10,5))
    fig.patch.set_facecolor("#080b13")
    ax.set_facecolor("#080b13")
    ax.plot(x,y,color="#38bdf8",linewidth=3,marker='o')
    ax.tick_params(colors='white')
    ax.set_title("Training Loss Curve",color="white")
    st.pyplot(fig,use_container_width=True)

# =========================================================
# MAIN GRID
# =========================================================
left,right = st.columns([3.5,1.2])

with left:

    st.markdown("<div class='card'><h3>Morphogenesis Canvas</h3>", unsafe_allow_html=True)

    if run:
        with st.spinner("Executing Signal..."):
            time.sleep(1)

    shape = st.session_state.shape

    if shape=="Grow Heart":
        draw_heart()

    elif shape=="Grow Gecko":
        draw_gecko()

    elif shape=="Damage":
        draw_gecko([1,0,0])

    elif shape=="Heal":
        draw_gecko([0,0.8,1])

    elif shape=="Grow Emoji":
        draw_emoji()

    elif shape=="Analytics":
        analytics()

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# RIGHT PANEL
# =========================================================
with right:

    st.markdown(f"""
    <div class='card'>
    <h4>Signal Parameters</h4>
    <p>Target Shape <b style='float:right'>{shape}</b></p>
    <p>Grid Size <b style='float:right'>128 × 128</b></p>
    <p>Cell States <b style='float:right'>16</b></p>
    <p>Fire Rate <b style='float:right'>0.50</b></p>
    <p>LR <b style='float:right'>2e-3</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    st.markdown("<div class='card'><h4>Training Progress</h4>", unsafe_allow_html=True)
    st.progress(100)
    st.caption("500 / 500 Epochs")

    st.progress(st.session_state.healing)
    st.caption("Loss 0.0021")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("")

    st.markdown("<div class='card'><h4>Activity Log</h4>", unsafe_allow_html=True)

    for tm,msg in st.session_state.logs[:6]:
        st.markdown(
            f"<p style='font-size:14px;color:#cbd5e1'>{tm} &nbsp;&nbsp; {msg}</p>",
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)