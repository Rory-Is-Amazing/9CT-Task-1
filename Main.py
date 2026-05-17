import os, time
import matplotlib.pyplot as plt
import pandas as pd

from Data_Module import total_data, clear_screen, visualise_data

def menu():
    while True:
        print('╔══════════════════════════════════╗ \n║           Data Science           ║\n╠══════════════════════════════════╣\n║ 1 > Veiw Data                    ║\n║ 2 > Veiw Visualisation           ║\n║ 3 > Search/Filter Data           ║\n║ 4 > Veiw Mean Data               ║\n║ 5 > Update data                  ║\n║ 6 > Quit                         ║\n╠══════════════════════════════════╣\n║  Enter Option (1-6) to continue  ║\n╚══════════════════════════════════╝')

        option = int(input("Input:"))

        if option == 1:
            total_data()
        elif option == 2:
            visualise_data()
        elif option == 3:
            #search_data()
        elif option == 4:
            #mean_data()
        elif option == 5:
            #compare_data()
        elif option == 6:
            print("Quiting Program...")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")
        clear_screen()

if __name__ == "__main__":
    menu()
