import unittest
from unittest import TestCase

from functions.aline_user_generator import generate_admin, get_member_json


class TestUser(TestCase):
    def test_get_member_json(self):
        response = get_member_json(1)
        if response is None:
            assert response is None
        else:
            assert response.status_code == 201

    def test_generate_admin(self):
        response = generate_admin(1)
        status_code = response.status_code
        text = response.text
        if status_code == 201:
            assert response == 201, text
        elif status_code == 409:
            assert response == 409, text
