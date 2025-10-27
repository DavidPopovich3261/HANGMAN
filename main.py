from hangman_game import game,io,words
from data import words_list
from tests import test_game


def play(wordse: list[str], max_tries: int = 6) -> None:
    word=words.choose_secret_word(wordse)
    state=game.init_state(word,max_tries)
    flag1=True
    flag2=True
    while flag1 and flag2:
        letter=io.prompt_guess()
        ret=game.validate_guess(letter,state['guessed'])
        print(ret[1])
        if ret[0]:
            apply=game.apply_guess(state,letter)
            if apply:
                print('success')
            else:
                print('loss')
        io.print_status(state,game.render_display(state))
        flag1=not game.is_won(state)
        flag2 =not game.is_lost(state)
    if flag2:
        pass








