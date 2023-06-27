import random

def coin_flip():
    choice = input("Heads or tails? Type 'h' for heads and 't' for tails.\n")
    face_value = random.choice(['h', 't'])
    if choice == face_value:
        return "Congratulations, you guessed correctly!"
    else:
        return "Sorry, you guessed incorrectly."

print(coin_flip())
