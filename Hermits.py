DRAGON_BROS = ["Mumbo Jumbo", "Iskall85", "Bdouble0100"]
STILL_ALIVE = ["Mumbo Jumbo", "Iskall85", "Bdouble0100", "Docm77",
               "JoeHillsTSD"]


def printer(winner):
    if winner in DRAGON_BROS:
        print("Dragon Bros!!!")
        if winner == DRAGON_BROS[2]:
            print("IDEA is rich!!!")
        elif winner == DRAGON_BROS[0]:
            print("How can a spoon win?!")
        else:
            burn_bdubs_castle()
    else:
        if winner == STILL_ALIVE[3]:
            amount_give_ren = 0.5
            give_ren_diamonds(amount_give_ren)
        else:
            print("Hiding from the dead works.")


def burn_bdubs_castle():
    print("Bdub's castle has been burned to a crisp :(")


def give_ren_diamonds(amount):
    print("Ren digity dog has been awarded "+ str(amount) + " diamonds!")


def input_check():
    while True:
        winner = str(input("Who won Demise?: "))

        if winner in STILL_ALIVE:
            return winner
        else:
            print("Incorrect name, try again!")


def main():
    winner = input_check()
    printer(winner)


main()
