from flask import jsonify, Flask
app = Flask(__name__)


debug = {
  'version': '2.0',
  'build': 'ed6b5669e072848c31edbd564cc56117fdd33943',
  'timestamp': 16584126793
}


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


@app.route("/info")
def info():
    """
    Get application info.

    @return: JSON object
    """
    return debug


@app.route("/products")
def get_products():
    """
    Get all products.

    @return: JSON array of products
    """
    return jsonify(products)
