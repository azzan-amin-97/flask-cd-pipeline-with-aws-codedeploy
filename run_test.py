import unittest
import requests

from app_test import BASE_HOST, BASE_PORT


class BasicTests(unittest.TestCase):

    def test_addition(self):
        # Given
        num1 = 100
        num2 = 200

        # When
        response = requests.post(f"http://{BASE_HOST}:{BASE_PORT}/api/addition",
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
        response = requests.post(f"http://{BASE_HOST}:{BASE_PORT}/subtraction",
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
        response = requests.post(f"http://{BASE_HOST}:{BASE_PORT}/api/multiplication",
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
        response = requests.post(f"http://{BASE_HOST}:{BASE_PORT}/api/division",
                                 data={'num1': num1,
                                       'num2': num2})

        res_json = response.json()
        result = res_json['result']

        # Then
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()