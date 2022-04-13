import requests
from requests.structures import CaseInsensitiveDict
from functions.ultilities.request_functions import *


def get_bearer_token():
    url = "http://localhost:8080/login"
    url2 = "http://localhost:8070/login"

    aline_login_form = \
        {
            "username": "noodleween",
            "password": "P@ssw0rd"
        }
    form = post_request(url, url2, aline_login_form)
    return form.headers['Authorization']


def get_member_json():
    url = "http://localhost:8080/api/members"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = get_bearer_token()

    response = requests.get(url, headers=headers)
    content = response.json()['content']
    for member in content:
        membershipId = member['membershipId']
        firstName = member['applicant']['firstName']
        lastName = member['applicant']['lastName']
        socialSecurity = member['applicant']['socialSecurity']
        lastFourOfSSN = socialSecurity.split('-')[-1]

        aline_member_form = \
            {
                "username": firstName + lastName,
                "password": "P@ssw0rd",
                "role": "member",
                'membershipId': membershipId,
                'lastFourOfSSN': lastFourOfSSN
            }
        generate_user(aline_member_form)


def generate_admin(on_off=0):
    if on_off != 0:
        url = "http://localhost:8080/api/users/registration"

        aline_user_form = \
            {
                "username": "noodleween",
                "password": "P@ssw0rd",
                "role": "admin",
                "firstName": "JR",
                "lastName": "Yabut",
                "email": "ricardo.yabut@smoothstack.com",
                "phone": "(208) 555-0129"
            }

        form = requests.post(url, json=aline_user_form)
        print(form)


def generate_user(form):
    url = "http://localhost:8080/api/users/registration"

    form = requests.post(url, json=form)
    print(form)
