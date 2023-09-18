"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730523434"

word: str = input("Enter a 5-character word: ")
if (len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
if (len(single_character) != 1): 
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_character + " in " + word)

count: int = 0 
if (single_character == word[0]): 
    print(single_character + " found at index 0")
    count = count + 1
if (single_character == word[1]): 
    print(single_character + " found at index 1")
    count = count + 1
if (single_character == word[2]):
    print(single_character + " found at index 2")
    count = count + 1
if (single_character == word[3]): 
    print(single_character + " found at index 3")
    count = count + 1
if (single_character == word[4]): 
    print(single_character + " found at index 4")
    count = count + 1

if (count == 0):
    print("No instances of " + single_character + " found in " + word)
if (count == 1):
    print("1 instance of " + single_character + " found in " + word)
if (count > 1): 
    print(str(count) + " instances of " + single_character + " found in " + word)