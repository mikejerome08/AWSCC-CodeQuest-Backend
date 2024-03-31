import json
import os

def print_menu():
    menu = ["1 - Add Username, Password, and Website",
            "2 - View All",
            "3 - Search",
            "4 - Delete",
            "5 - Update",
            "6 - Exit"]
    
    for option in menu:
        print(option)

def load_pass():
    if os.path.exists('passwords.json'):
        with open('passwords.json', 'r') as file:
            return json.load(file)
    return {}

def save_pass(passwords):
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file, indent=4)

def add():
    website = input("Enter name of website: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    passwords = load_pass()
    if website not in passwords:
        passwords[website] = []
    passwords[website].append({"email": email, "password": password})
    save_pass(passwords)
    print("Successfully added!")

def view():
    passwords = load_pass()
    if passwords:
        for website, logins in passwords.items():
            print(f"Website: {website}")
            for login in logins:
                print(f"\tEmail: {login['email']}")
                print(f"\tPassword: {login['password']}")
    else:
        print("No entries found.")

def search():
    website = input("Enter name of website to search: ")
    passwords = load_pass()
    if website in passwords:
        print(f"Website: {website}")
        for login in passwords[website]:
            print(f"\tEmail: {login['email']}")
            print(f"\tPassword: {login['password']}")
    else:
        print("Website not found.")

def delete(website):
    with open('passwords.json', 'r') as f:
        data = json.load(f)

        if website in data:
            print(f"Entries for {website}:")
            for i, login in enumerate(data[website], start=1):
                print(f"{i}. Email: {login['email']}, Password: {login['password']}")

            valid_idx = False
            while not valid_idx:
                num = int(input("Enter the number you want to delete: "))
                valid_idx = 0 <= num - 1 < len(data[website])

            data[website].pop(num - 1)

            if len(data[website]) == 0:
                data.pop(website)

            with open('passwords.json', 'w') as f:
                json.dump(data, f, indent=4)

            print("Successfully removed.")
        else:
            print("Website not found.")

def update():
    website = input("Enter name of website to update: ")
    passwords = load_pass()
    if website in passwords:
        print(f"Current entries for {website}:")
        for i, login in enumerate(passwords[website], start=1):
            print(f"{i}. Email: {login['email']}, Password: {login['password']}")
        
        index = int(input("Enter the index of entry to update: ")) - 1
        if 0 <= index < len(passwords[website]):
            email = input("Enter new email: ")
            password = input("Enter new password: ")
            passwords[website][index] = {"email": email, "password": password}
            save_pass(passwords)
            print("Entry updated successfully.")
        else:
            print("Invalid index.")
    else:
        print("Website not found.")

running = True

while running:
    print("PASSWORD MANAGER")
    print_menu()
    user_input = input("Enter a number: ")
    
    if user_input == "1":
        add()
    elif user_input == "2":
        view()
    elif user_input == "3":
        search()
    elif user_input == "4":
        website = input("Enter name of website to delete: ")
        delete(website)
    elif user_input == "5":
        update()
    elif user_input == "6":
        running = False
    else:
        print("Invalid input. Please enter a number between 1 and 6.")
