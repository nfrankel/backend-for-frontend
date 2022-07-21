from flask import jsonify, Flask
app = Flask(__name__)


products = [
  {
    'id': 1,
    'name': 'Stickers pack',
    'description': 'A pack of rad stickers to display on your laptop or wherever you feel like. Show your love for Apache APISIX'
  },
  {
    'id': 2,
    'name': 'Lapel pin',
    'description': 'With this \'Powered by Apache APISIX\' lapel pin, support your favorite API Gateway and let everybody know about it.'
  },
  {
    'id': 3,
    'name': 'Tee-Shirt',
    'description': 'The classic geek product! At a conference, at home, at work, this tee-shirt will be your best friend.'
  }
]

news = [
  {
    'title': 'Huge discount on all products', 'description': 'For a short time duration, you\'re entitled to a special discount ', 'start': 1658411677, 'end': 1689947677}
]

debug = {
  'version': '1.0',
  'build': '2b550565396595217103afa6dadc91317652a886/2732551010',
  'timestamp': 1658411677
}

@app.route("/products")
def get_products():
    """
    Get all products.

    @return: JSON array of products
    """
    return jsonify(products)


@app.route("/news")
def get_news():
    """
    Get all news.

    @return: JSON array of news
    """
    return jsonify(news)


@app.route("/info")
def info():
    """
    Get application info.

    @return: JSON object
    """
    return debug


@app.route("/")
def home():
    """
    Get an aggregate of all products, news and application info.

    @return: JSON object
    """
    return {
      'products': products,
      'news': news,
      'info': debug
  }
