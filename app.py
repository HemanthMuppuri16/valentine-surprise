import streamlit as st
import random

st.set_page_config(page_title="💘 Valentine Surprise", page_icon="💘")

HER_NAME = "Swetha"
YOUR_NAME = "Hemanth"

notes = [
    "You make my world brighter just by being in it.",
    "I’m grateful for you — today and always.",
    "You’re my favorite person, no matter what.",
    "Every day with you feels special.",
    "You are my happy place."
]

st.title(f"💘 Happy Valentine’s Day, {HER_NAME}!")
st.write("This link was made just for you 💌")

if st.button("💌 Open your love note"):
    st.success(random.choice(notes))

st.caption(f"— With love, {YOUR_NAME}")
