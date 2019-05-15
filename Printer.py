class Printer():

    ScanerSpeed = '15'

    def __init__(self,
                 name, printingSpeed, price, printTechnology, costPerPage, country):
        self.name = name
        self.printingSpeed = printingSpeed
        self.price= price
        self.printTechnology = printTechnology
        self.costPerPage = costPerPage
        self.country = country

        def __init__(self):
            print('Constructor called')

        def __del__(self):
            print('Destructor called')

    @staticmethod
    def printScanerSpeed():
     print ('Scaner speed: ' + Printer.ScanerSpeed)

    def __str__(self):
        return ', '.join((f"{name} = {value}" for name, value in self.__dict__.items()))

def main():

    p1 = Printer("Printer 1", 10, 200, 'Laser', 1, 'USA')
    p2 = Printer("Printer 2", 20, 300, 'Jet', 1, 'Ukraine')
    p3 = Printer("Printer 3", 30, 350, 'Jet', 3, 'UK')

    print(p1)
    print(p2)
    print(p3)
    Printer.printScanerSpeed()

if __name__ == '__main__':
    main()