import streamlit as st
import random
from PIL import Image, ImageDraw

if "possible_text" not in st.session_state:
    st.session_state.possible_text = []

st.title("Bingo maker")

st.title("Bingo Card Generator")

possible_text.append(new_text)
if st.button("Add new text"):
    new_text = st.text_input("What could happen?")

line_points = [[(0, 100), (500, 100)], [(0, 200), (500, 200)], [(0,300), (500, 300)], [(0, 400), (500, 400)], [(100, 0), (100, 500)], [(200, 0), (200, 500)], [(300, 1), (333.3333333333333, 500)], [(400, 0), (400, 500)]]
text_positions = [(50, 50), (150, 50), (250, 50), (350, 50), (450, 50), (50, 150), (150, 150), (250, 150), (350, 150), (450, 150), (50, 250), (150, 250), (250, 250), (350, 250), (450, 250), (50, 350), (150, 350), (250, 350), (350, 350), (450, 350), (50, 450), (150, 450), (250, 450), (350, 450), (450, 450)]

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
        for i in range(25):
            img1.text(text_positions[i], bingo_card_items[i], fill = "black")
        
        st.image(img, width = 500)
