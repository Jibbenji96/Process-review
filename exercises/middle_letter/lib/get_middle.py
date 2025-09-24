import math

def get_middle(word):
    if len(word) % 2 == 0:
        print((len(word)/2))
        return f"{word[(len(word)//2)-1]}{word[len(word)//2]}"
    return word[math.floor(len(word)/2)]