

def prompt_guess() -> str:
    letter=input('Please guess the letter.')
    return letter

def print_status(state: dict) -> None:
    print(state['display'],state['guessed'],(state['max_tries']-state['guesses_wrong']))


def print_result(state: dict) -> None:
    print()
    print(state['secret'],state['guessed'])