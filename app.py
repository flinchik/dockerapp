from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Docker on DigitalOcean App Platform!"

@app.route('/status')
def status():
    return jsonify(status="App is running", code=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
