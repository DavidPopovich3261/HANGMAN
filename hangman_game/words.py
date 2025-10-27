import random


def choose_secret_word(words: list[str]) -> str:
    word=words[random.randint(0,len(words))]
    return word


