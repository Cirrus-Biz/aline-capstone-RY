from functions.ultilities.user_data_generator import *
from functions.ultilities.request_functions import *
from functions.aline_user_generator import get_bearer_token

transaction_url = "http://localhost:8080/api/transactions"
transaction_url2 = "http://localhost:8073/transactions"
account_url = "http://localhost:8080/api/accounts"
account_url2 = "http://localhost:8072/accounts"
headers = {"Authorization": get_bearer_token()}


def transaction_form(account_number, transaction_type="DEPOSIT", amount=100):
    true = "true"
    aline_transaction_form = \
        {
          "type": transaction_type,
          "method": "ACH",
          "amount": amount,
          "merchantCode": merchant_code(),
          "merchantName": last_name(),
          "description": description(),
          "accountNumber": account_number,
          "hold": bool(true)
        }
    return aline_transaction_form


def get_account():
    account_num_list = []
    status_list = []
    balance_list = []
    response = get_request(account_url, account_url2, None, headers).json()
    pages = response['totalPages']
    for page in range(pages):
        page = "?page={}".format(page)
        accounts = get_request(account_url + page, account_url2 + page, None, headers)
        response = accounts.json()
        content = response['content']
        for account_num in content:
            account_num = account_num['accountNumber']
            account_num_list.append(account_num)
        for stat in content:
            stat = stat['status']
            status_list.append(stat)
        for balance in content:
            balance = balance['balance']
            balance_list.append(balance)
    account_dict = {
        'account_num': account_num_list,
        'status': status_list,
        'balance': balance_list
    }
    return account_dict


def deposit(on_off=0, amount=100):
    account_dict = get_account()
    if on_off != 0:
        account_num = account_dict['account_num']
        for num in account_num:
            form = transaction_form(num, amount=amount)
            print(post_request(transaction_url, transaction_url2, form))
            print("deposited in {}".format(num))


def withdrawal(on_off=0, amount=100):
    account_dict = get_account()
    if on_off != 0:
        account_num = account_dict['account_num']
        for num in account_num:
            form = transaction_form(num, 'WITHDRAWAL', amount)
            print(post_request(transaction_url, transaction_url2, form))
            print("withdrawal in {}".format(num))


def payment(on_off=0, amount=100):
    account_dict = get_account()
    if on_off != 0:
        account_num = account_dict['account_num']
        for num in account_num:
            form = transaction_form(num, 'PAYMENT', amount)
            print(post_request(transaction_url, transaction_url2, form))
            print("payment in {}".format(num))


