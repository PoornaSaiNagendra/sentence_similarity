import unittest
from flask_testing import TestCase

class MyTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app

    def test_calculate_similarity(self):
        response = self.client.post('/v1/calculate_similarity', json={"text1": "foo", "text2": "bar"})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
