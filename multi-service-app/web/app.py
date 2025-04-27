from flask import Flask
import redis
import os

app = Flask(__name__)
redis_client = redis.Redis(
    host=os.getenv('REDIS_HOST', 'redis'),
    port=os.getenv('REDIS_PORT', 6379),
    db=0
)

@app.route('/')
def counter():
    try:
        count = redis_client.incr('hits')
        return f'''Hello, this is Room-3, the Power Team .
                This page has been viewed {count} times!'''
    except Exception as e:
        return f'Error connecting to Redis: {str(e)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)