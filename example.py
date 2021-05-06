from flask import Flask, jsonify, request, make_response



app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hi():
    return "<h1>Hello World!<h1>"


@app.route('/name', methods = ['GET'])
def name():
    x = request.args
    return jsonify({'firstname': x.get('firstname',''),
            'lastname':x.get('lastname','')})


@app.route("/check")
def check():
    return make_response(jsonify(Success=True), 200)


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port ='8080')
