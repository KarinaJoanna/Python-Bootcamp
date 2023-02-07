# Multiple return values

def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = first_name.title()
    formated_l_name = last_name.title() 
    return f"{formated_f_name} {formated_l_name}"  # return tells the computer that this is the end of the function and exit the function

print(format_name(input("Whats your first name"), input("Whats your last name")))