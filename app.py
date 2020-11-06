
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/countries', methods=['get'])
def api():
    value = [
        {"country": "United States"},
        {"country": "Brazil"},
        {"country": "Mexico"},
        {"country": "Colombia"},
        {"country": "Argentina"},
        {"country": "Canada"},
        {"country": "Peru"},
        {"country": "Venezuela"},
        {"country": "Chile"},
        {"country": "Ecuador"},
        {"country": "Guatemala"},
        {"country": "Bolivia"},
        {"country": "Haiti"},
        {"country": "Panama"},
        {"country": "Uruguay"},
        {"country": "Russia"},
        {"country": "Ukraine"},
        {"country": "France"},
        {"country": "Spain"},
        {"country": "Sweden"},
        {"country": "Norway"},
        {"country": "Germany"},
        {"country": "Italy"},
        {"country": "United Kingdom"},
    ]

    return jsonify(value)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
