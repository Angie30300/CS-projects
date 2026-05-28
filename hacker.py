#Angela M
#Hacker

#Init
import pandas as pd

data = pd.read_csv('hacker.csv')

logID = data['Log_ID'].tolist()
IPadd = data['IP_Address'].tolist()
protocol = data['Protocol'].tolist()
KBdata = data['Data_KB'].tolist()
time = data['Time'].tolist()
description = data['Description'].tolist()
filter = []

#Functions
def hacker(fail):
    for i in range(len(logID)):
        if fail in description[i]:
            filter.append(i)


    print(filter)
    filter.clear()

def datastolen(kb):
    for i in range(len(logID)):
        if KBdata <= kb:
            filter.append

#Main
hacker('Failed Login Attempt')
print(data.loc[[196]])

