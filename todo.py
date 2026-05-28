#Angela Mercado
#Challenge 3 To do List

#Init

shopping_list = []
donelist = []

#Functions
def shoppinglist():
        while True:
            shoplist = int(input("""This is your shopping list, please choose one of the options(Enter the option#)
    1. Add an item to list
    2. Mark an item as done
    3. Remove an item or Clear the List
    4. Exit the program
    : """))

            if shoplist == 1:
                additem()
            elif shoplist == 2:
                markdone()
            elif shoplist == 3:
                remove()
            elif shoplist == 4:
                break
            else:
                print("Please enter an option number")
                return

            print(shopping_list)

def additem():
    addeditem = input("What would you like to add to the list?: ")
    shopping_list.append(addeditem)
def markdone():
    while true:

        doneitem = input("Which item would you like to mark as done?: ")
        try:
            shopping_list.append

def remove():
    while True:
        choice = int(input("""Would you like to,
        1. Remove an item from list
        2. Clear whole list
        3. Back to Menu
        : """))

        if choice == 1:
            while True:
                removeditem = input("What would you like to remove?: ")

                try:
                    shopping_list.remove(removeditem)
                except:
                    print("Item not on list")
                return

        elif choice == 2:
            shopping_list.clear()
        elif choice == 3:
            return
        else:
            print("Please enter an option number")






#Main
shoppinglist()

