def main():
    zadania = []



    while True:
        print("\n=== MENU GŁÓWNE ===")
        print("1. Dodaj Zadanie")
        print("2. Usuń Zadanie")
        print("3. Oznacz zadanie jako wykonane")
        print("4. Dodaj notatkę")
        print("5. Wyświetl listę zadań")
        print("6. Wyświetl listę notatek")
        print("7. Wyjście")

        wybor = input("Wybierz Opcję (1-7): ")
        

        if wybor == "1":
            zadanie = input("Podaj treść zadania: ")
            zadania.append({"opis": zadanie, "wykonane": False, "notatki": []})
            print(f"Zadanie '{zadanie}' zostało dodane.")
        elif wybor == "2":
            if zadania:
                print("Wybierz numer zadania do usunięcia:")
                for idx, zadanie in enumerate(zadania, 1):
                    status = "V" if zadanie["wykonane"] else "X"
                    print(f"{idx}. {zadanie['opis']} [{status}]")
                try:
                    numer_zadania = int(input("Podaj numer zadania do usunięcia: "))
                    if 1 <= numer_zadania <= len(zadania):
                        usuniete_zadanie = zadania.pop(numer_zadania - 1)
                        print(f"Zadanie '{usuniete_zadanie['opis']}' zostało usunięte")
                    else:
                        print("Nie ma takiego zadania")
                except ValueError:
                    print("Proszę podać prawidłowy numer.")
            else:
                print("Brak zadań do usunięcia.")
        elif wybor == "3":
            if zadania:
                print("Wybierz numer zadania do oznaczenia jako wykonane: ")
                for idx, zadanie in enumerate(zadania, 1):
                    status = "V" if zadanie["wykonane"] else "X"
                    print(f"{idx}. {zadanie['opis']} [{status}]")
                try:
                    numer_zadania = int(input("Podaj numer zadania do oznaczenia jako wykonane: "))
                    if 1 <= numer_zadania <= len(zadania):
                        zadania[numer_zadania - 1]["wykonane"] = True
                        print(f"Zadanie '{zadania[numer_zadania - 1]['opis']}' zostało oznaczone jako wykonane.")
                    else:
                        print("Nie ma takiego zadania")
                except ValueError:
                    print("Proszę podać prawidłowy numer")
            else:
                print("Brak zadań do oznaczenia.")
        elif wybor == "4":
            if zadania:
                print("Wybierz numer zadania, do którego chcesz dodać notatkę: ")
                for idx, zadanie in enumerate(zadania, 1):
                    print(f"{idx}. {zadanie['opis']}")
                try:
                    numer_zadania = int(input("Podaj numer zadania: "))
                    if 1 <= numer_zadania <= len(zadania):
                        notatka = input("Podaj treść notatki: ")
                        zadania[numer_zadania - 1]["notatki"].append(notatka)
                        print(f"Notatka została dodana do zadania {zadania[numer_zadania - 1]['opis']}'.")
                    else:
                        print("Nie ma takiego zadania.")
                except ValueError:
                    print("Proszę podać prawidłowy numer")
            else:
                print("Brak zadań do dodania notatki")
        elif wybor == "5":
            print("Wyświetl listę zadań")
            if zadania:
                for idx, zadanie in enumerate(zadania,1):
                    status = "V" if zadanie["wykonane"] else "X"
                    print(f"{idx}. {zadanie['opis']} [{status}]")
            else:
                print("Brak zadań do wyświetlenia.")
        elif wybor == "6":
            if zadania:
                for idx, zadanie in enumerate(zadania, 1):
                    print(f"\n{idx}. {zadanie['opis']}")
                    if zadanie["notatki"]:
                        for notatka in zadanie["notatki"]:
                            print(f"      -  {notatka}")
                    else:
                        print("    Brak notatek.")
            else:
                print("Brak zadań do wyświetlenia notatek.")
        elif wybor == "7":
            print("Dziękujemy za skorzystanie z aplikacji! Do zobaczenia!")
            break  # Kończymy działanie pętli, czyli aplikacji
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")



    
main() 


