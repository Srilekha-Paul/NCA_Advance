import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from styles import load_css
from ui import metric_card

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Adaptive Neural Cellular Automata",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(load_css(), unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================

if "steps" not in st.session_state:
    st.session_state.steps = 0

if "accuracy" not in st.session_state:
    st.session_state.accuracy = 77.95

if "logs" not in st.session_state:
    st.session_state.logs = ["System initialized", "NCA engine ready"]

if "state" not in st.session_state:
    st.session_state.state = np.random.rand(64, 64)

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.markdown("# 🧠 Controls")

    organism = st.selectbox(
        "Choose Organism",
        ["heart", "tree", "brain", "flower", "butterfly"]
    )

    st.markdown("---")

    if st.button("🚀 Grow"):
        st.session_state.steps += 1
        st.session_state.accuracy = min(99.9, st.session_state.accuracy + np.random.uniform(0.2, 1.2))
        st.session_state.logs.append(f"Growth iteration {st.session_state.steps} completed")
        st.session_state.state = np.random.rand(64,64)

    if st.button("💥 Damage"):
        st.session_state.logs.append("Cell damage simulated")
        st.session_state.accuracy -= np.random.uniform(1,3)

    if st.button("💊 Heal"):
        st.session_state.logs.append("Self-healing activated")
        st.session_state.accuracy += np.random.uniform(1,2)

    if st.button("🔄 Reset"):
        st.session_state.steps = 0
        st.session_state.accuracy = 77.95
        st.session_state.logs = ["System reset"]
        st.session_state.state = np.random.rand(64,64)

    st.markdown("---")

    iterations = st.slider(
        "Iterations",
        1,
        100,
        20
    )

# =========================
# HEADER
# =========================

st.markdown('<div class="main-title">🧬 Adaptive Neural Cellular Automata</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Production Grade Research Visualization Dashboard</div>', unsafe_allow_html=True)

# =========================
# METRICS
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    metric_card("Steps", st.session_state.steps)

with col2:
    metric_card("Accuracy", f"{st.session_state.accuracy:.2f}%")

with col3:
    metric_card("Target", organism.upper())

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# MAIN CONTENT
# =========================

left, right = st.columns([4, 1.2])

with left:

    st.markdown("### 🧪 Organism Simulation")

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.imshow(
        st.session_state.state,
        cmap="magma"
    )

    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_title(
        organism.upper(),
        fontsize=22,
        color="white",
        pad=15,
        fontweight="bold"
    )

    fig.patch.set_facecolor('#0b1120')
    ax.set_facecolor('#0b1120')

    st.pyplot(fig, use_container_width=True)

with right:

    st.markdown("### 📜 Logs")

    st.markdown('<div class="log-box">', unsafe_allow_html=True)

    for log in reversed(st.session_state.logs[-8:]):
        st.write(f"• {log}")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 📈 Progress")

    progress = min(int(st.session_state.accuracy), 100)

    st.progress(progress)

    st.caption("Shape Match Accuracy")

# =========================
# FOOTER
# =========================

st.markdown(
    '''
    <div class="footer">
        Version 2.0 • Publishable Neural Cellular Automata Research Prototype<br>
        Built with Streamlit + PyTorch
    </div>
    ''',
    unsafe_allow_html=True
)




# # app.py

# import streamlit as st
# import torch
# import time

# from advanced_model import NeuralCA
# from utils import make_seed, plot_tensor, damage_tensor, calc_accuracy
# from targets import make_target_tensor

# # =====================================================
# # PAGE CONFIG
# # =====================================================
# st.set_page_config(
#     page_title="NCA Version 2",
#     page_icon="🧬",
#     layout="wide"
# )

# # =====================================================
# # SESSION STATE
# # =====================================================
# if "model" not in st.session_state:
#     model = NeuralCA()
#     try:
#         model.load_state_dict(
#             torch.load("saved/best_model.pth", map_location="cpu")
#         )
#     except:
#         pass
#     model.eval()
#     st.session_state.model = model

# if "state" not in st.session_state:
#     st.session_state.state = make_seed()

# if "steps" not in st.session_state:
#     st.session_state.steps = 0

# if "logs" not in st.session_state:
#     st.session_state.logs = ["System Ready"]

# # =====================================================
# # SIDEBAR
# # =====================================================
# st.sidebar.title("🧠 Controls")

