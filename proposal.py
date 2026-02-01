import streamlit as st
from pathlib import Path

st.set_page_config(page_title="💍 One Question...", page_icon="💍", layout="centered")

# ---- Customize text here ----
HER_NAME = "My Love"
YOUR_NAME = "Your Name"
PHOTO_FILE = "US.jpg"   # change to "us.png" if needed

# Read query params (Streamlit compatible way)
try:
    params = st.query_params
    said_yes = params.get("yes", "0") == "1"
except Exception:
    # fallback for older versions
    params = st.experimental_get_query_params()
    said_yes = params.get("yes", ["0"])[0] == "1"

st.markdown(
    """
    <style>
      .big-title { font-size: 44px; font-weight: 800; text-align: center; margin-top: 8px; }
      .sub { text-align: center; font-size: 18px; opacity: 0.85; margin-bottom: 24px; }
      .center { display:flex; justify-content:center; }
      .card { border: 1px solid rgba(255,255,255,0.15); border-radius: 18px; padding: 20px; }
      .hint { text-align:center; font-size: 13px; opacity:0.7; margin-top: 10px; }
      button { cursor: pointer; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(f"<div class='big-title'>💍 {HER_NAME}, will you marry me?</div>", unsafe_allow_html=True)
st.markdown(f"<div class='sub'>A tiny website made by {YOUR_NAME} just for you 💘</div>", unsafe_allow_html=True)

if said_yes:
    st.success("SHE SAID YESSSS 💖💖💖")
    st.balloons()

    photo_path = Path(PHOTO_FILE)
    if photo_path.exists():
        st.image(str(photo_path), caption="Us ❤️", use_container_width=True)
    else:
        st.warning(
            f"I couldn't find **{PHOTO_FILE}** in the project folder.\n\n"
            "Add your photo to the repo (same folder as app.py) and redeploy."
        )

    st.markdown("<div class='center'><h2>🥰 Forever starts now.</h2></div>", unsafe_allow_html=True)

else:
    # Buttons area: "Yes" (works) + "No" (dodges cursor)
    st.components.v1.html(
        """
        <div class="card">
          <div class="center" style="gap: 16px; position: relative; height: 90px; align-items:center;">
            <button
              id="yesBtn"
              style="
                padding: 14px 26px; font-size: 18px; font-weight: 700;
                border-radius: 14px; border: none;
              "
              onclick="goYes()"
            >
              ✅ Yes
            </button>

            <button
              id="noBtn"
              style="
                padding: 14px 26px; font-size: 18px; font-weight: 700;
                border-radius: 14px; border: none;
                position: absolute; left: 58%; top: 22px;
              "
            >
              ❌ No
            </button>
          </div>
          <div class="hint">Try clicking “No” 😄</div>
        </div>

        <script>
          function goYes(){
            const url = new URL(window.location.href);
            url.searchParams.set("yes", "1");
            window.location.href = url.toString();
          }

          const noBtn = document.getElementById("noBtn");

          function moveNo(){
            // Move within a reasonable box around the buttons
            const minX = 40, maxX = 360;   // adjust if needed
            const minY = 0,  maxY = 55;

            const x = Math.floor(Math.random() * (maxX - minX + 1)) + minX;
            const y = Math.floor(Math.random() * (maxY - minY + 1)) + minY;

            noBtn.style.left = x + "px";
            noBtn.style.top  = y + "px";
          }

          // Dodge on hover + on mouse move near it
          noBtn.addEventListener("mouseenter", moveNo);
          document.addEventListener("mousemove", (e) => {
            const rect = noBtn.getBoundingClientRect();
            const dx = Math.abs(e.clientX - (rect.left + rect.width/2));
            const dy = Math.abs(e.clientY - (rect.top + rect.height/2));
            if (dx < 90 && dy < 60) moveNo();
          });
        </script>
        """,
        height=180
    )
