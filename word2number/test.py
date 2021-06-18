a_string = "abc !? 123"
alphanumeric = [character for character in a_string if character.isalnum()]

alphanumeric = "".join(alphanumeric)

print(alphanumeric)
