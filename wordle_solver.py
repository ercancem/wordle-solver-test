from collections import Counter
from random import choice

MISS = 0
CLOSE = 1
MATCH = 2


def get_feedback(guess, secret):
    taken = [False] * 5
    result = [MISS] * 5
    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = MATCH
            taken[i] = True
    for i, c in enumerate(guess):
        if result[i] == MATCH:
            continue
        j = next((j for j, c2 in enumerate(secret) if not taken[j] and c == c2), None)
        if j is not None:
            result[i] = CLOSE
            taken[j] = True
    return result


WORDS = []
with open("words.dat", "r") as file:

    # reading each line
    for line in file:
        WORDS.append(line.strip("\n\r"))


print(len(WORDS))

secret = choice(WORDS)
guess = "trace"
print("Wordle is: ", secret)
feedback = get_feedback(guess, secret)
# print("Feedback is: ", feedback)
history = [(guess, feedback)]
print("History is: ", history)

remaining_words = [
    word
    for word in WORDS
    if all(get_feedback(guess, word) == feedback for guess, feedback in history)
]
print("remaining_words: ", remaining_words)
