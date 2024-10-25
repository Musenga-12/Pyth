def remove_vowels(input_str):
    vowels = "aeiouAEIOU"
    result_str = "".join([char for char in input_str if char not in vowels])
    return result_str

# Get input from the user
text = input("Enter a string: ")
print("Text with vowels removed:", remove_vowels(text))