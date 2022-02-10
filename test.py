from library.src._check_filename import check_filename
from library.src._read_data import read_data
from library.src._analize_data import analize_data
from library.src._export_data import export_data

def menu():
    print("MAIN MENU")
    print("1. Wczytaj dane")
    print("2. Analizuj dane")
    print("3. Zapisz wyniki analizy w pliku")
    print("4. Wyjscie z programu")
    opcja = int(input("Wybierz opcje [1-4]: "))
    while opcja < 1 or opcja > 4:
        print("Wybrano niepoprawna opcje.")
        print("MAIN MENU")
        print("1. Wczytaj dane")
        print("2. Analizuj dane")
        print("3. Zapisz wyniki analizy w pliku")
        print("4. Wyjscie z programu")
        opcja = int(input("Wybierz ponownie opcje [1-4]: "))
    return opcja


if __name__ == "__main__":
    dane = None
    wyniki_analizy = None
    opcja = menu()
    while opcja != 4:
        if opcja == 1:
            filename = input("Wprowadz sciezke do pliku (albo [ENTER] aby powrocic do menu glownego): ")
            while filename != '' and not check_filename(filename):
                filename = input("Wprowadz ponownie sciezke do pliku (albo [ENTER] aby powrocic do menu glownego): ")
            if filename != '':
                dane = read_data(filename)
        elif opcja == 2:
            if dane is None:
                print("Nie wczytano zadnego pliku z danymi.")
            else:
                wyniki_analizy = analize_data(dane)
        elif opcja == 3:
            if wyniki_analizy is None:
                print("Nie przeanalizowano zadnych plikow z danymi.")
            else:
                filename = input("Wprowadz sciezke do pliku (albo [ENTER] aby powrocic do menu glownego): ")
                if filename != '':
                    if export_data(wyniki_analizy, filename):
                        print(f"Dane zostaly poprawnie zapisane do pliku {filename}")
                    else:
                        print(f"Dane NIE zostaly poprawnie zapisane do pliku {filename}")
        opcja = menu()

    print("Koniec programu...")
