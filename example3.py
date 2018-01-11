# example1.py
from flask import Flask , request , jsonify
app = Flask(__name__, static_url_path="")

name="Steven"
@app.route('/', methods=['GET'])
def index():
    return "Hello, {}!".format( name  )

@app.route('/', methods=['POST'])
def set_name():
    global name
    name =  request.get_json()['name'] 
    return jsonify({'result': name })


if __name__ == '__main__':
      app.run(host='0.0.0.0' , port=5000 )

