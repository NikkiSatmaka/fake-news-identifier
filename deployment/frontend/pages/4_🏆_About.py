#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st

from packages.page_config import set_page_config

from packages.profile import profile, github_img, linkedin_img, instagram_img, stsi_book_img
from packages.profile import github_url, linkedin_url, instagram_url, book_url


TITLE = "About Me"

# set page config
set_page_config(TITLE)

# Title of the main page
st.title(TITLE)

col1, col2 = st.columns(2)
col1.image(profile, width=300)

col2.markdown(
    """
    I'm Nikki Satmaka, a Data Scientist, Financial Market Practitioner and Analyst,
    Quantitave Finance Enthusiast. I'm a Co-Author of "Simple Trading Simple Investing"
    together with Ryan Filbert's Team.

    I can help you provide insights from data especially regarding the financial markets.
    This app is a sample portfolio of mine to display what you can do with data, computer,
    and a bit of imagination.
    """
)

st.markdown("--------------------")
st.markdown("Connect with me on")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image(github_img, width=50)
    st.markdown(github_url, unsafe_allow_html=True)

with col2:
    st.image(linkedin_img, width=50)
    st.markdown(linkedin_url, unsafe_allow_html=True)

with col3:
    st.image(instagram_img, width=50)
    st.markdown(instagram_url, unsafe_allow_html=True)

with col4:
    st.image(stsi_book_img, width=50)
    st.markdown(book_url, unsafe_allow_html=True)