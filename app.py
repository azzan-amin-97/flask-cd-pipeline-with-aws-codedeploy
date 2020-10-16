from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import requests

app = Flask(__name__)


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

if __name__ == "__main__":
    app.run()
