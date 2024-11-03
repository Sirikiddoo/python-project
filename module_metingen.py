import csv
import numpy as np
import matplotlib.pyplot as plt

# constanten
GASSEN = 'data/gassen.csv'
boetebedrag = 1

# constanten voor berekenen uitstoot
c1 = 1
c2 = 25
c3 = 5
c4 = 1000

# maximum toegestane uitstoot bedrijven
max_uitstoot = {
    "Shell": 30000,
    "ASML": 100000,
    "Tata Steel": 20000,
    "Dow Chemical": 40000,
    "Philips": 100000,
    "TNO": 60000,
}

bedrijven_coördinaten = {
        'Shell': (2, 2),
        'ASML': (14, 22),
        'Tata Steel': (28, 11),
        'Dow Chemical': (44, 55),
        'Philips': (70, 90),
        'TNO': (80, 20)
    }

    
def lees_plot_totaal():
    # totaal van de 4 gassen berekenen en weergeven in numpy array
    gasarray_co2 = np.loadtxt(GASSEN, delimiter=';', skiprows=1, usecols=2).reshape((100, 100))
    gasarray_ch4 = np.loadtxt(GASSEN, delimiter=';', skiprows=1, usecols=3).reshape((100, 100))
    gasarray_no2 = np.loadtxt(GASSEN, delimiter=';', skiprows=1, usecols=4).reshape((100, 100))
    gasarray_nh3 = np.loadtxt(GASSEN, delimiter=';', skiprows=1, usecols=5).reshape((100, 100))

    totaal = c1 * gasarray_co2 + c2 * gasarray_ch4 + c3 * gasarray_no2 + c4 * gasarray_nh3

    print(totaal)
    plt.imshow(totaal)
    plt.colorbar()
    plt.show()


def bereken_bedrijven_uitstoot():
    # totale uitstoot per bedrijf berekenen
    bedrijven_uitstoot = {}

    with open(GASSEN, 'r') as csvfile:
        gas_reader = csv.reader(csvfile, delimiter=';')
        next(gas_reader)  # koptekst overslaan
        
        # voor elk bedrijf en de bijbehorende coördinaten
        for bedrijf, (bx, by) in bedrijven_coördinaten.items():
            totaal_uitstoot = 0

            csvfile.seek(0)  # terug naar het begin van het bestand om opnieuw te lezen
            next(gas_reader)  # opnieuw de koptekst overslaan
            
            # voor elke rij in het metingenbestand
            for row in gas_reader:
                # coördinaten van de rij ophalen
                lat = int(row[0])
                lon = int(row[1])
                # afstand tussen het bedrijf en de huidige coördinaten berekenen
                afstand = abs(lat - bx) + abs(lon - by)

                if afstand == 0:
                    uitstoot_factor = 1.0  # 100% meetellen voor het bedrijf zelf
                elif afstand <= 2:  # 8 omliggende coördinaten
                    uitstoot_factor = 0.5  # 50% meetellen voor omliggende coördinaten
                elif afstand <= 4:  # 16 daaromheenliggende coördinaten
                    uitstoot_factor = 0.25  # 25% meetellen voor daaromheenliggende coördinaten
                else:
                    uitstoot_factor = 0  # niet meetellen voor coördinaten buiten het bereik

                totaal_uitstoot += uitstoot_factor * (c1 * float(row[2]) + c2 * float(row[3]) + c3 * float(row[4]) + c4 * float(row[5]))

            bedrijven_uitstoot[bedrijf] = totaal_uitstoot
            
    print("Totale uitstoot per bedrijf:")
    for bedrijf, uitstoot in bedrijven_uitstoot.items():
        print(f"{bedrijf}: {uitstoot}")

    return bedrijven_uitstoot


def toon_bedrijven_met_boetes(bedrijven_uitstoot):
    # toon bedrijven die een boete krijgen en het bijbehorende boetebedrag
    boetes = {bedrijf: (uitstoot - max_uitstoot.get(bedrijf, 0)) * boetebedrag for bedrijf, uitstoot in bedrijven_uitstoot.items() if uitstoot > max_uitstoot.get(bedrijf, 0)}

    if boetes:
        print("\nBedrijven die een boete krijgen:")
        for bedrijf, boete in boetes.items():
            print(f"{bedrijf}: Boetebedrag €{boete}")
    else:
        print("\nGeen bedrijven krijgen een boete.")        


def toon_hoge_waarden():
    # zoek hoge waarden in het metingenbestand en toon de bijbehorende gegevens
    hoge_waarden = []

    # open het metingenbestand en zoek naar hoge waarden
    with open(GASSEN, 'r') as csvfile:
        gas_reader = csv.reader(csvfile, delimiter=';')
        next(gas_reader)  # koptekst overslaan

        for row in gas_reader:
            # controleren of de waarde hoger is dan 2000 in kolom 3
            if float(row[2]) > 2000:
                # coördinaten van het punt
                x, y = int(row[0]), int(row[1])

                # check of de coördinaten niet overeenkomen met bedrijfslocaties
                if (x, y) not in [(loc[1][0], loc[1][1]) for loc in bedrijven_coördinaten.items()]:
                    # hoge waarde samen met bijbehorende gegevens toevoegen aan de lijst
                    hoge_waarden.append([row[0], row[1], *row[2:6]])

    # toon de gevonden hoge waarden en bijbehorende gegevens
    if hoge_waarden:
        print("Onbekende bedrijf met hoge uitstoot:")
        for waarden in hoge_waarden:
            print(f"Coördinaten: {waarden[0]}, {waarden[1]}, CO2: {waarden[2]}, CH4: {waarden[3]}, NO2: {waarden[4]}, NH3: {waarden[5]}")
    else:
        print("Er zijn geen rijen met hoge waarden gevonden.")





