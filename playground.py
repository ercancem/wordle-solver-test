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
  for i,c in enumerate(guess):
    if result[i] == MATCH: continue
    j = next((j for j, c2 in enumerate(secret) if not taken[j] and c == c2), None)
    if j is not None:
      result[i] = CLOSE
      taken[j] = True
  return result

WORDS = []
with open('words.dat', 'r') as file:
   
    # reading each line    
    for line in file:
         WORDS.append(line.strip('\n\r'))


from collections import Counter

# history: a list of tuple of (guess, feedback)
# feedback: a list of length 5, each element can be MISS, CLOSE, or MATCH
def play(history):
  # Hard coded first guess
  turn = len(history) + 1
  if turn == 1:
    return 'trace'

# li = [row[index] for row in outer_list]
# is equivalent to:
#     li = []
# for row in outer_list:
#     li.append(row[index])
  
  # When there are few words left
  # print("I am under comment, when there a re few words left..")
  remaining_words = [word for word in WORDS if all(get_feedback(guess, word) == feedback for guess, feedback in history)]
  # print("remaining_words: ", remaining_words)
  if len(remaining_words) <= 2:
    return remaining_words[0]
  
  # Hardcoded hard case
  if turn == 3 and history == [('trace', [MISS, CLOSE, MISS, MISS, CLOSE]), ('risen', [CLOSE, MISS, MISS, MATCH, MISS])]:
    return 'howdy'

  guess_list = WORDS if turn > 2 and len(remaining_words) < 100 else remaining_words
  # print("guess_list: ", guess_list)
  return find_best_guest(guess_list, remaining_words)
  

def find_best_guest(guess_list, secret_list):
  print("I am inside find best guess")
  R = []
  secret_set = set(secret_list)
  print("R: ", R)
  print("secret_set", secret_set)
  for guess in guess_list:
    c = Counter([tuple(get_feedback(guess, secret)) for secret in secret_list])
    R.append([guess, len(c), guess in secret_set, -max(c.values())])
    print("guess: ", guess)
    print("c: ", c)
    print("R: ", R)
  best_guess = max(R, key=lambda t:t[1:])
  print("best_guess: ", best_guess)
  return best_guess[0]
  

secret = choice(WORDS)
print(secret)
print()

guess = None
history = []
while guess != secret:
  guess = play(history)
  feedback = get_feedback(guess, secret)
  history.append((guess, feedback))
  print(guess)
  print("".join(map(str,feedback)))
  print()

print("SCORE:", len(history))
