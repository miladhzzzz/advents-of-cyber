import subprocess
from urllib.parse import urlparse
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def root():
    return jsonify({'yo': "nice to see you here"})

## Command injection
@app.route('/print', methods=['POST'])
def process_message():
    payload = request.get_json()
    message = payload.get('message')

    if message == None :
        return jsonify({'result': "you need a message in the body!"})

    # Introduce command injection vulnerability
    if ';' in message:
        return 'Invalid message', 400
    result = subprocess.check_output(f'echo {message}', shell=True)
    return jsonify({'result': result.decode()}), 200

## SSRF
WHITELISTED_DOMAINS = ['example.com', 'example.org']

@app.route('/api', methods=['POST'])
def api():
    url = request.form.get('url')
    if not is_whitelisted(url):
        return 'Access denied', 403

    response = request.get(url)
    return response.text

def is_whitelisted(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc in WHITELISTED_DOMAINS

if __name__ == '__main__':
    app.run(host="0.0.0.0" ,port=5000)