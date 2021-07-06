# from run import app
import unittest
import requests


class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"
    USER_URL = "{}/user".format(API_URL)
    USER_OBJECT = {
        "email": "new_email12@gmail.com",
        "first_name": "new_user_first_name",
        "last_name": "new_user_last_name",
        "password": "password1"
    }

    def test_1_get_all_user(self):
        r = requests.get(ApiTest.USER_URL)
        self.assertEqual(r.status_code, 200)

    def test_2_add_new_user(self):
        r = requests.post(ApiTest.USER_URL, json=ApiTest.USER_OBJECT)
        self.assertEqual(r.status_code, 201)

    def test_3_get_user_id(self):
        id = 4
        r = requests.get("{}/{}".format(ApiTest.USER_URL, id))
        self.assertEqual(r.status_code, 200)

    def test_4_delete_user_id(self):
        id = 4
        r = requests.delete("{}/{}".format(ApiTest.USER_URL, id))
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
