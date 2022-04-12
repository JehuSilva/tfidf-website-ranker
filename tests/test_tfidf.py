# Testing the tfidf endpoint

from app.app import app
from flask import json
import pytest

def test_tfidf():
    # Capture sklearn warnings
    with pytest.warns(FutureWarning):
        response = app.test_client().get('/tfidf',query_string = {
                'url':'https://en.wikipedia.org/wiki/Donald_Trump',
                'limit':'2'
            }
        )
    # Check if the response is valid
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data == {
        "terms": [
            {
                "term": "retrieved",
                "tf-idf": 0.664
            },
            {
                "term": "2021",
                "tf-idf": 0.39
            }
        ]
    }