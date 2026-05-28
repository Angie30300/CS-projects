#Angela Mercado
#Weather
#Advises you on what clothing to wear and accessories to bring based on tempurature given

#Function
def weather():
    tempurature = int(input("Please enter the tempurature:"))

    if tempurature >= 90:
        print("Wear something cool..It's burning hot.")
    elif tempurature >= 60:
        print("Wear something casual..It's pretty nice outside.")
    else:
        print("Wear layers. It's pretty chilly")

#Main
weather()
