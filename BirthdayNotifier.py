import notify2
from datetime import date
dt = date.today()
t = dt.strftime("%d/%b")

notify2.init("Demo application")

f = open("Birthday.txt")
f1 = f.readlines()
try:
    for i in f1:
        n = i.split(":")
        if (n[1] == t):
            n = notify2.Notification("Birthday", "Happy birthday ,{}".format(n[0]))
            n.show()
        else:
            notify2.Notification("No Birthday today").show()
except expression as identifier:
    print(expression)
