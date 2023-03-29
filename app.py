from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def log_data():
    data = request.get_data(as_text=True)
    print(f"Received data: {data}")
    return "Data received!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')