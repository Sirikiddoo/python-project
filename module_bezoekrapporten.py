from datetime import datetime
from tabulate import tabulate

# Constanten
BEZOEKRAPPORTEN = 'data/bezoekrapporten.txt'

def lees_bezoekrapporten():
    # tekstbestand met de bezoekrapporten inlezen
    try:
        with open(BEZOEKRAPPORTEN, mode='r') as rapporten:
            data = [record.strip().split(',') for record in rapporten.readlines()]
        print(f'Bestand {BEZOEKRAPPORTEN} ingelezen')
        return data[1:]  # eerste regel overslaan 
    except FileNotFoundError:
        print('Bestand', BEZOEKRAPPORTEN, 'niet gevonden')
        return 1


def bekijk_rapporten_per_inspecteur(inspecteurscode):
    # bezoekrapporten bekijken op basis van inspecteur
    try:
        # dictionary met de koppeling tussen inspecteurscodes en inspecteursnamen
        inspecteurs_namen = {'001': 'Piet Precies', '002': 'Bob de Bouwer', '003': 'Jan Groen', '004': 'Sarah Secuur', '005': 'Lisa Losjes'}

        # dictionary met de koppeling tussen bedrijfscodes en bedrijfsnamen
        bedrijfsnamen = {'0001': 'Shell', '0002': 'ASML', '0003': 'Tata Steel', '0004': 'Dow Chemical', '0005': 'Philips', '0006': 'TNO'}

        # open het tekstbestand met bezoekrapporten
        with open(BEZOEKRAPPORTEN, 'r') as file:
            gevonden_rapporten = False

            # lijst om alle gevonden rapporten op te slaan
            rapporten = []

            for regel in file:
                parts = regel.strip().split()
                if parts:
                    huidige_inspecteurscode = parts[0]  # eerste element is de inspecteurscode
                    huidige_bedrijfscode = parts[1]  # tweede element is de bedrijfscode

                    # controleer of de inspecteurscode overeenkomt met de opgegeven inspecteurscode
                    if huidige_inspecteurscode == inspecteurscode:
                        gevonden_rapporten = True

                        titels = ["Inspecteursnaam:", "Bedrijfsnaam:", "Bezoekdatum:", "Rapportdatum:", "Status:", "Opmerkingen:"]
                        rapport_info = regel.strip().split()

                        # vervang de inspecteurscode door de inspecteursnaam
                        inspecteursnaam = inspecteurs_namen.get(inspecteurscode, inspecteurscode)  # als de inspecteursnaam niet in de dictionary staat, gebruik de code
                        rapport_info[0] = inspecteursnaam

                        # vervang de bedrijfscode door de bedrijfsnaam
                        bedrijfsnaam = bedrijfsnamen.get(huidige_bedrijfscode, huidige_bedrijfscode)  # als de bedrijfsnaam niet in de dictionary staat, gebruik de code
                        rapport_info[1] = bedrijfsnaam

                        rapporten.append(["Bezoekrapport", "Gegevens"])
                        for titel, info in zip(titels, rapport_info):
                            rapporten.append([titel, info])
                        # lege regel toevoegen tussen de rapporten
                        rapporten.append(["", ""])

            if not gevonden_rapporten:
                print("Geen bezoekrapporten gevonden voor de opgegeven inspecteurscode.")
            else:
                print(tabulate(rapporten, tablefmt="grid"))

    except FileNotFoundError:
        print("Het tekstbestand met bezoekrapporten is niet gevonden.")
    except Exception as e:
        print("Er is een fout opgetreden:", e)



