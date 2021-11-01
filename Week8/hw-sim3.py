import threading
import time
import random
from tkinter import *
import names as name
from math import *

window = Tk()
simTime = 0
simEnd = 20
cusIndex = 0
appWidth = 1000
appHeight = 500
m1 = 5
m2 = 1
v1 = 1
v2 = -1
l1 = 50
l2 = 50
fillColor = ['red', 'blue', 'black', 'green', 'grey']

window.title("Homework week 8 class - sim3.py")
canvas = Canvas(window, width=appWidth, height=appHeight, bg="white")
canvas.grid(row=0,column=0)


class IceCreamCustomer(threading.Thread):

    def __init__(self, name, iceCreamBrand, reputation, display):
        threading.Thread.__init__(self)
        self.name = name
        self.iceCreamBrand = iceCreamBrand
        self.reputation = reputation
        self.display = display
        print('Customer ', self.name, ' created')

    def run(self):
        global simTime, simEnd

        while simTime < simEnd:
            time.sleep(1)

canvas.create_line(580, 210, 950, 210)
canvas.create_line(580, 280, 950, 280)
numCustomers = 5
offset = 35
for c in range(numCustomers):
    custDisp = canvas.create_oval(offset+550,220, offset+600,270, fill=random.choice(fillColor))
    # canvas.create_oval()
    cusObj = IceCreamCustomer(name.get_first_name(), random.randint(1, 5), random.randint(1, 10),custDisp)
    cusIndex = cusIndex + 1
    offset += 60
    cusObj.start()

# simulation loop
while simTime < simEnd:
    # increment simulation time
    simTime = simTime + 1
    time.sleep(1)
    window.update()

window.mainloop()