# shape = st.sidebar.selectbox(
#     "Choose Organism",
#     ["heart", "gecko", "emoji"]
# )

# grow = st.sidebar.button("🚀 Grow")
# damage = st.sidebar.button("💥 Damage")
# heal = st.sidebar.button("🩹 Heal")
# reset = st.sidebar.button("🔄 Reset")

# iters = st.sidebar.slider("Iterations", 1, 50, 20)

# target = make_target_tensor(shape)

# # =====================================================
# # ACTIONS
# # =====================================================
# if reset:
#     st.session_state.state = make_seed()
#     st.session_state.steps = 0
#     st.session_state.logs.insert(0, "Grid Reset")

# if grow:
#     for _ in range(iters):
#         with torch.no_grad():
#             st.session_state.state = st.session_state.model(
#                 st.session_state.state
#             )
#         st.session_state.steps += 1

# if damage:
#     st.session_state.state = damage_tensor(
#         st.session_state.state,
#         "center"
#     )
#     st.session_state.logs.insert(0, "Damage Applied")

# if heal:
#     for _ in range(iters):
#         with torch.no_grad():
#             st.session_state.state = st.session_state.model(
#                 st.session_state.state
#             )
#         st.session_state.steps += 1

# # =====================================================
# # METRICS
# # =====================================================
# acc = calc_accuracy(
#     st.session_state.state,
#     target
# )

# # =====================================================
# # UI
# # =====================================================
# st.title("🧬 Adaptive Neural Cellular Automata V2")
# st.caption("PyTorch CPU Edition • Self Growing AI Organisms")

# c1, c2, c3 = st.columns(3)

# c1.metric("Steps", st.session_state.steps)
# c2.metric("Accuracy", f"{acc:.2f}%")
# c3.metric("Target", shape.upper())

# left, right = st.columns([3, 1])

# with left:
#     fig = plot_tensor(
#         st.session_state.state,
#         shape.upper()
#     )
#     st.pyplot(fig, use_container_width=True)

# with right:
#     st.subheader("Logs")

#     for log in st.session_state.logs[:8]:
#         st.write("•", log)

#     st.subheader("Progress")

#     st.progress(min(int(acc), 100))
#     st.caption("Shape Match")

# st.markdown("---")
# st.caption("Version 2 • Publishable NCA Research Prototype")







































# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# import time

# from model import SimpleNCA
# from targets import get_target
# from utils import damage_grid, render_grid, calc_similarity

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
# if "model" not in st.session_state:
#     st.session_state.model = SimpleNCA()

# if "grid" not in st.session_state:
#     st.session_state.grid = np.zeros((64, 64), dtype=np.float32)
#     st.session_state.grid[32, 32] = 1.0

# if "steps" not in st.session_state:
#     st.session_state.steps = 0

# if "target_name" not in st.session_state:
#     st.session_state.target_name = "Heart"

# if "logs" not in st.session_state:
#     st.session_state.logs = ["System initialized"]

# # =========================================================
# # SIDEBAR
# # =========================================================
# st.sidebar.title("🧠 Controls")

# shape = st.sidebar.selectbox(
#     "Choose Target",
#     ["Heart", "Gecko", "Emoji"]
# )

# grow = st.sidebar.button("🚀 Grow")
# damage = st.sidebar.button("💥 Damage")
# heal = st.sidebar.button("🩹 Heal")
# reset = st.sidebar.button("🔄 Reset")

# speed = st.sidebar.slider("Iterations", 1, 50, 15)

# # =========================================================
# # ACTIONS
# # =========================================================
# target = get_target(shape)

# if reset:
#     st.session_state.grid = np.zeros((64, 64), dtype=np.float32)
#     st.session_state.grid[32, 32] = 1.0
#     st.session_state.steps = 0
#     st.session_state.logs.insert(0, "Grid reset")

# if grow:
#     for _ in range(speed):
#         st.session_state.grid = st.session_state.model.update(
#             st.session_state.grid,
#             target
#         )
#         st.session_state.steps += 1
#     st.session_state.logs.insert(0, f"{shape} growth executed")

# if damage:
#     st.session_state.grid = damage_grid(st.session_state.grid)
#     st.session_state.logs.insert(0, "Damage applied")

# if heal:
#     for _ in range(speed):
#         st.session_state.grid = st.session_state.model.update(
#             st.session_state.grid,
#             target
#         )
#         st.session_state.steps += 1
#     st.session_state.logs.insert(0, "Healing completed")

