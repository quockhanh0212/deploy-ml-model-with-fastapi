"""
Project: Deploy a ML Model to Cloud Application Platform with FastAPI
Author: quockhanh0212
Date: 2023-11-20
"""

import logging
import requests
import pickle
import yaml
import pandas as pd
from module.data import process_data
from module.model import inference

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Request to the Render server
url = "http://0.0.0.0:5000/infer"
[encoder, lb, model] = pickle.load(open("model/model.pkl", "rb"))

response = requests.post(
    url=url,
    json={
        "age": 52,
        "workclass": "Self-emp-not-inc",
        "fnlgt": 209642,
        "education": "HS-grad",
        "education-num": 9,
        "marital-status": "Married-civ-spouse",
        "occupation": "Exec-managerial",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "capital-gain": 0,
        "capital-loss": 0,
        "hours-per-week": 45,
        "native-country": "United-States"
    }
)
logger.info(f"Status code: {response.status_code}")
logger.info(response.json())