def bekijk_rapporten_per_datum(inspecteurscode, start_datum, eind_datum):
    # bezoekrapporten bekijken op basis van inspecteur en data
    try:
        # dictionary met de koppeling tussen inspecteurscodes en inspecteursnamen
        inspecteurs_namen = {'001': 'Piet Precies', '002': 'Bob de Bouwer', '003': 'Jan Groen', '004': 'Sarah Secuur', '005': 'Lisa Losjes'}

        # dictionary met de koppeling tussen bedrijfscodes en bedrijfsnamen
        bedrijfsnamen = {'0001': 'Shell', '0002': 'ASML', '0003': 'Tata Steel', '0004': 'Dow Chemical', '0005': 'Philips', '0006': 'TNO'}

        # start- en einddatum omzetten naar datetime-objecten
        start_datum = datetime.strptime(start_datum, "%d-%m-%Y")
        eind_datum = datetime.strptime(eind_datum, "%d-%m-%Y")

        # open het tekstbestand met bezoekrapporten
        with open(BEZOEKRAPPORTEN, 'r') as file:
            gevonden_rapporten = False

            # lijst om alle gevonden rapporten op te slaan
            rapporten = []

            for regel in file:
                parts = regel.strip().split()
                if parts:
                    huidige_inspecteurscode = parts[0]  # eerste element is de inspecteurscode
                    bezoekdatum = datetime.strptime(parts[2], "%d-%m-%Y")

                    # controleer of de inspecteurscode overeenkomt met de opgegeven inspecteurscode en of de bezoekdatum binnen het opgegeven bereik ligt
                    if huidige_inspecteurscode == inspecteurscode and start_datum <= bezoekdatum <= eind_datum:
                        gevonden_rapporten = True

                        titels = ["Inspecteursnaam:", "Bedrijfsnaam:", "Bezoekdatum:", "Rapportdatum:", "Status:", "Opmerkingen:"]
                        rapport_info = regel.strip().split()

                        # inspecteurscode door de inspecteursnaam vervangen
                        inspecteursnaam = inspecteurs_namen.get(inspecteurscode, inspecteurscode)  # als de inspecteursnaam niet in de dictionary staat, gebruik de code
                        rapport_info[0] = inspecteursnaam

                        # bedrijfscode door de bedrijfsnaam vervangen
                        bedrijfsnaam = bedrijfsnamen.get(rapport_info[1], rapport_info[1])  # als de bedrijfsnaam niet in de dictionary staat, gebruik de code
                        rapport_info[1] = bedrijfsnaam

                        # titels en gegevens toevoegen aan de lijst met gevonden rapporten
                        rapporten.append(["Bezoekrapport", "Gegevens"])
                        for titel, info in zip(titels, rapport_info):
                            rapporten.append([titel, info])
                        # lege regel toevoegen tussen de rapporten
                        rapporten.append(["", ""])

            # als er geen bezoekrapporten zijn gevonden voor de opgegeven inspecteurscode en datumbereik
            if not gevonden_rapporten:
                print("Geen bezoekrapporten gevonden voor de opgegeven inspecteurscode en datumbereik.")
            else:
                print(tabulate(rapporten, tablefmt="grid"))

    except FileNotFoundError:
        print("Het tekstbestand met bezoekrapporten is niet gevonden.")
    except ValueError:
        print("Ongeldig datum formaat. Voer de datum in als DD-MM-JJJJ.")
    except Exception as e:
        print("Er is een fout opgetreden:", e)



def bekijk_rapporten_per_bedrijf(bedrijf_input):
    # bezoekrapporten bekijken op basis van bedrijf
    try:
        # dictionary met de koppeling tussen inspecteurscodes en inspecteursnamen
        inspecteurs_namen = {'001': 'Piet Precies', '002': 'Bob de Bouwer', '003': 'Jan Groen', '004': 'Sarah Secuur', '005': 'Lisa Losjes'}

        # dictionary met de koppeling tussen bedrijfsnamen en bedrijfscodes
        bedrijfsnamen = {'Shell': '0001', 'ASML': '0002', 'Tata Steel': '0003', 'Dow Chemical': '0004', 'Philips': '0005', 'TNO': '0006'}

        # als de gebruiker een bedrijfsnaam heeft ingevoerd
        if bedrijf_input in bedrijfsnamen:
            bedrijfscode = bedrijfsnamen[bedrijf_input]
        # als de gebruiker een bedrijfscode heeft ingevoerd
        elif bedrijf_input in bedrijfsnamen.values():
            bedrijfscode = bedrijf_input
        else:
            print("Ongeldige invoer. Voer een geldige bedrijfscode of bedrijfsnaam in.")
            return

        with open(BEZOEKRAPPORTEN, 'r') as file:
            gevonden_rapporten = False

            # lijst om alle gevonden rapporten op te slaan
            rapporten = []

            # loop door elke regel van het tekstbestand
            for regel in file:
                parts = regel.strip().split()
                if parts and len(parts) >= 2:
                    huidige_bedrijfscode = parts[1]  # tweede element is de bedrijfscode

                    # controleer of de bedrijfscode overeenkomt met de opgegeven bedrijfscode
                    if huidige_bedrijfscode == bedrijfscode:
                        gevonden_rapporten = True

                        titels = ["Inspecteursnaam:", "Bedrijfsnaam:", "Bezoekdatum:", "Rapportdatum:", "Status:", "Opmerkingen:"]
                        rapport_info = regel.strip().split()

                        # bedrijfscode door de bedrijfsnaam vervangen
                        bedrijfsnaam = next((key for key, value in bedrijfsnamen.items() if value == huidige_bedrijfscode), huidige_bedrijfscode)
                        rapport_info[1] = bedrijfsnaam

                        # inspecteurscode door de inspecteursnaam vervangen
                        inspecteurscode = rapport_info[0]
                        inspecteursnaam = inspecteurs_namen.get(inspecteurscode, inspecteurscode)  # als de inspecteursnaam niet in de dictionary staat, gebruik de code
                        rapport_info[0] = inspecteursnaam

                        rapporten.append(["Bezoekrapport", "Gegevens"])
                        for titel, info in zip(titels, rapport_info):
                            rapporten.append([titel, info])
                        # lege regel toevoegen tussen de rapporten
                        rapporten.append(["", ""])

            # als er geen bezoekrapporten zijn gevonden voor de opgegeven bedrijfscode
            if not gevonden_rapporten:
                print(f"Geen bezoekrapporten gevonden voor het bedrijf met code '{bedrijfscode}'.")
            else:
                print(tabulate(rapporten, tablefmt="grid"))

    except FileNotFoundError:
        print("Het tekstbestand met bezoekrapporten is niet gevonden.")
    except Exception as e:
        print("Er is een fout opgetreden:", e)
