import unittest
from unittest import TestCase

from functions.aline_bank_and_branches_generator import generate_bank_address, generate_branch_address


class TestBanksAndBranches(TestCase):
    def test_generate_bank_address(self):
        response = generate_bank_address(1)
        assert response.status_code == 201

    def test_generate_branch_address(self):
        response = generate_branch_address(1)
        assert response.status_code == 201


if __name__ == '__main__':
    unittest.main()
