import streamlit as st
import requests
import time
import os

st.title("Stickman Video Generator")
prompt = st.text_input("Enter your stickman video idea:")

if st.button("Generate Video"):
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        st.info("Generating your stickman video...")
        time.sleep(3)
        st.success("Video ready!")
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")
