import random

german_words = [
    "Apfel", "Bäckerei", "Computer", "Dach", "Elefant", "Fahrrad", "Garten", "Haus",
    "Insel", "Jacke", "Katze", "Lampe", "Musik", "Nacht", "Orange", "Pizza", "Quark",
    "Regen", "Schule", "Tisch", "Uhr", "Vogel", "Wasser", "Xylophon", "Yacht",
    "Zitrone", "Bahnhof", "Chirurg", "Dünger", "Eltern", "Freund", "Gemüse", "Hund",
    "Insel", "Jäger", "Kaffee", "Lehrer", "Milch", "Nudeln", "Ofen", "Pferd", "Qualle",
    "Rakete", "Sonne", "Tee", "Urlaub", "Vogel", "Würfel", "Zahnarzt", "Zwilling"
]

random_word = random.choice(german_words)

print(f'Pssst, the solution is {random_word}.')
word_length = len(random_word)
display = ["_"] * word_length
print(display)

while "_" in display:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = random_word[position].lower()
        if letter == guess:
            display[position] = random_word[position]
            print(display)
print("Win")
