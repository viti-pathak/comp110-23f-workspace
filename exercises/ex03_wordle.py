"""EX03 - Structured Wordle"""
__author__ = "730523434"

def contains_char(word: str, character: str) -> bool: 
    """checks to see if character is contained in guess"""
    assert len(character) == 1
    position: bool = False
    index: int = 0
    while position is False and index < len(word):
        if word[index] == character:
            position = True
        else:
            position = False
        index = index + 1
    return position

def emojified(guess: str, secret: str) -> str:
    """prints out colored emoji boxes"""
    assert len(guess) == len(secret)

    i: int = 0
    emoji: str = ""

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while i < len(secret):
        if guess[i] == secret[i]:
            emoji = emoji + GREEN_BOX
        else:
            if contains_char(secret, guess[i]) == True:
                    emoji = emoji + YELLOW_BOX
            else:
                    emoji = emoji + WHITE_BOX
        i = i + 1
    return emoji

def input_guess(length: int) -> str:
    guess: str = input(f"Enter a { length } character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't { length } chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turns: int = 1
    won: bool = False
    while turns < 7 and won is False:
        print(f"=== Turn { turns }/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            won = True
        else:
            turns = turns + 1
    if won is True:
        print(f"You won in { turns }/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()