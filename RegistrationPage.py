def registration(user,password):
    if (user.endswith(".com") and user.__contains__("@")) or (user.startswith("998") and len(user) == 12):
        if (len(password) >= 8 and any(char.islower() for char in password) and any(
                char.isupper() for char in password) and any(char.isdigit() for char in password)):
            print(password)
        else:
            raise ValueError(
                "Password should contain at least one uppercase, lowercase and digit. Its length should be at least 8")
        return user, password
    else:
        raise ValueError("Invalid email or phone number format")


def option(options):
    if options.lower() == "email":
        email = input("Please enter your email:")
        return email

    if options.lower() == "phone":
        phone = input("Please enter your phone:")
        return phone

user = input("Choose the option 'email' or 'phone'?")
password = input("Please enter password:")
user_option = option(user)
register = registration(user_option, password)
print(register)