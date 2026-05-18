import os, time
import pandas as pd
import matplotlib.pyplot as plt
from Data_Module import clear_screen, total_data, view_selected_fields, visualise_data, search_data, mean_data

def menu():
    while True:
        print('╔══════════════════════════════════╗ \n║           Data Science           ║\n╠══════════════════════════════════╣\n║ 1 > Veiw Data                    ║\n║ 2 > Compare Fields               ║\n║ 3 > Visualise Data               ║\n║ 4 > Search/Filter Data           ║\n║ 5 > Veiw Mean Data               ║\n║ 6 > Quit                         ║\n╠══════════════════════════════════╣\n║  Enter Option (1-6) to continue  ║\n╚══════════════════════════════════╝')

        option = input("Input:")

        if option == "1":
            total_data()
        elif option == "2":
            view_selected_fields("Data Science Project.csv")
            rm = input('\nPress ENTER to return to menu')
        elif option == "3":
            visualise_data()
        elif option == "4":
            search_data()
        elif option == "5":
            mean_data()
        elif option == "6":
            print("Quiting Program...")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")
        clear_screen()

if __name__ == "__main__":
    menu()