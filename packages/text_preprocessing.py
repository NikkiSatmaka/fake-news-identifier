#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Useful functions to preprocess text data
"""

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


def combine_text(data, combined_col, *args):
    """
    Combine text features into one feature

    Parameters
    ----------
    data : pandas.DataFrame
        Dataframe to process
    combined_col : str
        Name of feature for combined text
    *args :
        List of features to combine

    Returns
    -------
    pandas.DataFrame
        Dataframe with combined text

    """

    # validation check
    if data is None or combined_col is None:
        raise ValueError('`data` and `combined_col` must be specified')

    # validation check
    if combined_col in data:
        raise AttributeError(f'The feature `{combined_col}` already exist. Use new feature name')

    # prepare output data
    output_data = data.copy()

    # loop through features to combine
    for col in args:
        if combined_col not in output_data:
            output_data['news'] = output_data[col]
            output_data = output_data.drop([col], axis=1)
            continue
        output_data['news'] = output_data['news'] + '\n' + output_data[col]
        output_data = output_data.drop([col], axis=1)

    return output_data


def process_text(text, stopwords=set(stopwords.words('english')), stemmer=PorterStemmer()):
    """
    Process text for NLP

    Parameters
    ----------
    text : str
        Text to process
    stopwords : list-like
        List of stopwords
    stemmer : stemmer object

    Returns
    -------
    str
        processed text
    """
    
    # preprocess text
    processed_text = text.lower()  # convert to lowercase
    processed_text = re.sub(r"@[A-Za-z0-9_]+", " ", processed_text)  # remove mention
    processed_text = re.sub(r"#[A-Za-z0-9_]+", " ", processed_text)  # remove hashtags
    processed_text = re.sub(r"\n", " ", processed_text)  # remove newline
    processed_text = re.sub(r"http\S+", " ", processed_text)  # remove link
    processed_text = re.sub(r"www\S+", " ", processed_text)  # remove link
    processed_text = re.sub(r"[^A-Za-z\s]", " ", processed_text)  # remove non-alpha characters aside from whitespace

    # tokenize processed_text
    tokens = word_tokenize(processed_text)

    # remove stopwords
    text_stopped = [word for word in tokens if word not in stopwords]

    # stem text
    text_stemmed = [stemmer.stem(word) for word in text_stopped]

    return ' '.join(text_stemmed)