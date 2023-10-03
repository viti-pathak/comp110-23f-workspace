"""EX03 - Structured Wordle."""
__author__ = "730523434"

def contains_char(word: str, character: str) -> bool:
    """Checks if a character is contained in a word."""
    assert len(character) == 1
    position: bool = False
    index: int = 0
    while not position and index < len(word):
        if word[index] == character:
            position = True
        index += 1
    return position

def emojified(guess: str, secret: str) -> str:
    """Prints out colored emoji boxes."""
    assert len(guess) == len(secret)

    i: int = 0
    emoji: str = ""

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        i += 1
    return emoji

def input_guess(length: int) -> str:
    """Gets user input for a word guess."""
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} characters! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turns: int = 1
    won: bool = False
    while turns < 7 and not won:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            won = True
        else:
            turns += 1
    if won:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()