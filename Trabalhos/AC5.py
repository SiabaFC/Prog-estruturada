import random
def main():

    vida1 = 100
    vida2 = 80

    atk1 = random.randint(10, 20)
    sav = random.randint(1, 5)
    atk2 = random.randint(20, 30)

    vida1 = vida1 - atk2 + sav
    vida2 = vida2 - atk1

    while vida1 > 0 and vida2 > 0:
        print(vida1, vida2)
        vida1 = vida1 - atk2 + sav
        vida2 = vida2 - atk1

        if vida1 <= 0:
            print("Voce morreu")
        if vida2 <= 0:
            print("Monstro morreu")
        if vida1 <= 0 and vida2 <= 0:
            print("Os dois morreram")


main()