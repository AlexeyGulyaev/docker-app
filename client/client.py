from flask import Flask, json
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def index():
    try:
        data = requests.get('http://docker-app123_server_1:8080/info').json()
        # data = requests.get('http://127.0.0.1:5000/info').json()
    except requests.exceptions.ConnectionError:
        data = {'string': 'server not available now'}
    data['machine'] = 'client'
    response = app.response_class(
        response=json.dumps(data, sort_keys=False, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(port=5001, debug=True)
