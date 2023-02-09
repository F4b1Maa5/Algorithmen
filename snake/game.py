import random

p1 = input("Player 1:")
p2 = input("Player 2:")

cards = {14: 'Ass', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Bube', 12: 'Dame', 13: 'König'}


quit = "0"

while(quit != "q"):
    randomnumberp1 = random.randrange(2,14)
    randomnumberp2 = random.randrange(2,14)
    print(p1 + " hat " + str(cards.get(randomnumberp1)) + " gezogen.")
    print(p2 + " antwortet daruf mit "+ str(cards.get(randomnumberp2)) )
    if(randomnumberp1 == randomnumberp2):
        print("Unentschieden PAIN")
    elif(randomnumberp1 > randomnumberp2):
        print(p1 + " hat damit gewonnen")
    else:
        print(p2 + " hatte einfach die bessere Antwort")
    quit = input("Zum beenden q drücken. Ansonsten wird das Spiel weitergeführt.")