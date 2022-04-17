from functions.ultilities.user_data_generator import *
from functions.ultilities.request_functions import *
from functions.aline_user_generator import get_bearer_token

headers = {"Authorization": get_bearer_token()}
bank_url = "http://localhost:8080/api/banks"
bank_url2 = "http://localhost:8083/banks"
branches_url = "http://localhost:8080/api/branches"
branches_url2 = "http://localhost:8083/branches"


def bank_form():
    aline_bank_form = \
        {
          "routingNumber": routing_number(),
          "address": address(),
          "city": city(),
          "state": state(),
          "zipcode": zipcode()
        }
    return aline_bank_form


def branch_form(num):
    aline_branch_form = \
        {
          "name": last_name(),
          "address": address(),
          "city": city(),
          "state": state(),
          "zipcode": zipcode(),
          "phone": phone(),
          "bankID": num
        }
    return aline_branch_form


def generate_bank_address(on_off=0):
    if on_off != 0:
        aline_bank_form = bank_form()

        return post_request(bank_url, bank_url2, aline_bank_form, headers)
    return


def get_bank_and_branch_id():
    bank_list = []
    branches_list = []

    # grabs the id's from banks endpoint
    response = get_request(bank_url, bank_url2, None, headers).json()
    pages = response['totalPages']
    for page in range(pages):
        page = "?page={}".format(page)
        banks = get_request(bank_url + page, bank_url2 + page, None, headers)
        response = banks.json()
        content = response['content']
        for bank_id in content:
            bank_id = bank_id['id']
            bank_list.append(bank_id)

    # grabs bank id's from branches endpoint
    response = get_request(branches_url, branches_url2, None, headers).json()
    pages = response['totalPages']
    for page in range(pages):
        page = "?page={}".format(page)
        branch = get_request(branches_url + page, branches_url2 + page, None, headers)
        response = branch.json()
        content = response['content']
        for branch_id in content:
            branch_id = branch_id['bank']['id']
            branches_list.append(branch_id)

    return list(set(bank_list) - set(branches_list))


def generate_branch_address(on_off=0):
    if on_off != 0:
        for bank in get_bank_and_branch_id():
            form = branch_form(bank)
            return post_request(branches_url, branches_url2, form, headers)
