from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import requests

app = Flask(__name__)

BASE_HOST = '0.0.0.0'
BASE_PORT = 80

class Addition(Resource):
    def post(self):
        numbers = request.form.to_dict()
        num = []
        # Append the dateRange(Dict) value into dateList
        for key, value in numbers.items():
            temp = value
            num.append(temp)
        num1 = int(num[0])
        num2 = int(num[1])
        result = num1 + num2
        return jsonify(result=result)


class Subtration(Resource):
    def post(self):
        numbers = request.form.to_dict()
        num = []
        # Append the dateRange(Dict) value into dateList
        for key, value in numbers.items():
            temp = value
            num.append(temp)
        num1 = int(num[0])
        num2 = int(num[1])
        result = num1 - num2
        return jsonify(result=result)


class Multiplication(Resource):
    def post(self):
        numbers = request.form.to_dict()
        num = []
        # Append the dateRange(Dict) value into dateList
        for key, value in numbers.items():
            temp = value
            num.append(temp)
        num1 = int(num[0])
        num2 = int(num[1])
        result = num1 * num2
        return jsonify(result=result)


class Division(Resource):
    def post(self):
        numbers = request.form.to_dict()
        num = []
        # Append the dateRange(Dict) value into dateList
        for key, value in numbers.items():
            temp = value
            num.append(temp)
        num1 = int(num[0])
        num2 = int(num[1])
        result = num1 / num2
        return jsonify(result=result)


api = Api(app)
api.add_resource(Addition, '/api/addition')
api.add_resource(Subtration, '/api/subtraction')
api.add_resource(Multiplication, '/api/multiplication')
api.add_resource(Division, '/api/division')


@app.route('/')
def home():
    num1 = 1
    num2 = 2

    response = requests.post(f"http://{BASE_HOST}:{BASE_PORT}/api/addition",
                             data={'num1': num1,
                                   'num2': num2})
    res_json = response.json()
    result = res_json['result']
    return f'<H1>{num1} + {num2} = {result}</H1>'


if __name__ == "__main__":
    app.run(host=BASE_HOST, port=BASE_PORT, debug=True)
