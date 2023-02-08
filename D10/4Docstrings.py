# Docstrings are used to document the code and are used to explain what the function does.

def format_name(first_name, last_name):
    """Take a first and last name and format it to return the title case version of the name.""" # Docstring
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = first_name.title()
    formated_l_name = last_name.title() 
    return f"{formated_f_name} {formated_l_name}"  # return tells the computer that this is the end of the function and exit the function

print(format_name(input("What is your first name? "), input("What is your last name? ")))