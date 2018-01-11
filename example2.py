# example1.py
from flask import Flask
app = Flask(__name__, static_url_path="")

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
      app.run(host='0.0.0.0' , port=5000 )
