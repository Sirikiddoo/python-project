from tabulate import tabulate

# constanten
BEDRIJVEN = 'data/bedrijven.txt'
BEZOEKRAPPORTEN = 'data/bezoekrapporten.txt'

lijst_bedrijven = []   # lijst met alle bedrijf objecten

def lees_bedrijven():
    # tekstbestand met bedrijfsgegevens inlezen
    try:
        with open(BEDRIJVEN, mode='r') as bedrijven:
            data = [record.strip().split(',') for record in bedrijven.readlines()]
        print(f'Bestand {BEDRIJVEN} ingelezen')
        return data[1:]  # eerste regel overslaan 
    except FileNotFoundError:
        print(f'Bestand {BEDRIJVEN} niet gevonden')
        return 1

def toon_bedrijven():
    # bedrijfsgegevens tonen
    try:
        with open(BEDRIJVEN, 'r') as bedrijven:
            data = [regel.strip().split(',') for regel in bedrijven.readlines()]
        headers = data[0]  # eerste regel als kolomkoppen
        rows = data[1:]    # rest van de regels als rijen met gegevens
        print(tabulate(rows, headers=headers, tablefmt='grid'))
    except FileNotFoundError:
        print(f'Bestand {BEDRIJVEN} niet gevonden')


