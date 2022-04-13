from functions.aline_applicant_generator import generate_applicant, get_applicant_id
from functions.aline_application_generator import *
from functions.aline_user_generator import generate_admin
# to run microservice  mvn spring-boot:run -pl {microservice dir}


def main():
    print(process_applicants())


if __name__ == '__main__':
    main()

