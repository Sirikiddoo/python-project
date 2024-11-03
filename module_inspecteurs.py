from tabulate import tabulate

# constanten
INSPECTEURS = 'data/inspecteurs.txt'
BEZOEKRAPPORTEN = 'data/bezoekrapporten.txt'

lijst_inspecteurs = []   # lijst met alle inspecteur objecten

def lees_inspecteurs() :
    # tekstbestand met de inspecteursgegevens inlezen
    try :
        with open(INSPECTEURS, mode='r') as inspecteurs_bestand :
            data = [line.strip().split(',') for line in inspecteurs_bestand.readlines()]
        print(f'Bestand {INSPECTEURS} ingelezen')
        return data[1:]  # eerste regel overslaan 
    except FileNotFoundError:
        print(f'Bestand {INSPECTEURS} niet gevonden')
        return []
        

def toon_inspecteurs():
    # bedrijfsgegevens tonen
    try:
        with open(INSPECTEURS, 'r') as inspecteurs:
            data = [regel.strip().split(',') for regel in inspecteurs.readlines()]
        headers = data[0]  # eerste regel als kolomkoppen
        rows = data[1:]    # rest van de regels als rijen met gegevens
        print(tabulate(rows, headers=headers, tablefmt='grid'))
    except FileNotFoundError:
        print(f'Bestand {INSPECTEURS} niet gevonden')



