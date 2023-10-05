from army import Units, Order, Army
import random

class battlesim:
    def __init__(self):
        self.lst = Units()
        #placeholder for function override
    def getUnits(self):
        return lst
    def expectedAttack(self, army):
        trps = army.getTroops
        xpect1 = 0
        for key in trps:
            xpect2 += (1/6 * trps[key] * self.lst.getAttack(key))
        xpect2 = xpect1 % 1
        xpect1 -= xpect2
        if random.random() < xpect1:
            xpect2 += 1 #to insure that there are no infinite battles (like between two singular infantryment)
        return xpect2
    def expectedDefense(self, army):
        trps = army.getTroops
        xpect1 = 0
        for key in trps:
            xpect2 += (1/6 * trps[key] * self.lst.getDefense(key))
        xpect2 = xpect1 % 1
        xpect1 -= xpect2
        if random.random() < xpect1:
            xpect2 += 1
        return xpect2
    def randomAttack(self, army):
        pass
    def randomDefense(self, army):
        pass
