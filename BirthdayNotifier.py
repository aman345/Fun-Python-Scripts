import notify2
from datetime import date
import logging

#capturing current date and formating it 
dt = date.today()
t = dt.strftime("%d/%b")

notify2.init("Birthday Reminder  application")

#file source
f = open("Your birthday txt file here")
f1 = f.readlines()

try:
    for i in f1:
        print("here in loop")
        n = i.split(":")
        if (n[1].strip("\n") == t):
            notify2.Notification("Birthday", "Happy birthday ,{}".format(n[0])).show() 
except:
    print("Error occured while reading file....")
