from functions.aline_applicant_generator import generate_applicant
from functions.aline_application_generator import generate_application
# to run microservice  mvn spring-boot:run -pl {microservice dir}


def main():
    generate_application()
    generate_applicant()


if __name__ == '__main__':
    main()

