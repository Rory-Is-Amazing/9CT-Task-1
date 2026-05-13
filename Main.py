

def menu():
    while True:
        print('╔══════════════════════════════════╗ \n║           Data Science           ║\n╠══════════════════════════════════╣\n║ 1 > Veiw Visualisation           ║\n║ 2 > Search/Filter Data           ║\n║ 3 > Veiw Mean Data               ║\n║ 4 > Update data                  ║\n║ 5 > Quit                         ║\n╠══════════════════════════════════╣\n║  Enter Option (1-5) to continue  ║\n╚══════════════════════════════════╝')

        option = input()

        if option == '1':
            #visualise_data()
            pass
        elif option == '2':
            #search_data()
            pass
        elif option == '3':
            #mean_data()
            pass
        elif option == '4':
            #update_data()
            pass
        elif option == '5':
            #save_changes()
            print("Quiting Program...")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    menu()