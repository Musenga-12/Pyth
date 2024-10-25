def camel_to_snake(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    # Remove leading underscore if the input starts with an uppercase
    if snake_case[0] == "_":
        snake_case = snake_case[1:]
    return snake_case

# Get input from the user
camel_case_input = input("Enter the variable name in camelCase: ")
print("Variable name in snake_case:", camel_to_snake(camel_case_input))