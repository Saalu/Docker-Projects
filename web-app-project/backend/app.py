from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    return jsonify({
        'message': 'Hello from the API!',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)