import unittest
from unittest import TestCase

from functions.aline_application_generator import generate_application


class TestApplication(TestCase):
    def test_generate_application(self):
        response = generate_application(1)
        self.assertNotEqual(response, "Gateway and Underwriter isn't running")
        self.assertEqual(201, response.status_code)


if __name__ == '__main__':
    unittest.main()
