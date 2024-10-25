def camel_case(camel_case_input):
    snake_case =""
    for char in camel_case_input :
        if char.isupper () :
            snake_case +="_"+char.lower ()
        else :
            snake_case +=char 
    return snake_case
camel_case_input =input("\nenter the name:")
print (f"The snake case is :{camel_case (camel_case_input )}")
