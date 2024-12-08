def format_name(f_name, l_name):
    """Take a first and last name and capitalize the first letters of each"""
    if f_name == "" or l_name == "":
        return "You did not provided a valid name.."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name?"), input("What is your last name?")))
