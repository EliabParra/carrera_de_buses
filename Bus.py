import random as r
import os
import time

class Bus:
    self.variable = 0
    def __init__(self, bus1, bus2):
        self.nombre1 = bus1
        self.nombre2 = bus2
        self.inicioCarrera()
        
    def clearConsole():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def inicioCarrera(self, n1 = 0, n2 = 0):
        print("Iniciando carrera de buses")
        print("-" * 155)
        print(self.drawBuses(n1, n2))
        time.sleep(1)
        
        while n1 < 100 or n2 < 100:
            self.variable = r.randint(1, 2)
            if self.variable == 1:
                n1 += 1
                self.clearConsole()
            

        self.clearConsole()
        print("Terminando carrera de buses")
        print("-" * 155)

    def drawBuses(self, n1, n2):
        output = []
        output.append((n1 * " ") + "_______________  " + ((100 - n1) * " ") + "|")
        output.append((n1 * " ") + "|__|__|__|__|__|___ " + ((97  - n1) * " ") + "|")
        output.append((n1 * " ") + "|    "+ self.nombre1 +"        |)" + ((96  - n1) * " ") + "|")
        output.append((n1 * " ") + "|~~~@~~~~~~~~~@~~~|)" + ((95  - n1) * " ") + "|")
        output.append(155 * "_")
        output.append((n2 * " ") + "_______________  " + ((100 - n2) * " ") + "|")
        output.append((n2 * " ") + "|__|__|__|__|__|___ " + ((97  - n2) * " ") + "|")
        output.append((n2 * " ") + "|    "+ self.nombre2 +"     |)" + ((96  - n2) * " ") + "|")
        output.append((n2 * " ") + "|~~~@~~~~~~~~~@~~~|)" + ((95  - n2) * " ") + "|")
        output.append(155 * "_")
        return "\n".join(output)