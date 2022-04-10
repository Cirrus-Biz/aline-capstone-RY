from functions.ultilities.user_data_generator import *
import requests

first_name = first_name()
last_name = last_name()


def generate_users(number_of_applications=0):
    for num in range(number_of_applications):
        url = "http://localhost:8080/api/applications"

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

        form = requests.post(url, json=aline_application_form)
        print(form)
