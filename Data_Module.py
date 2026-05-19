import pandas as pd # type: ignore
import matplotlib.pyplot as plt
import os, time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def total_data():
    clear_screen()
    print('╔══════════════════════════════════╗\n║         View & Sort Data         ║\n╠══════════════════════════════════╣\n║ 1 > View unsorted data           ║\n║ 2 > View sorted data             ║\n║ 3 > Return                       ║\n╚══════════════════════════════════╝')
    optiont = input('Input: ')
    if optiont == "1":
        clear_screen()
        total_df = pd.read_csv('Data Science Project.csv')
        print(total_df)
        print('')
        rm = input('Press ENTER to return to menu')
        total_data()
    elif optiont == "2":
        clear_screen()
        df = pd.read_csv("Data Science Project.csv")
        fields = list(df.columns)
        print("Choose a field to sort by:")
        print("══════════════════════════")
        number = 1
        for field in fields:
            print(str(number) + ". " + field)
            number += 1
        choice = input("\nEnter number: ")
        if not choice.isdigit():
            print("Not a number. Showing unsorted data.")
            print(df)
            rm = input("Press ENTER to return to menu")
            total_data()
        choice_number = int(choice)
        selected_field = fields[choice_number - 1]
        df = df.sort_values(selected_field)
        print(df)
        rm = input("Press ENTER to return to menu")
        total_data()
    elif optiont == "3":
        pass
    else:
        print("Invalid selection. Please choose a number between 1 and 2.")
        total_data()

def compare_data(csv_file):
    clear_screen()
    df = pd.read_csv(csv_file)
    fields = list(df.columns)
    print("Choose which fields to view (e.g. 1,3,4):")
    print("═════════════════════════════════════════")
    for i,f in enumerate(fields,1):
        print(str(i)+"."+f)
    choice=input('\nEnter number(s):\n')
    parts=[p.strip() for p in choice.split(",")]  # Removes comma and space to allow later lines to understand users input
    if not all(p.isdigit() for p in parts):       # Used to check for formats including (1), (1,2), etc
        print("Invalid input. Showing all data.")
        print(df)
        input("\nPress ENTER to return to menu")
        return
    nums=[int(p) for p in parts]
    if any(n<1 or n>len(fields) for n in nums):
        print("Number out of range. Showing all data.")
        time.sleep(3)
        print(df)
        input("\nPress ENTER to return to menu")
        return





def visualise_data():
    clear_screen()
    print('╔════════════════════════════════════════════╗ \n║              Visualise Data                ║\n╠════════════════════════════════════════════╣\n║ 1 > Extracurricular Hours / School Opinion ║\n║ 2 > Extracurricular Hours / Breaak Opinion ║\n║ 3 > School Opinion / Break Opinion         ║\n║ 4 > Return                                 ║\n╠════════════════════════════════════════════╣\n║  Enter Option (1-4) to continue            ║\n╚════════════════════════════════════════════╝')    
    optionv = int(input('Inupt: '))
    if optionv == 1:
        print('Close graph to continue')
        total_df = pd.read_csv('Data Science Project.csv')
        total_df['How many hours of extracurricular do you take part in a week?'] = \
            pd.to_numeric(total_df['How many hours of extracurricular do you take part in a week?'], errors='coerce')
        total_df_sorted = total_df.sort_values(by='How many hours of extracurricular do you take part in a week?') 
        total_df_sorted = total_df_sorted .reset_index(drop=True) # Fixes graph order
        total_df_sorted.plot(
                kind='bar',
                y='What is your opinion of school?',
                x='How many hours of extracurricular do you take part in a week?',
                color='green',
                alpha=0.3,
                title='Correlation of extracurricular hours and opinion on school'
                )
        plt.show()
        visualise_data()
    elif optionv == 2:
        print('Close graph to continue')
        total_df = pd.read_csv('Data Science Project.csv')
        total_df['How many hours of extracurricular do you take part in a week?'] = \
            pd.to_numeric(total_df['How many hours of extracurricular do you take part in a week?'], errors='coerce')
        total_df_sorted = total_df.sort_values(by='How many hours of extracurricular do you take part in a week?') 
        total_df_sorted = total_df_sorted .reset_index(drop=True) # Fixes graph order
        total_df_sorted.plot(
                kind='bar',
                y='What is your opinion of breaktime?',
                x='How many hours of extracurricular do you take part in a week?',
                color='green',
                alpha=0.3,
                title='Correlation of extracurricular hours and opinion on school'
                )
        plt.show()
        visualise_data()
    elif optionv == 3:
        print('Close graph to continue')
        total_df = pd.read_csv('Data Science Project.csv')
        total_df['What is your opinion of breaktime?'] = \
            pd.to_numeric(total_df['What is your opinion of breaktime?'], errors='coerce')
        total_df_sorted = total_df.sort_values(by='What is your opinion of breaktime?') 
        total_df_sorted = total_df_sorted .reset_index(drop=True) # Fixes graph order
        total_df_sorted.plot(
                kind='bar',
                y='What is your opinion of school?',
                x='What is your opinion of breaktime?',
                color='green',
                alpha=0.3,
                title='Correlation of extracurricular hours and opinion on school'
                )
        plt.show()
        visualise_data()
    elif optionv == 4:
        pass
    else:
        print("Invalid selection. Please choose a number between 1 and 5.")
        visualise_data()

def search_data():
    pass
    # Search data for specific values
    # Possibly sort data

def mean_data():
    pass
    # Bring up means for each field