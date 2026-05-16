
def load_css():
    return """
    <style>

    .stApp {
        background: linear-gradient(135deg, #050816 0%, #0b1120 100%);
        color: white;
        font-family: 'Inter', sans-serif;
    }

    section[data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.95);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    .main-title {
        font-size: 3rem;
        font-weight: 800;
        color: white;
        margin-bottom: 0;
    }

    .subtitle {
        color: #94a3b8;
        margin-top: 0;
        margin-bottom: 2rem;
    }

    .glass-card {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 1.2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    }

    .metric-card {
        background: linear-gradient(145deg,#111827,#1e293b);
        border-radius: 18px;
        padding: 20px;
        border: 1px solid rgba(255,255,255,0.08);
        transition: 0.3s ease;
    }

    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }

    .metric-label {
        color: #94a3b8;
        font-size: 0.95rem;
    }

    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: white;
    }

    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 48px;
        border: none;
        background: linear-gradient(135deg,#7c3aed,#2563eb);
        color: white;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: scale(1.02);
        background: linear-gradient(135deg,#8b5cf6,#3b82f6);
    }

    .log-box {
        background: #0f172a;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.06);
        max-height: 300px;
        overflow-y: auto;
    }

    .footer {
        text-align: center;
        color: #64748b;
        margin-top: 30px;
        font-size: 0.9rem;
    }

    </style>
    """


