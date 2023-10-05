from battle import battlesim
from army import Units, Order, Army

class ann50(battlesim):
    def __init__(self):
        self.lst = Units()
        self.lst.addUnit('Infantry', 'land', 1, 2, 3)
        self.lst.addUnit('Artillery', 'land', 2, 2, 4)
        self.lst.addUnit('Tank', 'land', 3, 3, 5)
        self.lst.addUnit('Fighter', 'air', 3, 4, 10)
        self.lst.addUnit('Bomber', 'air', 4, 1, 12)
        self.lst.addUnit('Battleship', 'sea', 4, 4, 20, 2)
        self.lst.addUnit('Aircraft Carrier', 'sea', 1, 2, 14)
        self.lst.addUnit('Cruiser', 'sea', 3, 3, 12)
        self.lst.addUnit('Destroyer', 'sea', 2, 2, 8)
        self.lst.addUnit('Submarine', 'sea', 2, 1, 6)
