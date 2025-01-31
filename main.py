def main_menu():
    load_alarms_from_file()
    while True:
        print("\nHuvudmeny:")
        print("1. Starta övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Radera larm")
        print("5. Starta övervakningsläge")
        print("0. Avsluta")

        choice = input("Välj ett alternativ: ")

        if choice == '1':
            start_monitoring_mode()
        elif choice == '2':
            list_alarms()
        elif choice == '3':
            configure_alarm()
        elif choice == '4':
            delete_alarm()
        elif choice == '5':
            start_monitoring_mode()
        elif choice == '0':
            save_alarms_to_file()
            break
        else:
            print("Ogiltigt val, försök igen.")

# Kör huvudmenyn
if __name__ == "__main__":
    main_menu()