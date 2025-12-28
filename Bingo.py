import streamlit as st
import numpy as np
import random
from PIL import Image, ImageDraw

if "possible_text" not in st.session_state:
    st.session_state.possible_text = []
possible_text = []

st.title("Bingo maker")

st.title("Bingo Card Generator")

if st.button("Add new text"):
    new_text = st.text_input("What could happen?")
    possible_text.append(new_text)

line_points = [[(0, 100), (500, 100)], [(0, 200), (500, 200)], [(0,300), (500, 300)], [(0, 400), (500, 400)], [(100, 0), (100, 500)], [(200, 0), (200, 500)], [(300, 1), (333.3333333333333, 500)], [(400, 0), (400, 500)]]

if st.button("Generate Bingo Card"):
    if len(st.session_state.possible_text) < 25:
        st.warning("You need 25 items")
    else:
        bingo_card_items = random.sample(st.session_state.possible_text, 25)
        
        w, h = 500, 500
        img = Image.new("RGB", (w, h))

        img1 = ImageDraw.Draw(img)
        for line in line_points:
            img1.line(line, fill = "black", width = 10)
        st.image(img, width = 500)
