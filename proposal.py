import streamlit as st
from pathlib import Path
import time
import random

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
PHOTO_FILE = "US.JPG"   # exact filename (case-sensitive)

APP_DIR = Path(__file__).parent
PHOTO_PATH = APP_DIR / PHOTO_FILE

# -----------------------------------
# State
# -----------------------------------
if "said_yes" not in st.session_state:
    st.session_state.said_yes = False

if "yes_level" not in st.session_state:
    st.session_state.yes_level = 0

if "no_count" not in st.session_state:
    st.session_state.no_count = 0

# Optional: keep query param compatibility
params = st.query_params
if params.get("yes", "0") == "1":
    st.session_state.said_yes = True


# -----------------------------------
# Theme + floating hearts
# -----------------------------------
st.markdown(
    """
    <style>
      html, body {
        background: radial-gradient(circle at top, #ffe1ef 0%, #fff0f6 35%, #ffd6e8 100%);
      }

      .big-title {
        font-size: 52px;
        font-weight: 900;
        text-align: center;
        color: #c9184a;
        margin-top: 10px;
        letter-spacing: 0.3px;
        text-shadow: 0 8px 22px rgba(201, 24, 74, 0.25);
      }

      .sub {
        text-align: center;
        font-size: 18px;
        color: #7a284e;
        margin-bottom: 18px;
      }

      .card {
        border-radius: 22px;
        padding: 24px;
        background: rgba(255, 255, 255, 0.75);
        box-shadow: 0 10px 35px rgba(255, 105, 180, 0.35);
        border: 1px solid rgba(201, 24, 74, 0.15);
        backdrop-filter: blur(6px);
      }

      .hint {
        text-align:center;
        font-size: 13px;
        color:#9d4edd;
        margin-top: 10px;
      }

      .pill {
        display:inline-block;
        padding: 6px 12px;
        border-radius: 999px;
        background: rgba(201, 24, 74, 0.10);
        color: #a4133c;
        font-size: 13px;
        font-weight: 700;
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
        animation: fadeIn 700ms ease-out forwards;
        opacity: 0;
        transform: translateY(8px);
      }

      @keyframes fadeIn {
        to { opacity: 1; transform: translateY(0); }
      }

      .countdown {
        text-align:center;
        font-size: 18px;
        font-weight: 800;
        color: #c9184a;
        margin: 12px 0 6px;
      }
    </style>

    <script>
      function createHeart() {
        const heart = document.createElement("div");
        heart.className = "heart";
        heart.innerText = ["💖","💗","💘","💕","💞","💝"][Math.floor(Math.random()*6)];
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.animationDuration = (4 + Math.random() * 4) + "s";
        heart.style.fontSize = (16 + Math.random() * 28) + "px";
        document.body.appendChild(heart);
        setTimeout(() => heart.remove(), 8000);
      }
      setInterval(createHeart, 260);
    </script>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# Header
# -----------------------------------
st.markdown(f"<div class='big-title'>💍 {HER_NAME}, will you marry me?</div>", unsafe_allow_html=True)
st.markdown(f"<div class='sub'>A tiny pink universe made by {YOUR_NAME} just for you 💕</div>", unsafe_allow_html=True)


# ===================================
# YES SCREEN
# ===================================
if st.session_state.said_yes:
    st.success("SHE SAID YES 💖💖💖")
    st.balloons()

    # A cute countdown before reveal
    st.markdown("<div class='countdown fade-in'>Photo reveal in…</div>", unsafe_allow_html=True)
    counter = st.empty()
    for i in range(3, 0, -1):
        counter.markdown(f"<div class='countdown'>{i}…</div>", unsafe_allow_html=True)
        time.sleep(0.6)

    counter.markdown("<div class='countdown'>✨ NOW ✨</div>", unsafe_allow_html=True)

    if PHOTO_PATH.exists():
        st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
        st.image(str(PHOTO_PATH), caption="Us 💞", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning(f"Couldn't find **{PHOTO_FILE}** next to app.py")
        st.code(str(PHOTO_PATH))

    st.markdown("<div style='text-align:center;' class='fade-in'><h2>💍 Forever starts now 💕</h2></div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("🔁 Replay", use_container_width=True):
            st.session_state.said_yes = False
            st.session_state.yes_level = 0
            st.session_state.no_count = 0
            st.query_params["yes"] = "0"
            st.rerun()


# ===================================
# QUESTION SCREEN
# ===================================
else:
    # escalating YES messages
    yes_texts = [
        "💖 YES 💖",
        "💍 YES!! 💍",
        "😳 YES!!! 😳",
        "🥹 YESSSSS 🥹",
        "💘 OKAY YES 💘"
    ]
    prompts = [
        "Just one question…",
        "Think about it… 😌",
        "My heart is racing… 💓",
        "You’re really going to make me ask again? 😅",
        "Destiny is tapping your shoulder 💘"
    ]
    st.markdown(
        f"<div style='text-align:center; margin-bottom:10px;'><span class='pill'>{random.choice(prompts)}</span></div>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 1.2, 1])

    with col2:
        btn_label = yes_texts[min(st.session_state.yes_level, len(yes_texts)-1)]
        if st.button(btn_label, use_container_width=True):
            st.session_state.yes_level += 1
            # after a few clicks, lock it in (feels playful)
            if st.session_state.yes_level >= 2:
                st.session_state.said_yes = True
                st.query_params["yes"] = "1"
            st.rerun()

    # NO button as a mischievous runner (better bounds + click handling)
    # Also shows playful "no attempts" count.
    st.components.v1.html(
        f"""
        <div class="card">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <div style="font-weight:800; color:#a4133c;">Try clicking “No” 😈</div>
            <div style="font-size:12px; color:#7a284e;">No attempts: {st.session_state.no_count}</div>
          </div>

          <div id="arena" style="position:relative; height:120px; margin-top:10px; overflow:hidden;">
            <button
              id="noBtn"
              style="
                position:absolute;
                left:42%;
                top:46px;
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

            const maxX = Math.max(0, a.width - b.width - 10);
            const maxY = Math.max(0, a.height - b.height - 10);

            const x = Math.random() * maxX;
            const y = Math.random() * maxY;

            noBtn.style.left = x + "px";
            noBtn.style.top  = y + "px";
          }

          // runs away on hover and on click
          noBtn.addEventListener("mouseenter", moveNo);
          noBtn.addEventListener("click", (e) => {
            e.preventDefault();
            moveNo();
            // ping Streamlit to rerun by updating hash (tiny trick)
            window.location.hash = "no-" + Math.floor(Math.random()*100000);
          });

          // if cursor gets close, dodge
          arena.addEventListener("mousemove", (e) => {
            const r = noBtn.getBoundingClientRect();
            const dx = Math.abs(e.clientX - (r.left + r.width/2));
            const dy = Math.abs(e.clientY - (r.top  + r.height/2));
            if (dx < 110 && dy < 70) moveNo();
          });
        </script>
        """,
        height=240
    )

    # Track "No attempts" via URL hash change
    # When hash changes, Streamlit reruns; we can detect and count.
    # (Not perfect, but works well enough for this playful effect.)
    if st.session_state.get("last_hash") != st.experimental_get_query_params().get("hash", [""])[0]:
        st.session_state.last_hash = st.experimental_get_query_params().get("hash", [""])[0]

    # Cleaner: count no attempts using query params isn't reliable; instead provide a manual button:
    cA, cB, cC = st.columns([1, 1, 1])
    with cB:
        if st.button("I tried clicking No 🙃", use_container_width=True):
            st.session_state.no_count += 1
            st.rerun()
