import random

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


german_words = [
    "Apfel", "Bäckerei", "Computer", "Dach", "Elefant", "Fahrrad", "Garten", "Haus",
    "Insel", "Jacke", "Katze", "Lampe", "Musik", "Nacht", "Orange", "Pizza", "Quark",
    "Regen", "Schule", "Tisch", "Uhr", "Vogel", "Wasser", "Xylophon", "Yacht",
    "Zitrone", "Bahnhof", "Chirurg", "Dünger", "Eltern", "Freund", "Gemüse", "Hund",
    "Insel", "Jäger", "Kaffee", "Lehrer", "Milch", "Nudeln", "Ofen", "Pferd", "Qualle",
    "Rakete", "Sonne", "Tee", "Urlaub", "Vogel", "Würfel", "Zahnarzt", "Zwilling"
]

while True:
    print(logo)
    random_word = random.choice(german_words)
    print(f'Pssst, the solution is {random_word}.')
    word_length = len(random_word)
    display = ["_"] * word_length
    lives = 6

    while "_" in display:
        guess = input("Guess a letter: ").lower()
        if guess in random_word.lower():
            for position in range(word_length):
                letter = random_word[position].lower()
                if letter == guess:
                    display[position] = random_word[position]
            print(display)
        else:
            lives -= 1
            print(stages[lives])
            print(f"Your lives are {lives}")
            print(display)
            if lives == 0:
                print("You lose")
                break

    if "_" not in display:
        print("You won!")

    request = input("Do you want to play again? (y/n): ").lower()
    if request == "n":
        print("See you again")
        break
    elif request != "y":
        while True:
            print("Write a valid answer")
            request = input("Do you want to play again? (y/n): ").lower()
            if request == "y":
                break
            elif request == "n":
                break
        if request == "n":
            print("See you again")
            break
