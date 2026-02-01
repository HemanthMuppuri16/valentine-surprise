import streamlit as st
from pathlib import Path
import time

# -----------------------------------
# Page setup
# -----------------------------------
st.set_page_config(
    page_title="💍 One Question...",
    page_icon="💍",
    layout="centered"
)

# -----------------------------------
# Customize
# -----------------------------------
HER_NAME = "Swetha"
YOUR_NAME = "Hemanth"
PHOTO_FILE = "US.JPG"

APP_DIR = Path(__file__).parent
PHOTO_PATH = APP_DIR / PHOTO_FILE

# -----------------------------------
# Session state
# -----------------------------------
if "said_yes" not in st.session_state:
    st.session_state.said_yes = False

# -----------------------------------
# Theme + floating hearts
# -----------------------------------
st.markdown(
    """
    <style>
      html, body {
        background: radial-gradient(circle at top, #ffe1ef 0%, #fff0f6 40%, #ffd6e8 100%);
      }

      .big-title {
        font-size: 52px;
        font-weight: 900;
        text-align: center;
        color: #c9184a;
        margin-top: 10px;
        text-shadow: 0 8px 22px rgba(201, 24, 74, 0.25);
      }

      .sub {
        text-align: center;
        font-size: 18px;
        color: #7a284e;
        margin-bottom: 22px;
      }

      .card {
        border-radius: 22px;
        padding: 24px;
        background: rgba(255, 255, 255, 0.75);
        box-shadow: 0 10px 35px rgba(255, 105, 180, 0.35);
        border: 1px solid rgba(201, 24, 74, 0.15);
      }

      .hint {
        text-align:center;
        font-size: 13px;
        color:#9d4edd;
        margin-top: 10px;
      }

      .heart {
        position: fixed;
        font-size: 22px;
        animation: floatUp linear infinite;
        opacity: 0.85;
        z-index: 0;
        pointer-events: none;
      }

      @keyframes floatUp {
        0% { transform: translateY(110vh) scale(0.8); opacity: 0; }
        10% { opacity: 1; }
        100% { transform: translateY(-10vh) scale(1.4); opacity: 0; }
      }

      .fade-in {
        animation: fadeIn 800ms ease-out forwards;
        opacity: 0;
      }

      @keyframes fadeIn {
        to { opacity: 1; }
      }
    </style>

    <script>
      function createHeart() {
        const heart = document.createElement("div");
        heart.className = "heart";
        heart.innerText = ["💖","💗","💘","💕","💞","💝"][Math.floor(Math.random()*6)];
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.animationDuration = (4 + Math.random() * 4) + "s";
        heart.style.fontSize = (18 + Math.random() * 26) + "px";
        document.body.appendChild(heart);
        setTimeout(() => heart.remove(), 8000);
      }
      setInterval(createHeart, 280);
    </script>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# Header
# -----------------------------------
st.markdown(
    f"<div class='big-title'>💍 {HER_NAME}, will you marry me?</div>",
    unsafe_allow_html=True
)
st.markdown(
    f"<div class='sub'>A tiny pink universe made by {YOUR_NAME} just for you 💕</div>",
    unsafe_allow_html=True
)

# ===================================
# YES SCREEN
# ===================================
if st.session_state.said_yes:
    st.success("SHE SAID YES 💖💖💖")
    st.balloons()

    countdown = st.empty()
    for i in range(3, 0, -1):
        countdown.markdown(f"<h3 style='text-align:center;color:#c9184a;'>{i}…</h3>", unsafe_allow_html=True)
        time.sleep(0.6)

    countdown.markdown("<h3 style='text-align:center;color:#c9184a;'>✨ FOREVER ✨</h3>", unsafe_allow_html=True)

    if PHOTO_PATH.exists():
        st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
        st.image(str(PHOTO_PATH), caption="Us 💞", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error(f"Image not found: {PHOTO_FILE}")

    st.markdown(
        "<div style='text-align:center;' class='fade-in'><h2>💍 Forever starts now 💕</h2></div>",
        unsafe_allow_html=True
    )

    if st.button("🔁 Replay"):
        st.session_state.said_yes = False
        st.rerun()

# ===================================
# QUESTION SCREEN
# ===================================
else:
    col1, col2, col3 = st.columns([1, 1.2, 1])

    with col2:
        if st.button("💖 YES 💖", use_container_width=True):
            st.session_state.said_yes = True
            st.rerun()

    st.components.v1.html(
        """
        <div class="card">
          <div id="arena" style="position:relative; height:120px; margin-top:10px; overflow:hidden;">
            <button
              id="noBtn"
              style="
                position:absolute;
                left:40%;
                top:44px;
                padding:14px 26px;
                font-size:18px;
                font-weight:800;
                border-radius:14px;
                border:none;
                background:#ff4d6d;
                color:white;
                cursor:pointer;
                box-shadow: 0 10px 25px rgba(255, 77, 109, 0.35);
              "
            >
              ❌ No
            </button>
          </div>
          <div class="hint">You can try… but destiny says YES 💘</div>
        </div>

        <script>
          const noBtn = document.getElementById("noBtn");
          const arena = document.getElementById("arena");

          function moveNo(){
            const a = arena.getBoundingClientRect();
            const b = noBtn.getBoundingClientRect();

            const maxX = a.width - b.width - 10;
            const maxY = a.height - b.height - 10;

            const x = Math.random() * maxX;
            const y = Math.random() * maxY;

            noBtn.style.left = x + "px";
            noBtn.style.top  = y + "px";
          }

          noBtn.addEventListener("mouseenter", moveNo);
          noBtn.addEventListener("click", (e) => {
            e.preventDefault();
            moveNo();
          });
        </script>
        """,
        height=220
    )
