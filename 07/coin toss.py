import random

def tos():
    rand_i = random.randint(0, 1)
    outcomes = ["Heads", "Tails"]
    return outcomes[rand_i]

tos = tos()

print(tos)