"""EX02 - one shot wordle."""
__author__ = "730481704"

secret: str = "python"
guess: str = input(f"What is your { len(secret) }-letter guess? ")

while len(guess) != len(secret):  #checking if the length of the guessed word matches the secret word
    guess = input(f"That was not { len(secret) } letters! Try again: ")

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")

index: int = 0
emoji: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

if guess == secret:
    while index < len(secret):
        emoji = emoji + GREEN_BOX 
        index = index + 1
    print(emoji)
    print("Woo! You got it!")
else:
    while index < len(secret):
        if guess[index] == secret[index]:
            emoji = emoji + GREEN_BOX 
        else:
            position_found = False
            match = 0
            while not position_found and match < len(secret):
                if guess[index] == secret[match]:
                    position_found = True
                else:
                    match = match + 1
            if position_found:
                emoji = emoji + YELLOW_BOX
            else:
                emoji = emoji + WHITE_BOX
        index = index + 1
    print(emoji)
    print("Not quite. Play again soon!")