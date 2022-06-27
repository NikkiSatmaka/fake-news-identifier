#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import requests
from PIL import Image
import re

from packages.options import subject_options, subject_map

from packages.page_config import set_page_config, create_sidebar


TITLE = "Fake News Identifier"

# set page config
set_page_config(TITLE)

# create sidebar
create_sidebar()

msg_0_res = "Uh-Oh!! Fake News Alert!"
msg_0_act = "Seems like this news is fake!"
msg_0_add = "You might want to consider reading other news"
msg_1_res = "Seems like this news is real"
msg_1_act = "That's great. Enjoy your read"
msg_1_add = "A wine to accompany your read"
msg_goodluck = "Good Luck!"

img_crystal = Image.open('assets/crystal-ball.jpg')
img_res_0 = Image.open('assets/warning-careful.jpg')
img_res_1 = Image.open('assets/toast-wine.jpg')

# compile URL regex
url_regex = re.compile(r'https?:\S+|www\.\S+')

# URL = "http://127.0.0.1:5000/predict"  # for testing
URL = "https://news-detection-backend.herokuapp.com/predict"  # for deployment

col1, col2 = st.columns(2)
with col1:
    st.title(TITLE)
with col2:
    st.image(img_crystal, width=300)

# get user input
col1, col2 = st.columns(2)
with col1:
    subject_key = st.selectbox(
        "Subject",
        subject_options,
        index=0,
        help="Select the subject of the news article"
    )

with col2:
    date = st.date_input(
        "Date:",
        help='Select the date of the news article.'
    )

title = st.text_input(
    "Title:",
    help='Enter the title of the news article.',
    placeholder='Title of the news article.'
)

text = st.text_area(
    "Text:",
    help="Enter the text of the news article",
    placeholder="Body of the news article."
)

# make sure the input data has the format that the backend expects
subject = subject_map[subject_key]
date = str(date)

# store user input in a dictionary
data = {
    "title": title,
    "text": text,
    "subject": subject,
    "date": date,
}

# predict
predict = st.button("Predict")

with st.spinner('Predicting...'):
    # inferencing
    if not predict:
        st.stop()

    # check if all the fields are filled
    if not all(data.values()):
        st.error("Please fill all the fields.")
        st.stop()

    # check if title contains links
    if url_regex.search(title):
        st.error("Please remove links from the title")
        st.stop()

    # communicate
    r = requests.post(URL, json=data)
    res = r.json()

    if r.status_code == 200:
        result = res['result']['class_name']
        if result == 'Fake':
            st.warning(msg_0_res)
            st.subheader(msg_0_act)
            st.subheader(msg_goodluck)
            col1, col2, col3 = st.columns(3)
            with col2:
                st.write(msg_0_add)
                st.image(img_res_0, width=300)
        else:
            st.success(msg_1_res)
            st.subheader(msg_1_act)
            st.subheader(msg_goodluck)
            col1, col2, col3 = st.columns(3)
            with col2:
                st.write(msg_1_add)
                st.image(img_res_1, width=300)

    elif r.status_code == 400:
        st.title("There's an error in the input data!")
        st.write(res['message'])