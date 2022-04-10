from functions.ultilities.user_data_generator import *
import requests

first_name = first_name()
last_name = last_name()


def generate_applicant(number_of_applicants=0):
    for num in range(number_of_applicants):
        url = "http://localhost:8080/api/applicants"
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0ZWQiLCJhdXRob3JpdHkiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNjQ5MjcxNTI1LCJleHAiOjE2NTA0ODExMjV9.CvrY4PLj6-lONGpfxtL1Uh8de0hblJCLq95NoYZB59M"}

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

        form = requests.post(url, json=aline_applicant_form, headers=headers)
        print(form)
