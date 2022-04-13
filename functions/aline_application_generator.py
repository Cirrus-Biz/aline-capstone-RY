from functions.aline_user_generator import get_bearer_token
from functions.aline_applicant_generator import get_applicant_id
from functions.ultilities.user_data_generator import *
from functions.ultilities.request_functions import *

first_name = first_name()
last_name = last_name()


def application_form():
    aline_application_form = \
        {
            "applicationType": account_type(),
            "applicants": [
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
                    "income": income(),
                    "address": address(),
                    "city": city(),
                    "state": state(),
                    "zipcode": zipcode(),
                    "mailingAddress": address(),
                    "mailingCity": city(),
                    "mailingState": state(),
                    "mailingZipcode": zipcode()
                }
            ]
        }
    return aline_application_form


def existing_applicant_form():
    aline_application_form = \
        {
          "applicationType": "CHECKING",
          "noApplicants": true,
          "applicantIds": [
            num
          ]
        }


def generate_application(on_off=0):
    url = "http://localhost:8080/api/applications"
    url2 = "http://localhost:8071/applications"
    if on_off != 0:
        aline_application_form = application_form()

        print(post_request(url, url2, aline_application_form))


def get_application_id():
    application_list = []
    headers = {"Authorization": get_bearer_token()}
    url = "http://localhost:8080/api/applications"
    url2 = "http://localhost:8071/applications"

    response = get_request(url, url2, None, headers).json()
    pages = response['totalPages']
    for page in range(pages):
        page = "?page={}".format(page)
        applications = get_request(url + page, url2 + page, None, headers)
        response = applications.json()
        content = response['content']
        for app_id in content:
            app_id = app_id['primaryApplicant']['id']
            application_list.append(app_id)

    return set(application_list)


def process_applicants():
    results = list(get_applicant_id() - get_application_id())
    return results
