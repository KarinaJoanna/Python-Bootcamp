# Functions with Outputs

# Title case
def format_name(first_name, last_name):
    formated_f_name = first_name.title()
    formated_l_name = last_name.title() 
  
    return f"{formated_f_name} {formated_l_name}"

# way 1

formated_string = format_name("james", "bond")
print(formated_string)

# way 2

print(format_name("james", "bond"))