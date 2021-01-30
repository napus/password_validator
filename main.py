my_string = input("Enter password: ")
def validator(my_string):
    my_spec_char = ['!','@','#','$','%','^','&','*']
    val = True
    if not any(i.isdigit() for i in my_string):
        print("No digits in password")
        val = False
    if not any(char in my_spec_char for char in my_string):
        print("No special characters in password")
        val = False
    if val:
        print("Password validated")


if __name__ == "__main__":
    validator(my_string)
