import unittest
from unittest import TestCase

from functions.aline_applicant_generator import generate_applicant


class TestApplicant(TestCase):
    def test_generate_applicant(self):
        response = generate_applicant(1)
        status_code = response.status_code
        assert status_code == 201


if __name__ == '__main__':
    unittest.main()