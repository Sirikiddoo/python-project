import module_bedrijven as mbd
import module_inspecteurs as mi
import module_bezoekrapporten as mb
import module_metingen as mm

# menufunctie met inlezen van gegevens en submenu's voor alle onderdelen van de applicatie

def lees_gegevens():
    mi.lees_inspecteurs()
    mb.lees_bezoekrapporten()
    mbd.lees_bedrijven()

def toon_hoofdmenu():
    print("Hoofdmenu:")
    print("1. Metingen")
    print("2. Inspecteurs")
    print("3. Bedrijven")
    print("4. Bezoekrapporten")
    print("5. Afsluiten")

def toon_metingen_menu():
    print("Metingen:")
    print("1. Plot gegevens")
    print("2. Bereken totale uitstoot")
    print("3. Bereken boetes")
    print("4. Terug naar hoofdmenu")

def toon_inspecteurs_menu():
    print("Inspecteurs:")
    print("1. Toon overzicht met inspecteurs")
    print("2. Terug naar hoofdmenu")

def toon_bedrijven_menu():
    print("Bedrijven:")
    print("1. Toon overzicht met bedrijven")
    print("2. Toon onbekende bedrijf")
    print("3. Terug naar hoofdmenu")

def toon_rapporten_menu():
    print("Bezoekrapporten:")
    print("1. Op inspecteurscode")
    print("2. Op bedrijf")
    print("3. Terug naar hoofdmenu")

def main():
    lees_gegevens() 

    while True:
        toon_hoofdmenu()
        keuze = input("Kies een optie: ")

        if keuze == '1': # submenu metingen met keuze voor het inlezen en plotten van data, berekenen van de uitstoot en boetes
            while True:
                toon_metingen_menu()
                metingen_keuze = input("Kies een optie: ")
                if metingen_keuze == '1':
                    mm.lees_plot_totaal()
                elif metingen_keuze == '2':
                    mm.bereken_bedrijven_uitstoot()
                elif metingen_keuze == '3':
                    bedrijven_uitstoot = mm.bereken_bedrijven_uitstoot()
                    mm.toon_bedrijven_met_boetes(bedrijven_uitstoot)
                elif metingen_keuze == '4':
                    break
                else:
                    print("Ongeldige keuze. Probeer opnieuw.")

        elif keuze == '2': # submenu inspecteurs met keuze om overzicht van inspecteurs weer te geven
            while True:
                toon_inspecteurs_menu()
                inspecteur_keuze = input("Kies een optie: ")
                if inspecteur_keuze == '1':
                    mi.toon_inspecteurs()
                elif inspecteur_keuze == '2':
                    break
                else:
                    print("Ongeldige keuze. Probeer opnieuw.")

        elif keuze == '3': # submenu bedrijven met keuze om overzicht van bedrijven weer te geven, en ook het onbekende bedrijf te tonen
            while True:
                toon_bedrijven_menu()
                bedrijf_keuze = input("Kies een optie: ")
                if bedrijf_keuze == '1':
                    mbd.toon_bedrijven()
                elif bedrijf_keuze == '2':
                    mm.toon_hoge_waarden()
                elif bedrijf_keuze == '3':
                    break
                else:
                    print("Ongeldige keuze. Probeer opnieuw.")

        elif keuze == '4': # submenu bezoekrapporten met weergave op inspecteur of bedrijf
            # lijsten met geldige inspecteurscodes, bedrijfscodes en bedrijfsnamen
            geldige_inspecteurscodes = ['001', '002', '003', '004', '005']
            geldige_bedrijfscodes = ['0001', '0002', '0003', '0004', '0005', '0006']
            geldige_bedrijfsnamen = ['Shell', 'ASML', 'Tata Steel', 'Dow Chemical', 'Philips', 'TNO']



            while True:
                toon_rapporten_menu()
                rapport_keuze = input("Kies een optie: ")
                if rapport_keuze == '1':
                    while True:
                        inspecteurscode = input("Voer de code van de inspecteur in: ")
                        if inspecteurscode in geldige_inspecteurscodes:
                            met_data = input("Wilt u een begin- en einddatum invoeren? (ja/nee): ").lower()
                            if met_data == 'ja':
                                start_datum = input("Voer de begindatum in (DD-MM-YYYY): ")
                                eind_datum = input("Voer de einddatum in (DD-MM-YYYY): ")
                                mb.bekijk_rapporten_per_datum(inspecteurscode, start_datum, eind_datum)
                                break
                            elif met_data == 'nee':
                                mb.bekijk_rapporten_per_inspecteur(inspecteurscode)
                                break
                            else:
                                print("Ongeldige keuze. Voer 'ja' of 'nee' in.")
                        else:
                            print("Ongeldige inspecteurscode. Probeer opnieuw.")
                    break  
                elif rapport_keuze == '2':
                    while True:
                        bedrijf_input = input("Voer een bedrijfscode of bedrijfsnaam in: ")
                        if bedrijf_input in geldige_bedrijfscodes or geldige_bedrijfsnamen:
                            mb.bekijk_rapporten_per_bedrijf(bedrijf_input)
                            break
                        else:
                            print("Ongeldige invoer. Voer een geldige bedrijfscode of bedrijfsnaam in.")
                            continue
                    break  


        elif keuze == '5':
            print("Applicatie wordt afgesloten.")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

if __name__ == "__main__":
    main()
