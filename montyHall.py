import random

def montyHall(numberOfDoors, switch):

    prize = random.randint(0, numberOfDoors-1)
    choice = random.randint(0, numberOfDoors-1)

    selected = list(range(numberOfDoors))

    while len(selected) > 2:
        rand = random.choice(selected)
        if rand not in [prize, choice]:
            selected.remove(rand)

    if switch:
        available = list(selected)
        available.remove(choice)
        choice = available[0]

    return prize == choice
        

winner = 0
winnerSwitcher = 0
times = 4
doors = 400

for _ in range(times):
    sol = montyHall(doors, False)
    if sol:
        winner = winner + 1

    sol = montyHall(doors, True)
    if sol:
        winnerSwitcher = winnerSwitcher + 1  

switchWinner = 0
for _ in range(times):
    switchWinner = switchWinner + montyHall(doors, True)

print("When the person decided not to switch, he won", str((winner/times)*100),  "percent of the times.")
print("When the person decided to switch, he won", str((switchWinner/times)*100),  "percent of the times.")
