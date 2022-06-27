#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image

from packages.page_config import set_page_config, create_sidebar


TITLE = 'Fake News Identifier'
LOGO = Image.open('assets/news.jpg')

# set page config
set_page_config(f"Home - {TITLE}")

# create sidebar
create_sidebar()

# Title of the main page
col1, col2 = st.columns(2)
with col1:
    st.image(LOGO, width=300)
with col2:
    st.title(TITLE)

st.header('Introduction')

st.markdown(
    """
    News and media is an important part of our daily lives. They're mainly used to spread information.
    Therefore, news could play an important part in our decision making as well. We might decide on which route to take to work,
    based on the news. We might decide on whether to shop now or what to buy, based on the news.
    
    This would mean that if one could control the news, they control the information, and potentially control our decision making and life choices.
    This is why news manipulation is a tool that's often used, especially during political campaigns.
    Therefore, it's important to monitor the news and filter whether the news that we're reading is fake

    This **Fake News Identifier** application is created to help you detect fake news.
    Using our state-of-the-art technology, we will be able to easily identify those fake news.

    Simply navigate to the [Prediction](/Prediction) page using the sidebar on the left and input the news you want to check.
    You will then find out whether you should read the news or not.

    Now you can feel safe when you read the news.
    Go to the [Prediction](/Prediction) page and check out the news before reading.
    """,
    unsafe_allow_html=True
)