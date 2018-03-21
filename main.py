from flask import Flask, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


@app.route('/idk', methods=['POST'])
def idk():
    if request.method == 'POST':
        request
        return "hi mom" + request.form['file'] + request.form['dest']



if __name__ == '__main__':
    app.run(port=8081)