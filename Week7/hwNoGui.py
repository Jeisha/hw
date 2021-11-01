import time
import threading
import random
import names
from queue import Queue
import pandas as pd

cusQ = Queue(maxsize = 60)
simTime = 0
simEnd = 20
done = []

class IceCreamServer(threading.Thread):
  def __init__(self, ID):
    threading.Thread.__init__(self)
    self.ID = ID
    self.busy = False
    self.customer = None

  def run(self):
    global cusQ, simTime, simEnd
    while simTime < simEnd:

      if self.busy:
        if self.customer.status == IceCreamCustomer.DONE:
          self.busy = False
          self.customer = None

      if not self.busy:

        if not cusQ.empty():
          self.customer = cusQ.get()
          self.customer.status = IceCreamCustomer.SERVED
          self.busy = True


class IceCreamCustomer(threading.Thread):
  IN_QUEUE = 0
  SERVED = 1
  DONE = 2

  def __init__(self, name, numIceCream):
    threading.Thread.__init__(self)
    self.name = name
    self.numIceCream = numIceCream
    self.status = IceCreamCustomer.IN_QUEUE
  
  def run(self):
    
    while self.status != IceCreamCustomer.DONE:

      if self.status == IceCreamCustomer.IN_QUEUE :
        continue

      if self.status == IceCreamCustomer.SERVED :
        for ice in range(self.numIceCream):
          time.sleep(0.5)
          print('{0} decided on flavor for ice cream {1}.'.format(self.name,ice+1))
        self.status = IceCreamCustomer.DONE

queLength = []
server = []
servers = input('Number of ice cream servers: ')
for i in range(int(servers)):
  server.append(IceCreamServer(i))
  server[i].start()
  done.append(server[i])


while simTime < simEnd:
  print('Period =',simTime)
  numCustomer = random.randint(0,3)
  for c in range(numCustomer):
    cusObj = IceCreamCustomer(names.get_first_name(), 3)
    cusQ.put(cusObj)
    cusObj.start()
  
  simTime += 1
  queLength.append(cusQ.qsize())

df = pd.DataFrame(queLength, columns = ['qLength'])
df.to_csv('data.csv')