import unittest

import requests


class BasicTests(unittest.TestCase):

    def test_addition(self):
        # Given
        num1 = 100
        num2 = 200

        # When
        response = requests.post("http://127.0.0.1:5000/api/addition",
                                 data={'num1': num1,
                                       'num2': num2})

        res_json = response.json()
        result = res_json['result']

        # Then
        self.assertEqual(result, 300)

    def test_subtraction(self):
        # Given
        num1 = 1
        num2 = 1

        # When
        response = requests.post("http://127.0.0.1:5000/api/subtraction",
                                 data={'num1': num1,
                                       'num2': num2})

        res_json = response.json()
        result = res_json['result']

        # Then
        self.assertEqual(result, 0)

    def test_multiplication(self):
        # Given
        num1 = 2
        num2 = 2

        # When
        response = requests.post("http://127.0.0.1:5000/api/multiplication",
                                 data={'num1': num1,
                                       'num2': num2})

        res_json = response.json()
        result = res_json['result']

        # Then
        self.assertEqual(result, 4)

    def test_division(self):
        # Given
        num1 = 2
        num2 = 2

        # When
        response = requests.post("http://127.0.0.1:5000/api/division",
                                 data={'num1': num1,
                                       'num2': num2})

        res_json = response.json()
        result = res_json['result']

        # Then
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()