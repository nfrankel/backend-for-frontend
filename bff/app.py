import os
import requests
from flask import Flask


app = Flask(__name__)

GATEWAY_ROOT = os.getenv('GATEWAY_ROOT')
print('GATEWAY_ROOT', GATEWAY_ROOT)

products_uri = GATEWAY_ROOT + '/products'
catalog_info_uri = GATEWAY_ROOT + '/catalog/info'
news_uri = GATEWAY_ROOT + '/news'
news_info_uri = GATEWAY_ROOT + '/news/info'


@app.route("/")
def home():
    """
    Get necessary data from both catalog and news endpoints.

    @return: JSON object
    """
    products = requests.get(products_uri).json()
    catalog_info = requests.get(catalog_info_uri).json()
    news = requests.get(news_uri).json()
    news_info = requests.get(news_info_uri).json()
    return {
      'products': products,
      'news': news,
      'info': {
          'catalog': catalog_info,
          'news': news_info
      }
    }
