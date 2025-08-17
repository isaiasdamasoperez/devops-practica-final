import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()
    
    def test_hello_world(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), '¡Hola Mundo DevOps!')

if __name__ == '__main__':
    unittest.main()