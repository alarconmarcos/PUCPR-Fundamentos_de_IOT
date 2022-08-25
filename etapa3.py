import dht
import machine
import time

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)
bstatus = False

while True:
    d.measure()
    print("Temperatura = {}     Umidade = {}".format(d.temperature(), d.humidity()))
    if d.temperature() > 31 or d.humidity() > 70:
        r.value(1)
        
        if bstatus == False:
          print()
          print("Muito calor, ligando o Ar Condicionado!")
          print()
          bstatus = True
    else:
        r.value(0)
    
        if bstatus == True:
          print()
          print("Refrescou um pouco, o Ar Condicionado foi desligado!")
          print()
          bstatus = False

    time.sleep(5)