# # =========================================================
# # HEADER
# # =========================================================
# st.title("🧬 Adaptive Neural Cellular Automata")
# st.caption("Self-Growing + Self-Healing Organisms with Local Intelligence")

# # =========================================================
# # METRICS
# # =========================================================
# sim = calc_similarity(st.session_state.grid, target)
# live_cells = int((st.session_state.grid > 0.2).sum())

# c1, c2, c3, c4 = st.columns(4)

# c1.metric("Steps", st.session_state.steps)
# c2.metric("Accuracy", f"{sim:.1f}%")
# c3.metric("Live Cells", live_cells)
# c4.metric("Target", shape)

# # =========================================================
# # MAIN LAYOUT
# # =========================================================
# left, right = st.columns([3, 1])

# with left:
#     fig = render_grid(st.session_state.grid, shape)
#     st.pyplot(fig, use_container_width=True)

# with right:
#     st.subheader("Activity Log")

#     for log in st.session_state.logs[:8]:
#         st.write("•", log)

#     st.subheader("Progress")

#     st.progress(min(int(sim), 100))
#     st.caption(f"Similarity: {sim:.2f}%")

#     st.progress(min(live_cells // 10, 100))
#     st.caption(f"Live Cells: {live_cells}")

# # =========================================================
# # FOOTER
# # =========================================================
# st.markdown("---")
# st.caption("Built with Streamlit + NumPy + Cellular Intelligence")























# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
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
#         ("15:53", "Epoch 500 completed"),
#         ("15:52", "Model loaded"),
#     ]

# # =========================================================
# # CSS
# # =========================================================
# st.markdown("""
# <style>
# html, body, [class*="css"]{
#     font-family: 'Segoe UI', sans-serif;
# }

# body, .main{
#     background:#0a0d14;
#     color:white;
# }

# .block-container{
#     padding-top:0rem;
#     padding-left:0rem;
#     padding-right:0rem;
#     max-width:100%;
# }

# section[data-testid="stSidebar"]{
#     background:#10141f;
#     border-right:1px solid rgba(255,255,255,0.05);
# }

# .card, .metric{
#     background:linear-gradient(145deg,#141928,#101522);
#     border:1px solid rgba(255,255,255,0.06);
#     border-radius:16px;
#     padding:20px;
#     position:relative;
#     overflow:hidden;
#     transition:all .35s ease;
# }

# .card::before,
# .metric::before{
#     content:"";
#     position:absolute;
#     top:0;
#     left:0;
#     width:100%;
#     height:2px;
#     background:linear-gradient(90deg,#38bdf8,#8b5cf6,#22c55e,#f59e0b);
# }

# .card:hover,
# .metric:hover{
#     transform:translateY(-4px);
#     box-shadow:0 15px 35px rgba(0,0,0,.45);
# }

# .metric-title{
#     color:#64748b;
#     font-size:11px;
#     letter-spacing:2px;
# }

# .metric-value{
#     color:white;
#     font-size:30px;
#     font-weight:800;
# }

# .stButton>button{
#     width:100%;
#     height:50px;
#     border:none;
#     border-radius:12px;
#     background:linear-gradient(90deg,#2563eb,#7c3aed);
#     color:white;
#     font-size:16px;
#     font-weight:700;
# }

# .stSelectbox label{
#     color:#94a3b8 !important;
# }

# div[data-testid="stProgressBar"] > div > div{
#     background:linear-gradient(90deg,#38bdf8,#8b5cf6);
# }

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
# # BUTTON ACTION
# # =========================================================
# if run:
#     st.session_state.shape = signal
#     st.session_state.signals += 1
#     st.session_state.accuracy = round(np.random.uniform(92, 98), 1)
#     st.session_state.healing = int(np.random.uniform(84, 98))

#     tm = datetime.now().strftime("%H:%M")
#     st.session_state.logs.insert(0, (tm, f"{signal} signal executed"))

# # =========================================================
# # HEADER
# # =========================================================
# h1, h2, h3 = st.columns([8,1,1])

# with h1:
#     st.markdown("""
#     <div style='padding:18px 28px'>
#         <h1 style='font-size:34px;margin-bottom:0'>
#         🧬 Adaptive Neural Cellular Automata
#         </h1>
#         <p style='color:#64748b;margin-top:5px;font-size:16px'>
#         Self-Healing Morphogenesis with AI Signals
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

