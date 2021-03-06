import names
import random
from RandomWordGenerator import RandomWord
from faker import Faker

fake = Faker()

# "firstName": "string",
def first_name():
    return names.get_first_name()


# "middleName": "string",
def middle_name():
    return first_name()


# "lastName": "string",
def last_name():
    return names.get_last_name()


# "dateOfBirth": "2022-04-06",
def DoB():
    date_of_birth = fake.date_of_birth(minimum_age=18)
    return str(date_of_birth)


# "gender": "MALE",
def gender():
    gender_list = ["MALE", "FEMALE"]
    return random.choice(gender_list)


# "email": "string",
def email(string):
    return string + "@gmail.com"


# "phone": "string",
def phone():
    return '(' + str(random.randint(100, 999)) + ') ' \
            + str(random.randint(100, 999)) + "-" + str(random.randint(1000, 9999))


# "socialSecurity": "string",
def ssn():
    return fake.ssn()


# "driversLicense": "string",
def drivers_license():
    return fake.license_plate()


# "income": 0, (in cents) maximum int size 2147483647
def income():
    number = str(random.randint(1000000, 10000000))
    return number


# "address": "string",
def address():
    return fake.street_address()


# "city": "string",
def city():
    return fake.city()


# "state": "string",
def state():
    return fake.state()


# "zipcode": "string",
def zipcode():
    return fake.postcode()


# account type
def account_type():
    acc_list = ['LOAN', 'SAVINGS', 'CHECKING', 'CHECKING_AND_SAVINGS', 'CREDIT_CARD']
    return random.choice(acc_list)


def routing_number():
    return fake.aba()


def merchant_code():
    code = RandomWord(max_word_size=5, constant_word_size=True)
    return code.generate()


def description():
    return fake.sentence()



