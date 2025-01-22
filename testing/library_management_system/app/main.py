import sys
from user import login, register, UserObj, client_menu, admin_menu


def main():
    print("Welcome to Basic Library Management System...\n[ ops ].\n\t1. login\n\t2. register")
    try:
        ops =  int(input("\n\n===[input]===  "))
        user :UserObj
        if ops == 1:
            user = login()
        elif ops == 2:
            user = register()
        else:
            print(f"Invalid ops...\nshutting down LMS...")
            exit(-1)

        if not user:
            print(f"Error fetching User...\nshutting down LMS...")
            exit(-1)
        client_menu(user) if user.mode == "client" else admin_menu()
        print("Thank you for using the Library Management System. Goodbye!")
        sys.exit()

    except Exception as e:
        print(f"ERROR [{e}]...\nshutting down LMS...")
        exit(-1)



if __name__ == '__main__':
    main()