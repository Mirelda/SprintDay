from flask import Flask, jsonify, request, make_response



app = Flask(__name__)


@app.route('/', methods = ['GET'])
def hi():
    return "<h1>Hello World!<h1>"


@app.route('/name', methods = ['GET'])
def name():
    x = request.args

    if(request.method == 'Post' or request.method == 'PUT'):

        return make_response(jsonify(Success= False, Error='405 Method Not Allowed.'),405)
        
    
    else:
    
        return jsonify({'firstname': x.get('firstname',''),
            'lastname':x.get('lastname','')})
    
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port ='8080')
