import requests
from requests.structures import CaseInsensitiveDict
from functions.ultilities.request_functions import *

login_url = "http://localhost:8080/login"
login_url2 = "http://localhost:8070/login"
member_url = "http://localhost:8080/api/members"
member_url2 = "http://localhost:8083/members"
registration_url = "http://localhost:8080/api/users/registration"
registration_url2 = "http://localhost:8070/users/registration"


def get_bearer_token():
    aline_login_form = \
        {
            "username": "noodleween",
            "password": "P@ssw0rd"
        }
    form = post_request(login_url, login_url2, aline_login_form)
    return form.headers['Authorization']


headers = {"Authorization": get_bearer_token()}


def get_member_json():
    response = get_request(member_url, member_url2, None, headers).json()
    pages = response['totalPages']
    for page in range(pages):
        page = "?page={}".format(page)
        member = get_request(member_url + page, member_url2 + page, None, headers)
        response = member.json()
        content = response['content']
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
            return generate_user(aline_member_form)


def generate_admin(on_off=0):
    if on_off != 0:
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
        return post_request(registration_url, registration_url2, aline_user_form)


def generate_user(form):
    return post_request(registration_url, registration_url2, form)