# with h2:
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

# with h3:
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
# m1, m2, m3, m4 = st.columns(4)

# metrics = [
#     ("Accuracy", f"{st.session_state.accuracy}%"),
#     ("Signals", st.session_state.signals),
#     ("Healing", f"{st.session_state.healing}%"),
#     ("Epochs", "500")
# ]

# for col, (title, val) in zip([m1,m2,m3,m4], metrics):
#     with col:
#         st.markdown(f"""
#         <div class='metric'>
#             <div class='metric-title'>{title.upper()}</div>
#             <div class='metric-value'>{val}</div>
#         </div>
#         """, unsafe_allow_html=True)

# # =========================================================
# # SHAPE FUNCTIONS
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

# def draw_gecko(color="lime"):
#     fig, ax = plt.subplots(figsize=(12,6))
#     fig.patch.set_facecolor("#080b13")
#     ax.set_facecolor("#080b13")

#     # body
#     body = patches.Ellipse((0,0),4.2,2,color=color)
#     ax.add_patch(body)

#     # head
#     head = patches.Circle((2.5,0.2),0.75,color=color)
#     ax.add_patch(head)

#     # eye
#     eye = patches.Circle((2.75,0.45),0.08,color="black")
#     ax.add_patch(eye)

#     # tail
#     x=np.linspace(-5,-2,200)
#     y=0.35*np.sin(x*1.6)
#     ax.plot(x,y,color=color,linewidth=18,solid_capstyle="round")

#     # lower legs
#     ax.plot([-1.2,-2.2],[-0.5,-1.8],color=color,linewidth=9)
#     ax.plot([-0.3,-1.1],[-0.7,-2.0],color=color,linewidth=9)
#     ax.plot([1.0,2.0],[-0.4,-1.7],color=color,linewidth=9)
#     ax.plot([1.7,2.8],[-0.2,-1.5],color=color,linewidth=9)

#     # upper legs
#     ax.plot([1.0,2.0],[0.5,1.7],color=color,linewidth=9)
#     ax.plot([0.1,1.0],[0.7,1.9],color=color,linewidth=9)
#     ax.plot([-1.1,-2.1],[0.5,1.7],color=color,linewidth=9)
#     ax.plot([-0.2,-1.1],[0.7,1.9],color=color,linewidth=9)

#     ax.set_xlim(-6,5)
#     ax.set_ylim(-3,3)
#     ax.axis("off")

#     st.pyplot(fig,use_container_width=True)

# def draw_emoji(mode="happy"):
#     fig, ax = plt.subplots(figsize=(7,5))
#     fig.patch.set_facecolor("#080b13")
#     ax.set_facecolor("#080b13")

#     # Face
#     face = plt.Circle((0,0),1,color="gold")
#     ax.add_patch(face)

#     # Eyes
#     ax.plot([-0.35,0.35],[0.35,0.35],'ko',markersize=12)

#     # HAPPY MOUTH
#     t = np.linspace(-0.55,0.55,200)
#     y = -0.45 + 0.45*(1 - (t/0.55)**2)

#     ax.plot(t,y,color="black",linewidth=5)

#     ax.set_xlim(-1.4,1.4)
#     ax.set_ylim(-1.2,1.2)
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
# left,right = st.columns([3.5,1.2])

# with left:
#     st.markdown("<div class='card'><h3>Morphogenesis Canvas</h3>", unsafe_allow_html=True)

#     if run:
#         with st.spinner("Executing Signal..."):
#             time.sleep(1)

#     shape = st.session_state.shape

#     if shape=="Grow Heart":
#         draw_heart()

#     elif shape=="Grow Gecko":
#         draw_gecko("lime")

#     elif shape=="Damage":
#         draw_gecko("red")

#     elif shape=="Heal":
#         draw_gecko("cyan")

#     elif shape=="Grow Emoji":
#         draw_emoji()

#     elif shape=="Analytics":
#         analytics()

#     st.markdown("</div>", unsafe_allow_html=True)

# # =========================================================
# # RIGHT PANEL
# # =========================================================
# with right:

#     st.markdown(f"""
#     <div class='card'>
#     <h4>Signal Parameters</h4>
#     <p>Target Shape <b style='float:right'>{shape}</b></p>
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



# app.py

