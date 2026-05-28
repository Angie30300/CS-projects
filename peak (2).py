#Angela Mercado
#Peaks

#Init
import random
dataset = []
for i in range(12):
    dataset.append(random.randint(0,99))

#Functions
def peakks():
#if 1st num greater and 2nd
        if dataset[0] > dataset[1]:
            print(f"Peak detected: Value is {dataset[0]} at index 0")
        if dataset[1] > dataset [2] and dataset[1] > dataset[0]:
            print(f"Peak detected: Value is {dataset[1]} at index 1")
        if dataset[2] > dataset [3] and dataset[2] > dataset[1]:
            print(f"Peak detected: Value is {dataset[2]} at index 2")
        if dataset[3] > dataset [4] and dataset[3] > dataset[2]:
            print(f"Peak detected: Value is {dataset[3]} at index 3")
        if dataset[4] > dataset [5] and dataset[4] > dataset[3]:
            print(f"Peak detected: Value is {dataset[4]} at index 4")
        if dataset[5] > dataset [6] and dataset[5] > dataset[4]:
            print(f"Peak detected: Value is {dataset[5]} at index 5")
        if dataset[6] > dataset [7] and dataset[6] > dataset[5]:
            print(f"Peak detected: Value is {dataset[6]} at index 6")
        if dataset[7] > dataset [8] and dataset[7] > dataset[6]:
            print(f"Peak detected: Value is {dataset[7]} at index 7")
        if dataset[8] > dataset [9] and dataset[8] > dataset[7]:
            print(f"Peak detected: Value is {dataset[8]} at index 8")
        if dataset[9] > dataset [10] and dataset[9] > dataset[8]:
            print(f"Peak detected: Value is {dataset[9]} at index 9")
        if dataset[10] > dataset [11] and dataset[10] > dataset[9]:
            print(f"Peak detected: Value is {dataset[10]} at index 10")
        if dataset[11] > dataset[10]:
            print(f"Peak detected: Value is {dataset[11]} at index 11")




def loop():

    if dataset[11] > dataset[10]:
        print(f"Peak detected: Value is {dataset[11]} at index 11")

    for i in range(11):
        if dataset[i] > dataset[i + 1] and dataset[i] > dataset [i - 1]:
            print(f"Peak detected: Value is {dataset[i]} at index {i}")

#Main
loop()
