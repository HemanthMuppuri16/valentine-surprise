import streamlit as st
from pathlib import Path

# -----------------------------------
# Page setup
# -----------------------------------
st.set_page_config(
    page_title="💍 One Question...",
    page_icon="💍",
    layout="centered"
)

# ---- Customize here ----
HER_NAME = "Swetha"
YOUR_NAME = "Hemanth"
PHOTO_FILE = "US.jpg"   # place image in same folder


# -----------------------------------
# Read query params
# -----------------------------------
params = st.query_params
said_yes = params.get("yes", "0") == "1"


# -----------------------------------
# PINK THEME + HEARTS
# -----------------------------------
st.markdown(
    """
    <style>
      html, body {
        background: linear-gradient(180deg, #ffd6e8, #fff0f6);
      }

      .big-title {
        font-size: 46px;
        font-weight: 900;
        text-align: center;
        color: #c9184a;
        margin-top: 10px;
      }

      .sub {
        text-align: center;
        font-size: 18px;
        color: #7a284e;
        margin-bottom: 26px;
      }

      .card {
        border-radius: 20px;
        padding: 24px;
        background: rgba(255, 255, 255, 0.75);
        box-shadow: 0 8px 25px rgba(255, 105, 180, 0.35);
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
        opacity: 0.8;
        z-index: 0;
      }

      @keyframes floatUp {
        0% { transform: translateY(100vh) scale(1); opacity: 0; }
        10% { opacity: 1; }
        100% { transform: translateY(-10vh) scale(1.4); opacity: 0; }
      }
    </style>

    <script>
      function createHeart() {
        const heart = document.createElement("div");
        heart.className = "heart";
        heart.innerText = ["💖","💗","💘","💕","💞"][Math.floor(Math.random()*5)];
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.animationDuration = (4 + Math.random() * 4) + "s";
        heart.style.fontSize = (18 + Math.random() * 26) + "px";
        document.body.appendChild(heart);

        setTimeout(() => heart.remove(), 8000);
      }

      setInterval(createHeart, 300);
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
if said_yes:
    st.success("SHE SAID YES 💖💖💖")
    st.balloons()

    photo_path = Path(PHOTO_FILE)
    if photo_path.exists():
        st.image(str(photo_path), caption="Us 💞", use_container_width=True)
    else:
        st.warning(f"Add **{PHOTO_FILE}** next to app.py")

    st.markdown(
        "<div style='text-align:center;'><h2>💍 Forever starts now 💕</h2></div>",
        unsafe_allow_html=True
    )


# ===================================
# QUESTION SCREEN
# ===================================
else:
    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        if st.button("💖 YES 💖", use_container_width=True):
            st.query_params["yes"] = "1"
            st.rerun()

    st.components.v1.html(
        """
        <div class="card">
          <div style="position:relative; height:90px;">
            <button
              id="noBtn"
              style="
                position:absolute;
                left:50%;
                top:20px;
                padding:14px 26px;
                font-size:18px;
                font-weight:700;
                border-radius:14px;
                border:none;
                background:#ff4d6d;
                color:white;
                cursor:pointer;
              "
            >
              ❌ No
            </button>
          </div>
          <div class="hint">You can try… but destiny says YES 💘</div>
        </div>

        <script>
          const noBtn = document.getElementById("noBtn");

          function moveNo(){
            const x = Math.random() * 280;
            const y = Math.random() * 60;
            noBtn.style.left = x + "px";
            noBtn.style.top  = y + "px";
          }

          noBtn.addEventListener("mouseenter", moveNo);
          document.addEventListener("mousemove", (e) => {
            const r = noBtn.getBoundingClientRect();
            if (Math.abs(e.clientX - r.left) < 80 &&
                Math.abs(e.clientY - r.top) < 60) {
              moveNo();
            }
          });
        </script>
        """,
        height=170
    )

