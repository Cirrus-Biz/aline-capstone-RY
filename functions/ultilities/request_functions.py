import requests


def post_request(url, url2=None,  json=None, headers=None):
    try:
        form = requests.post(url, json=json, headers=headers)
        return form
    except requests.exceptions.RequestException:
        try:

            form = requests.post(url2, json=json, headers=headers)
            return form
        except requests.exceptions.RequestException:
            return "Services aren't running"


def get_request(url, url2=None,  json=None, headers=None):
    try:
        form = requests.get(url, json=json, headers=headers)
        return form
    except requests.exceptions.RequestException:
        try:

            form = requests.get(url2, json=json, headers=headers)
            return form
        except requests.exceptions.RequestException:
            return "Services aren't running"

