import unittest
from unittest import TestCase

from functions.aline_transactions_generator import deposit, withdrawal, payment, transfer


class TestTransaction(TestCase):
    def test_deposit(self):
        response = deposit(1)
        status_code = response.status_code
        if status_code == 201:
            assert response == 201

    def test_withdrawal(self):
        response = withdrawal(1)
        status_code = response.status_code
        if status_code == 201:
            assert response == 201

    def test_payment(self):
        response = payment(1)
        status_code = response.status_code
        if status_code == 201:
            assert response == 201

    def test_transfer(self):
        response = transfer(1, 2, 3)
        assert response == 201
