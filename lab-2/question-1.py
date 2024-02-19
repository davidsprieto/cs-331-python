def convert_celsius_to_fahrenheit(c):
    """Convert a numeric data type from degrees Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32


def convert_fahrenheit_to_celsius(f):
    """Convert a numeric data type from degrees Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


def get_temperature_conversion(user_choice, user_number):
    """Perform the temperature conversion based on user choice."""
    if user_choice == 1:
        return convert_celsius_to_fahrenheit(user_number), "Celsius", "Fahrenheit"
    else:
        return convert_fahrenheit_to_celsius(user_number), "Fahrenheit", "Celsius"


def get_valid_input(prompt, valid_responses):
    """Get a valid input from the user based on the provided valid responses."""
    while True:
        response = input(prompt).lower().strip()
        if response in valid_responses:
            return valid_responses[response]
        print("Invalid input, please try again.")


print("Welcome to the temperature degree converter.")

conversion_choices = {"1": 1, "2": 2}
yes_no_choices = {"yes": True, "no": False}

while True:
    user_choice = get_valid_input(
        "Enter '1' to convert from Celsius to Fahrenheit -- Enter '2' to convert from Fahrenheit to Celsius: ",
        conversion_choices)
    while True:
        try:
            user_number = float(input("What temperature would you like to convert?: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    converted_value, from_unit, to_unit = get_temperature_conversion(user_choice, user_number)
    print(f"{user_number}° {from_unit} to {to_unit} is: {converted_value}°")

    user_continue = get_valid_input("Would you like to perform another conversion? -- Enter 'yes' or 'no': ",
                                    yes_no_choices)
    if not user_continue:
        print("Bye ✌️")
        break
