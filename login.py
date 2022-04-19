import ast


def login_form():
    print("please enter your email and password")
    email = input("Email : ")
    password = input("Password : ")
    if check_data(email, password):
        return email
    else:
        return False


def check_data(email, password):
    user_data = open("user-data.txt", "r")
    lines = user_data.readlines()
    for line in lines:
        user = ast.literal_eval(line)
        if email == user['email'] and password == user['password']:
            print('logged in successfully welcome to our app ')
            user_data.close()
            return email
        elif email == user['email'] and password != user['password']:
            print("sorry you entered wrong password try again")
            login_form()
    else:
        print("sorry this email doesn't exist enter valid email or try to register first .")
        user_data.close()
        return False
