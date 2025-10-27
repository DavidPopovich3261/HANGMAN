

def init_state(secret: str, max_tries: int) -> dict:
    state={
            'secret':secret,
           'display':list[str],
           'guessed':set[str],
           'guesses_wrong':0,
           'max_tries':max_tries
           }
    return state


def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    ch=ch.strip()
    if len(ch)==1 and ch not in guessed and 'א' <= ch <='ת' :
        ret= (True,'The input is correct')
        return ret
    ret=(False,"The input is incorrect")
    return ret


def apply_guess(state: dict, ch: str) -> bool:
    if ch in state['secret']:
        state['guessed'].append(ch)
        return True
    else:
        state['guesses_wrong']+=1
        return False


def is_won(state: dict) -> bool:
    for i in state['secret']:
        if i not in state['guessed']:
            return False
    return True


def is_lost(state: dict) -> bool:
    if state['guesses_wrong']>=state['max_tries']:
        return True
    return False

def render_display(state: dict) -> str:
    pass