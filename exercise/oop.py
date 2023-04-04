print()
print('in the name of Guido van Rossum')
print('-------------------------------')
print()


class Human:
    # Contractor
    def __init__(self, name, partner=None, childs=[]):
        self.name = name
        self.partner = partner
        self.childs = childs

    def getName(self):
        return self.name

    def getPartner(self):
        if self.partner is not None:
            return self.partner
        return None

    def getChilds(self):
        return self.childs

    def setPartner(self, partner):
        self.partner = partner


if __name__ == "__main__":
    # d = Human(str(input("What is Human name: ")))
    # print((d.getData()))

    sarina = Human('sarina')
    pedram = Human('pedram')
    elham = Human('elham', None, [sarina, pedram])
    sohrab = Human('sohrab', elham, [sarina, pedram])
    elham.setPartner(sohrab)

    print('pedran name:', pedram.getName())
    print('elham name:', elham.getName())
    print('elham childes: ', elham.getChilds())

    print('sohrab childes:')
    childrens = elham.getChilds()
    for child in childrens:
        print(child.getName())

    print('sohrab partner:', sohrab.getPartner().getName())
