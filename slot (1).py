#Angela Mercado and Alejandra Figueroa Villanueva
#Slot Machine


#Init
import time
import random
global credits
credits = 0

#Functions
def payout():
    credits == credits + payout



def slot():
    while True:
        global credits
        choice = input("""Welcome to the Slot Machine. What would you like to do?
        1. Play
        2. Buy credits
        3. Exit
        : """)

        if choice == "1" and credits != 0:

            credits = credits - 10
            print ("Spinning the slot machine..")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("...")
            symbols = ['♥', '♦', '♠', '7']
            list = []

            #Randomizer
            for i in range(3):
                list.append(random.choices(symbols, weights = [9,7,3,1]))

            print(f"{(list)}")
            print(f"Credits remaining:{credits} ")


            if list == [['7'], ['7'], ['7']]:
                print("Jackpot!!!")
                credits = credits + 1500
            elif list == [['♥'], ['♥'], ['♥']] or list == [['♦'], ['♦'], ['♦']] or list == [['♠'], ['♠'], ['♠']]:
                print("Small Win!")
                credits = credits + 100
            else:
                print("You Lose..")

        elif choice == "1" and credits == 0:
                print("INSUFFICIENT FUNDS. Please buy more credits")
                print(f"Credits remaining:{credits} ")

        elif choice == "2":
            creditchoice = input("""How much would you like to add?
            1. 20 credits
            2. 50 credits
            3. 100 credits
            : """)
            if creditchoice == "1":
                credits = credits + 20
            elif creditchoice == "2":
                credits = credits + 50
            elif creditchoice == "3":
                credits = credits + 100
            else:
                print("Please enter the correct number")

        elif choice == "3":
                break


def simulation():
    credits = 10000
    symbols = ['♥', '♦', '♠', '7']
    list = []
    for i in range(1000):
        credits = credits - 10

        for x in range(3):
            list.append(random.choices(symbols, weights = [9,7,3,1]))


        print(f"Credits remaining:{credits} ")
        print(f"{(list)}")


        if list == [['7'], ['7'], ['7']]:
            print("Jackpot!!!")
            credits = credits + 500
        elif list == [['♥'], ['♥'], ['♥']] or list == [['♦'], ['♦'], ['♦']] or list == [['♠'], ['♠'], ['♠']]:
            print("Small Win!")
            credits = credits + 70
        else:
            print("You Lose..")
        list = []


    print(f"Casino Profit: {10000 - credits}")



#Main
simulation()

