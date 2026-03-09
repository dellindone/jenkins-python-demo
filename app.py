import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a Jenkins Python Demo.'

@app.route('/healthcheck')
def healthcheck():
    return 'OK', 200

if __name__ == '__main__':
    time.sleep(10)  # Simulate some startup time
    app.run(host='0.0.0.0', port=80)