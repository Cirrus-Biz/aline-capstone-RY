from functions.aline_user_generator import generate_admin, get_member_json
from functions.aline_application_generator import *
# to run microservice  mvn spring-boot:run -pl {microservice dir}


def main():
    print(generate_application(1))


if __name__ == '__main__':
    main()

