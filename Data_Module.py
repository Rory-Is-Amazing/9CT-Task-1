import pandas as pd # type: ignore
import matplotlib.pyplot as plt
import os, time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def total_data():
    clear_screen()
    print('╔══════════════════════════════════╗\n║         View & Sort Data         ║\n╠══════════════════════════════════╣\n║ 1 > View unsorted data           ║\n║ 2 > View sorted data             ║\n╚══════════════════════════════════╝')
    optiont = input('Input: ')
    if optiont == "1":
        clear_screen()
        total_df = pd.read_csv('Data Science Project.csv')
        print(total_df)
        print('')
        rm = input('Press ENTER to return to menu')
        total_data()
    elif optiont == "2":
        df = pd.read_csv("Data Science Project.csv")
        fields = list(df.columns)
        print("Choose a field to sort by:")
        print("__________________________")
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
    else:
        print("Invalid selection. Please choose a number between 1 and 2.")
        total_data()

def compare_data(csv_file):
    clear_screen()
    df = pd.read_csv(csv_file)
    fields = list(df.columns)
    print("Choose a field to sort by:")
    print("══════════════════════════")
    number = 1
    for field in fields:
        print(str(number) + ". " + field)
        number += 1
    print("")
    choice = input("Enter number: ")
    if not choice.isdigit():
        print("Invalid input. Showing unsorted data.")
        return df
    choice_number = int(choice)
    if choice_number < 1 or choice_number > len(fields):
        print("Number out of range. Showing unsorted data.")
        return df
    selected_field = fields[choice_number - 1]
    df = df.sort_values(selected_field)
    return df


#def compare_data():
    clear_screen()
    print('╔════════════════════════════════════════════╗ \n║               Compare Data                 ║\n╠════════════════════════════════════════════╣\n║ 1 > Extracurricular Hours / School Opinion ║\n║ 2 > Extracurricular Hours / Breaak Opinion ║\n║ 3 > School Opinion / Break Opinion         ║\n║ 5 > Return                                 ║\n╠════════════════════════════════════════════╣\n║  Enter Option (1-5) to continue            ║\n╚════════════════════════════════════════════╝')    
    optionc = int(input('Inupt: '))
    if optionc == 1:
        df = pd.read_csv('Data Science Project.csv')
        dfr = df.drop(columns=["What extracurriculars do you take part in outside of school?", "What is your opinion of school?"])
        print(dfr)
        rm = input('Press ENTER to return to menu')
    #Remove specific collums
    elif optionc == 2:
        pass
    elif optionc == 3:
        pass
    elif optionc == 4:
        pass
    elif optionc == 5:
        pass
    else:
        print("Invalid selection. Please choose a number between 1 and 5.")
        visualise_data()
    # UI that allows for choice of comparions
    # Select prebuilt options for field comparison

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
                x='What is your opinion of breaktime',
                color='green',
                alpha=0.3,
                title='Correlation of extracurricular hours and opinion on school'
                )
        plt.show()
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
    elif optionv == 3:
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