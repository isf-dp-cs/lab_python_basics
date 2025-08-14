print("Welcome to the A Game! Enter words that start with the letter a to earn points! Type exit to leave the game.")

user_word = ""
points = 0

while user_word != "exit":
    print("Your score: ", points)
    user_word = input("Tell me a word that starts with A: ")

    points = points + 1
