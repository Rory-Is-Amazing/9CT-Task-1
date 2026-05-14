import os, time

import pandas as pd

from Data_Module import total_data, clear_screen

def menu():
    while True:
        print('╔══════════════════════════════════╗ \n║           Data Science           ║\n╠══════════════════════════════════╣\n║ 1 > Veiw Data                    ║\n║ 2 > Veiw Visualisation           ║\n║ 3 > Search/Filter Data           ║\n║ 4 > Veiw Mean Data               ║\n║ 5 > Update data                  ║\n║ 6 > Quit                         ║\n╠══════════════════════════════════╣\n║  Enter Option (1-6) to continue  ║\n╚══════════════════════════════════╝')

        option = int(input("Input:"))

        if option == 1:
            total_data()
        elif option == 2:
            #visualise_data()
            pass
        elif option == 3:
            #search_data()
            pass
        elif option == 4:
            #mean_data()
            pass
        elif option == 5:
            #update_data()
            pass
        elif option == 6:
            #save_changes()
            print("Quiting Program...")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")
        clear_screen()

if __name__ == "__main__":
    menu()