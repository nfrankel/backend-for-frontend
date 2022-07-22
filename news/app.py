from flask import jsonify, Flask
app = Flask(__name__)


debug = {
  'version': '2.0',
  'build': 'df8b944048bb6d628301a2feacbd7c9462209008',
  'timestamp': 1658412677
}


news = [
  {
    'title': 'Huge discount on all products',
    'description': 'For a short time duration, you\'re entitled to a special discount ',
    'start': 1658411677,
    'end': 1689947677
  }
]


@app.route("/info")
def info():
    """
    Get application info.

    @return: JSON object
    """
    return debug


@app.route("/news")
def get_news():
    """
    Get all news.

    @return: JSON array of news
    """
    return jsonify(news)
