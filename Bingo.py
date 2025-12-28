import streamlit as st
import random
from PIL import Image, ImageDraw, ImageFont
import uuid
from textwrap import wrap

font = ImageFont.load_default()


if "possible_text" not in st.session_state:
    st.session_state.possible_text = []

st.title("Bingo maker")

st.title("Bingo Card Generator")

def get_wrapped_text(text, max_width, font=font):
    lines = ['']
    for word in text.split():
        line  = f'{lines[-1]} {word}'.strip()
        if font.getlength(line) <= max_width:
            lines[-1] = line
        else: 
            lines.append(word)
        
    return '\n'.join(lines)

def add_the_text():
    if st.session_state.new_text:
        st.session_state.possible_text.append({"id": str(uuid.uuid4()), "text": st.session_state.new_text})
        st.session_state.new_text = ""

st.text_input("What could happen?", key = "new_text", on_change=add_the_text)

line_points = [[(0, 100), (500, 100)], [(0, 200), (500, 200)], [(0,300), (500, 300)], [(0, 400), (500, 400)], [(100, 0), (100, 500)], [(200, 0), (200, 500)], [(300, 1), (300, 500)], [(400, 0), (400, 500)]]
text_positions = [(5, 5), (105, 5), (205, 5), (305, 5), (405, 5), (5, 105), (105, 105), (205, 105), (305, 105), (405, 105), (5, 205), (105, 205), (205, 205), (305, 205), (405, 205), (5, 305), (105, 305), (205, 305), (305, 305), (405, 305), (5, 405), (105, 405), (205, 405), (305, 405), (405, 405)]

if st.button("Generate Bingo Card"):
    if len(st.session_state.possible_text) < 25:
        st.warning("You need 25 items")
    else:
        bingo_card_items = random.sample(st.session_state.possible_text, 25)
        
        w, h = 500, 500
        img = Image.new("RGB", (w, h))

        img1 = ImageDraw.Draw(img)
        img1.rectangle([(0,0), (500, 500)], fill = "white")
        for lines in line_points:
            img1.line(lines, fill = "black", width = 10)
        for i in range(25):
            wrapped = get_wrapped_text(bingo_card_items[i]["text"], max_width = 48, font = font)
            img1.multiline_text(text_positions[i], wrapped, fill = "black", max_width = 48, max_height = 48)

        
        st.image(img, width = 500)


if "more_info_opened" not in st.session_state:
    st.session_state.more_info_opened = False

if "remove_list" not in st.session_state:
    st.session_state.remove_list = []

if st.button("More info"):
    st.session_state.more_info_opened = True
if st.session_state.more_info_opened:
    for text in st.session_state.possible_text.copy():
        st.write(text["text"])
        if st.button(f"Remove {text['text']}", key = f"remove{text['id']}"):
            st.session_state.remove_list.append(text["id"])
    if st.button("Close info"):
        for i in st.session_state.possible_text.copy():
            if i["id"] in st.session_state.remove_list:
                st.session_state.possible_text.remove(i)
        st.session_state.more_info_opened = False
