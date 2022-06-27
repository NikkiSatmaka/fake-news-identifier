#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st

from packages.profile import github_img, linkedin_img, instagram_img, stsi_book_img
from packages.profile import github_url, linkedin_url, instagram_url, book_url


TITLE = "Fake News Detection"

PAGE_ICON = '📰'
MENU_ITEMS = {
    'Get Help': 'https://github.com/NikkiSatmaka',
    'Report a bug': 'https://github.com/NikkiSatmaka',
    'About': f'**{TITLE}**',
}

# set page config
def set_page_config(page_title, page_icon=PAGE_ICON, menu_items=MENU_ITEMS):
    st.set_page_config(
        page_title = page_title,
        page_icon=page_icon,
        menu_items=menu_items,
    )

# create sidebar
def create_sidebar():
    with st.sidebar:
        st.markdown("Connect with me on")

        col1, col2 = st.columns(2)
        with col1:
            st.image(github_img, width=50)
        with col2:
            st.markdown(github_url, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.image(linkedin_img, width=50)
        with col2:
            st.markdown(linkedin_url, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.image(instagram_img, width=50)
        with col2:
            st.markdown(instagram_url, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.image(stsi_book_img, width=50)
        with col2:
            st.markdown(book_url, unsafe_allow_html=True)
