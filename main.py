import users
import login
import projects


options = {
    1: 'register',
    2: 'login'
}


def main_menu():
    selection = input("""
    Hello to our app , choose one of the options :
    1- Register , if you are new member
    2-Login
    """)
    if selection:
        user_input(int(selection))
    else:
        print("please choose valid option")
        main_menu()


def user_input(selection):
    while selection not in options.keys():
        print("please choose valid option")
        main_menu()

    if selection == 1:
        user = users.User.register_form()
        user_data = {
            'first_name': user.fname,
            'last_name': user.lname,
            'email': user.email,
            'password': user.password,
            'mobile': user.mobile
        }
        register_file = open("user-data.txt", "a")
        register_file.write(str(user_data) + '\n')
        register_file.close()
        print("Thank you for registration :)")
        main_menu()

    elif selection == 2:
        email = login.login_form()
        if email:
            projects.Project.projects_actions(email)
        else:
            main_menu()

    else:
        print("please enter valid option!")
        main_menu()


main_menu()
