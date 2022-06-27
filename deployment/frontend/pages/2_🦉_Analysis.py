#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image

from packages.page_config import set_page_config, create_sidebar


TITLE = "News Dataset Analysis"
IMG_LAPTOP = Image.open('assets/laptop-analyze.jpg')

# set page config
set_page_config(TITLE)

# create sidebar
create_sidebar()

col1, col2 = st.columns(2)
with col1:
    st.title(TITLE)
with col2:
    st.image(IMG_LAPTOP, width=300)

st.markdown("## Dataset Condition")
st.image(
    'assets/eda/dataset-label.png',
    caption='news label in the dataset',
)
st.markdown(
    """
    We have about equal number of news articles in each label,
    that means the dataset is balanced.
    """
)

st.markdown("## Subjects")
st.image(
    'assets/eda/news-subject.png',
    caption='news subjects',
)
st.markdown(
    """
    The above bar chart shows the total number of news grouped by subjects.
    It shows that fake news and real news have totally different subjects.

    This would make classification using too easy and might not be a good idea,
    since creator of fake news could use it to their advantage. It would also
    make our model to be biased.
    """
)

st.markdown("## Date")
st.image(
    'assets/eda/news-date.png',
    caption='number of news over time',
)
st.markdown(
    """
    We can see that the number of fake news have recently started to decrease, which is a good sign.
    The number of real news has also increased. This might also be in conjunction with the fact that 
    the election was over.
    The number of fake news started to increase at the start of 2016, the year of the election,
    and started to decrease gradually in 2017, after the election was over.

    This increases the evidence that news are often used as political propaganda.
    """
)

st.markdown("## Tweet Embedded News")
st.image(
    'assets/eda/news-tweet.png',
    caption='number of news which have embedded tweets',
)
st.markdown(
    """
    Though most news do not contain any tweets embedded, fake news have a higher tendency to have one compared to real news.
    This makes the data quite imbalanced, since there are clear characteristics that are leaning towards one label.

    According to this [kaggle research](https://www.kaggle.com/code/josutk/only-one-word-99-2#2),
    it could be caused by fake news sourcing their content from twitter.
    """
)

st.markdown("## Word Cloud")
col1, col2 = st.columns(2)
with col1:
    st.markdown("#### Fake News")
    st.image(
        'assets/eda/wordcloud-fake.png',
        caption='word cloud for fake news'
    )
with col2:
    st.markdown("#### Real News")
    st.image(
        'assets/eda/wordcloud-real.png',
        caption='word cloud for real news'
    )
st.markdown(
    """
    There does not seem to be a clear difference between fake news and real news.
    Both have a similar word cloud, with 'said', 'Donald Trump', and 'United State' being the most common words.
    This is because the dataset contains mostly news published during the election.
    """
)

st.markdown("## Number of Words in News")
st.markdown("#### Without Outliers")
col1, col2 = st.columns(2)
with col1:
    st.image(
        'assets/eda/news-words-box.png',
        width=300,
        caption='distribution of number of words per news without outliers'
    )
with col2:
    st.markdown(
        """
        Both fake and real news have about 400 words in their body of text.
        However, the first quartile for real news is lower than that of fake news.

        We need to take notes though, that we had the outliers hidden for that plot.

        Now let's show them
        """
    )

st.markdown("#### With Outliers")
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
    It's now a totally different story.

    Fake news dataset have a lot of outliers.
    That means, there are a couple fake news which have a lot more words compared to real news
    """
    )
with col2:
    st.image(
        'assets/eda/news-words-box-outlier.png',
        width=300,
        caption='distribution of number of words per news with outliers'
    )

st.markdown("## Number of Unique Words in News")
st.image(
    'assets/eda/news-unique-words.png',
    caption='number of unique words per news'
)
st.markdown(
    """
    The number of unique words in fake news is slightly higher than in real news
    """
)

st.markdown("## Gibberish Words in News")
st.image(
    'assets/eda/news-gibberish.png',
    caption='number of gibberish words per news'
)
st.markdown(
    """
    We found that there are a couple of gibberish words in a news.
    Words like `zzzzzzzz`, `zzuml`, `zzqvyk`, `zzpxelb`, `zzomtmd`, `zzn`, `zzll`, `zzjjpdaivn`, `zzg`, `zz`.
    Most of them are from fake news. This makes the data even more imbalanced.
    """
)