import random

words = ["apple", "book", "computer", "python"]
word = random.choice(words)
chance = len(word)

for i in range(chance):
    guess = input("کلمه را حدس بزن: ")
    if guess == word:
        print("تبریک! کلمه را درست حدس زدی.")
        break
else:
    print("پایان بازی!")