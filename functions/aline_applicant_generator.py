from functions.ultilities.request_functions import *
from functions.ultilities.user_data_generator import *
from functions.aline_user_generator import get_bearer_token

first_name = first_name()
last_name = last_name()

headers = {"Authorization": get_bearer_token()}
url = "http://localhost:8080/api/applicants"
url2 = "http://localhost:8071/applicants"


def applicant_form():
    aline_applicant_form = \
        {
            "firstName": first_name,
            "middleName": middle_name(),
            "lastName": last_name,
            "dateOfBirth": DoB(),
            "gender": gender(),
            "email": email(first_name + last_name),
            "phone": phone(),
            "socialSecurity": ssn(),
            "driversLicense": drivers_license(),
            "income": 2147483647,
            "address": address(),
            "city": city(),
            "state": state(),
            "zipcode": zipcode(),
            "mailingAddress": address(),
            "mailingCity": city(),
            "mailingState": state(),
            "mailingZipcode": zipcode()
        }
    return aline_applicant_form


def generate_applicant(on_off=0):
    if on_off != 0:
        aline_applicant_form = applicant_form()

        return post_request(url, url2, aline_applicant_form, headers)


def get_applicant_id():
    applicant_list = []

    response = get_request(url, url2, None, headers).json()
    pages = response['totalPages']
    for page in range(pages):
        page = "?page={}".format(page)
        applications = get_request(url + page, url2 + page, None, headers)
        response = applications.json()
        content = response['content']
        for app_id in content:
            app_id = app_id['id']
            applicant_list.append(app_id)

    return set(applicant_list)
