
  # Function to calculate the position
  # of characters in a string (numbers are left untouched)
def positions(str):
    NUM = 31
    for character in str:
        if character.isdigit():
            print(character, end ="")
        # Performing AND operation with number 31
        else:
            print((ord(character) & NUM), end ="")
    return

def remove(string):
    return string.replace(" ", "")
  
# Driver code
str = "A8c"
positions(remove(str))
