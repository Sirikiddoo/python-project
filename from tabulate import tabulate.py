from tabulate import tabulate


BEDRIJVEN = '/Users/siri/Desktop/OneDrive_1_7-19-2023/bedrijven.txt'

lijst_bedrijven = []   # List to store all companies

def lees_bedrijven():
    """Read the text file with companies"""
    try:
        with open(BEDRIJVEN, mode='r') as bedrijven:
            for record in bedrijven:
                code = record[0:4].strip()
                naam = record[5:25].strip()
                adres = record[25:56].strip()
                plaats = record[67:87].strip()
                Bedrijf(code, naam, adres, plaats)
        print('Bestand', BEDRIJVEN, 'ingelezen')
        return 0
    except FileNotFoundError:
        print('Bestand', BEDRIJVEN, 'niet gevonden')
        return 1
    
def toon_bedrijven(BEDRIJVEN):
    with open(BEDRIJVEN, 'r') as bedrijven:
        data = [line.strip().split(',') for line in bedrijven.readlines()]

    headers = data[0]  # Eerste regel als kolomkoppen
    rows = data[1:]    # Rest van de regels als rijen met gegevens

    print(tabulate(rows, headers=headers, tablefmt='grid'))

# Voorbeeldgebruik:
toon_bedrijven(BEDRIJVEN)
        
class Bedrijf:
    def __init__(self, code, naam='', adres='', plaats=''):
        self.__code = code
        self.__naam = naam
        self.__adres = adres
        self.__plaats = plaats
        self.__bezoekrapporten = []
        lijst_bedrijven.append(self)

    def getCode(self):
        return self.__code

    def setCode(self, code):
        self.__code = code

    def getNaam(self):
        return self.__naam

    def setNaam(self, naam):
        self.__naam = naam

    def getAdres(self):
        return self.__adres

    def setAdres(self, adres):
        self.__adres = adres

    def getPlaats(self):
        return self.__plaats

    def setPlaats(self, plaats):
        self.__plaats = plaats

    def addBezoekrapport(self, bezoekrapport):
        self.__bezoekrapporten.append(bezoekrapport)

    def toonGegevens(self):
        print(self.__code + ' ', self.__naam, self.__adres, self.__plaats)


