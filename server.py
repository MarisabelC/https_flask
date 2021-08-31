from flask import Flask, jsonify

app = Flask(__name__)
ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return 'Flask is running!'


@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}

    return jsonify(data)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', ssl_context=('cert.pem', 'key.pem'))
