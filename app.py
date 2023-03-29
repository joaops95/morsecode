import logging
from flask import Flask, request

app = Flask(__name__)

# Configure logging to stdout
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

@app.route('/', methods=['GET', 'POST'])
def log_data():
    if request.method == 'GET':
        logging.info(f"Received GET request: {request}")
        return "Hello, World!"
    elif request.method == 'POST':
        data = request.get_data(as_text=True)
        logging.info(f"Received POST request: {request}, data: {data}")
        return "Data received!"
    else:
        logging.warning(f"Received request with unsupported HTTP method: {request}")
        return "Method not allowed!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')