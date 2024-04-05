from flask import Flask, jsonify, render_template, request
from datetime import datetime

app = Flask(__name__)

logs = []

@app.route('/ping', methods=['GET'])
def ping():
    logs.append({'timestamp': datetime.now(), 'route': '/ping', 'method': 'GET'})
    return jsonify({'resposta': 'pong'})

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    input = data['dados']
    logs.append({'timestamp': datetime.now(), 'route': '/echo', 'method': 'POST', 'user_input': input})
    return jsonify({'resposta': input})

@app.route('/dash')
def dash():
    logs.append({'timestamp': datetime.now(), 'method': request.method, 'route': request.path})
    return render_template('dashboard.html', logs=logs)

@app.route('/info')
def info():
    return jsonify(logs)

if __name__ == '__main__':
    app.run()