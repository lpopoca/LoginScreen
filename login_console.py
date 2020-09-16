import json

# Dictionary holds all the usernames and passwords.
login_dict = json.load(open("logins.json"))

def create_login(login_dict):
    """Create a new login"""
    #TODO Add a way to save to json file.
    pass

def login(login_dict):
    """Enter a password and username to login"""
    userinput = input("What is your username?-->")
    passinput = input("What is your password?-->")
    current_login = {userinput:passinput}

    if current_login.get(userinput) == login_dict.get(userinput):
        print("Login successfull. Welcome {}".format(userinput))

def menu():
    """Runs a menu to either login or create a login"""
    #TODO Create a menu
    pass

def main():
    menu()

if __name__ == "__main__":
    main()