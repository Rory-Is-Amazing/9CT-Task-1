import pandas as pd # type: ignore
import matplotlib.pyplot as plt
import os, time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def total_data():
    
    # Ask if they would prefere data sorted or unsorted
    total_df = pd.read_csv('Data Science Project.csv')
    total_df['How many hours of extracurricular do you take part in a week?'] = \
        pd.to_numeric(total_df['How many hours of extracurricular do you take part in a week?'], errors='coerce')
    total_df.sort_values('How many hours of extracurricular do you take part in a week?', inplace=True) # BROOOO Not workin
    print(total_df)
    print('')
    rm = input('Press ENTER to return to menu')


def compare_data():
    clear_screen()
    print('╔════════════════════════════════════════════╗ \n║              Visualise Data                ║\n╠════════════════════════════════════════════╣\n║ 1 > Extracurricular Hours / School Opinion ║\n║ 2 > Extracurricular Hours / Breaak Opinion ║\n║ 3 > School Opinion / Break Opinion         ║\n║ 5 > Return                                 ║\n╠════════════════════════════════════════════╣\n║  Enter Option (1-5) to continue            ║\n╚════════════════════════════════════════════╝')    
    optionc = int(input('Inupt: '))
    if optionc == 1:
        pass
    elif optionc == 2:
        pass
    elif optionc == 3:
        pass
    elif optionc == 4:
        pass
    elif optionc == 5:
        pass
    # UI that allows for choice of comparions
    # Select prebuilt options for field comparison

def visualise_data():
    clear_screen()
    print('╔════════════════════════════════════════════╗ \n║              Visualise Data                ║\n╠════════════════════════════════════════════╣\n║ 1 > Extracurricular Hours / School Opinion ║\n║ 2 > Extracurricular Hours / Breaak Opinion ║\n║ 3 > School Opinion / Break Opinion         ║\n║ 5 > Return                                 ║\n╠════════════════════════════════════════════╣\n║  Enter Option (1-5) to continue            ║\n╚════════════════════════════════════════════╝')    
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
    elif optionv == 2:
        print('Close graph to continue')
    elif optionv == 3:
        print('Close graph to continue')
    elif optionv == 4:
        print('Close graph to continue')
    elif optionv == 5:
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