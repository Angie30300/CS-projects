#Angela Mercado
#Grade
# Writes a function that asks the user to input a score as an interger and returns the appropriate letter

#Function
def grade():
    score = int(input("Please enter your score:"))

    if score >= 90:
        print("You got an A!!")
    if score >= 80 and score <90:
        print("You got a B!")
    if score >=70 and score <80:
        print("You got a C")
    if score >=60 and score <70:
        print("You got a D..")
    if score <60:
        print("Get the grade up. You got an F")

#Main
grade()
