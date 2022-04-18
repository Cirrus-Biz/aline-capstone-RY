from functions.aline_user_generator import generate_admin, get_member_json
from functions.aline_applicant_generator import generate_applicant
from functions.aline_application_generator import generate_application, process_applicants
from functions.aline_bank_and_branches_generator import generate_bank_address, generate_branch_address
from functions.aline_transactions_generator import deposit, withdrawal, payment, transfer
# to run microservice  mvn spring-boot:run -pl {microservice dir}


def main():
    # run users and bank microservice (gateway can be run for faster result)
    print(generate_admin())
    print(get_member_json())
    # run users microservice (gateway can be run for faster result)
    # run underwriter microservice
    print(generate_application())
    print(generate_applicant())
    print(process_applicants())
    # run banks and branches microservice
    print(generate_bank_address())
    print(generate_branch_address())
    # run transaction and account microservice
    deposit()
    withdrawal()
    payment()
    print(transfer())


if __name__ == '__main__':
    main()

