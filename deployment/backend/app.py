#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify

import numpy as np
import pandas as pd
from pathlib import Path

from tensorflow import keras

from packages.imputation_handling import drop_missing_news
from packages.text_preprocessing import combine_text
from packages.text_preprocessing import clean_text
from packages.text_preprocessing import lemmatize_text

app = Flask(__name__)

# initiate model & columns
LABEL = ["Fake", "Real"]

# set threshold for prediction
THRESHOLD = 0.5

# model location
model_dir = 'models'
model_name = 'nlp_model'

# create path object
model_path = Path(model_dir, model_name)

# load model
model = keras.models.load_model(model_path)

@app.route("/")
def welcome():
    return "<h3>This is the Backend for My Modeling Program</h3>"

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method != "POST":
        # return from get method
        return "<p>Please use the POST method to predict <em>inference model</em></p>"

    content = request.json
    try:
        # create dictionary to store input data
        new_data = {
            "title": content["title"],
            "text": content["text"],
            "subject": content["subject"],
            "date": content["date"],
        }

        # convert to dataframe
        new_data = pd.DataFrame([new_data])

        # drop missing news
        prepared_data = drop_missing_news(new_data, date_col='date', variable=['title'])

        # combine title and text features as news
        combined_data = combine_text(prepared_data, 'news', 'title', 'text')

        # keep only the news feature as the only text to process
        combined_data = combined_data['news']

        # clean text
        cleaned_data = combined_data.apply(clean_text)

        # lemmatize text
        lemmatized_data = cleaned_data.apply(lemmatize_text)

        # predict and store result
        res = model.predict(lemmatized_data).reshape(-1)
        res = np.where(res > THRESHOLD, 1, 0)

        # convert result to dictionary
        result = {
            "class": str(res[0]),
            "class_name": LABEL[res[0]]
        }

        # jsonify result
        response = jsonify(
            success=True,
            result=result
        )

        # return response
        return response, 200

    except Exception as e:
        response = jsonify(
            success=False,
            message=str(e)
        )

        # return response
        return response, 400

# app.run(debug=True)
