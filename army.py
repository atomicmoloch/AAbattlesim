
class Units:
    def __init__(self):
        self.units = {}
    def addUnit(self, name, typ, attk, defce, cost, hp=1):#typ should only be land, air, or sea
        self.units[name] = [typ, attk, defce, cost, hp]
    def removeUnit(self, name):
        del self.units[name]
    def sortByLowest(self, var):#var = 1 for attk, 2 for defce, 3 for cost
        tUnits = self.units.copy()
        lOrder = []
        while len(tUnits) > 0:
            minV = 9999 #Inelegant, I know, but python ints are unbounded
            minK = ''
            for key in tUnits:
                if tUnits[key][var] < minV:
                    minV, minK = tUnits[key][var], key
            lOrder.append(minK)
            del tUnits[minK]
        return lOrder
    def sortByHighest(self, var):#var = 1 for attk, 2 for defce, 3 for cost
        tUnits = self.units.copy()
        hOrder = []
        while len(tUnits) > 0:
            maxV = -9999
            maxK = ''
            for key in tUnits:
                if tUnits[key][var] > maxV:
                    maxV, maxK = tUnits[key][var], key
            hOrder.append(maxK)
            del tUnits[maxK]
        return hOrder
    def getTwoHp(self):
        tHP = []
        for key in self.units:
            if self.units[key][4] > 1:
                tHP.append(key)
        return tHP
    def getType(self, name):
        return (self.units[name])[0]
    def getAttack(self, name):
        return (self.units[name])[1]
    def getDefence(self, name):
        return (self.units[name])[2]
    def getCost(self, name):
        return (self.units[name])[3]

class Order:
    def __init__(self, uniclass):
        self.units = uniclass
        self.order = self.units.sortByLowest(3)
        self.tworder = self.units.getTwoHP()
    def sort(self, low, attkdef):
        if low:
            self.order = self.units.sortByLowest(attkdef)
        else:
            self.order = self.units.sortByHighest(attkdef)
    def moveUp(self, name):
        x = self.order.index(name)
        if x > 0:
            self.order.remove(x)
            self.order.insert(x - 1, name)
    def moveDown(self, name):
        x = self.order.index(name)
        if x < (len(self.order) - 1):
            self.order.remove(x)
            self.order.insert(x + 1, name)
    def moveUpthp(self, name):
        x = self.tworder.index(name)
        if x > 0:
            self.tworder.remove(x)
            self.tworder.insert(x - 1, name)
    def getOrder(self):
        return self.order
    def getTworder(self):
        return self.tworder

class Army:
    def __init__(self, uniclass):
        self.troops = {}
        self.twohptroops = {}
        self.units = uniclass
        self.order = Order(uniclass)
    def BuildTwoHp(self): #might be unused in the final
        tHP = self.units.getTwoHp
        for x in tHP:
            if x in self.troops:
                self.twohptroops[x] = self.troops[x]
    def addTwoHp(self, name):
        if name in self.twohptroops:
            self.twohptroops[name] = self.twohptroops[name] + 1
        else:
            self.twphotroops[name] = 1
    def addTroop(self, name):
        if name in self.troops:
            self.troops[name] = self.troops[name] + 1
        else:
            self.troops[name] = 1
        if name in self.units.getTwoHp():
            self.addTwoHp(name)
    def removeUnit(self):
        thporder = self.order.getTworder()
        for x in thporder: #presently always removes all second hp before removing any units, might change
            if x in self.twohptroops:
                self.twohptroops[x] = self.twohptroops[x] - 1
                if self.twohptroops[x] == 0:
                    del self.twohptroops[x]
                return [x, 0]
        onorder = self.order.getOrder()
        for x in onorder:
            if x in self.troops:
                self.troops[x] = self.troops[x] - 1
                if self.troops[x] == 0:
                    del self.troops[x]
                return [x, (self.troops[x])[3]]
        return 0
    def removeType(self, typ): #removes all land, air, or sea units
        for key in self.troops:
            if (self.units.getType(key)) == typ:
                del self.troops[key]
        for key in self.twohptroops:
            if (self.units.getType(key)) == typ:
                del self.twohptroops[key]
    def getTroops(self):
        return self.troops


