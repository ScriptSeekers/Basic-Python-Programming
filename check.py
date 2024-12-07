def is_palindrome(string):
    # Convert the string to lowercase and remove spaces for accurate checking
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    # Check if the string is the same when reversed
    return cleaned_string == cleaned_string[::-1]

# Example usage
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
