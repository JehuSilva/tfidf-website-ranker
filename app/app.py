# tf-idf API

# Basic packages
import os
from flask import Flask, jsonify, request

# Custom packages
from app.utils.scraper import Scrapper
from app.utils.tfidf_calculator import TfIdfCalculator

app = Flask(__name__)

@app.route('/tfidf')
def tfidf():
    article_url = request.args.get('url', None)
    limit = request.args.get('limit', None)
    if not article_url or not limit:
        return jsonify({'error': 'Invalid URL: Missing parameters'}), 400
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # Scrapping the article
    scrapper = Scrapper()
    article = scrapper.get_page_article(article_url)
    # Calculating the tfidf top features
    models_directory = os.path.dirname(os.path.realpath(__file__))+'/models/'
    tfidf_calculator = TfIdfCalculator(models_directory=models_directory)
    tfidf_calculator.load_models()
    tfidf = tfidf_calculator.calculate_tfidf(article=article, top_n=int(limit))
    return jsonify(tfidf), 200


