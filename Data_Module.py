import pandas as pd # type: ignore
import matplotlib.pyplot as plt
import os, time


def clear_screen(): # Easy function to clear the screen, for visual improvment
    os.system('cls' if os.name == 'nt' else 'clear')


def total_data():
    clear_screen()

    print('╔══════════════════════════════════╗\n║         View & Sort Data         ║\n╠══════════════════════════════════╣\n║ 1 > View unsorted data           ║\n║ 2 > View sorted data             ║\n║ 3 > Return                       ║\n╚══════════════════════════════════╝')
    optiont = input('Input: ')

    if optiont == "1":
        clear_screen()
        total_df = pd.read_csv('Data Science Project.csv') # Reads the .csv file in
        print(total_df) # Displays .csv file
        print('')
        rm = input('Press ENTER to return to menu') # Works as a break 
        total_data()

    elif optiont == "2":
        clear_screen()
        df = pd.read_csv("Data Science Project.csv")
        fields = list(df.columns)

        print("Choose a field to sort by:")
        print("══════════════════════════")

        number = 1
        for field in fields: # Displays the fields with a number next to
            print(str(number) + ". " + field)
            number += 1

        choice = input("\nEnter number: ") #\n works as an extra line beforehand

        if not choice.isdigit(): # Checks if the input is a number
            print("Not a number. Showing unsorted data.")
            print(df)
            rm = input("Press ENTER to return to menu")
            total_data()

        choice_number = int(choice)
        selected_field = fields[choice_number - 1]

        df = df.sort_values(selected_field) # Sorts polished data
        print(df)

        rm = input("Press ENTER to return to menu")
        total_data()

    elif optiont == "3":
        pass # Skips to main menu

    else:
        print("Invalid selection. Please choose a number between 1 and 2.") # Error output
        total_data()

def compare_data(csv_file): #csv_file is used to allow for the function to be used elsewhere
    clear_screen()

    df = pd.read_csv(csv_file)
    fields = list(df.columns)

    print("Choose which fields to view (e.g. 1,3,4):")
    print("═════════════════════════════════════════")

    for i,f in enumerate(fields,1): #enumerate is a new function to me, allowing for the number to be added to the start of the field
        print(str(i)+"."+f)
    choice=input('\nEnter number(s):\n')
    parts=[p.strip() for p in choice.split(",")]

    if not all(p.isdigit() for p in parts):
        print("Invalid input. Showing all data.")
        print(df)
        input("\nPress ENTER to return to menu")
        return
    nums=[int(p) for p in parts]

    if any(n<1 or n>len(fields) for n in nums): #n<1 or n>len(fields) checks if the number is out of range
        print("Number out of range. Showing all data.")
        print(df)
        input("\nPress ENTER to return to menu")
        return # returns straight to menu
    
    selected=[fields[n-1] for n in nums]
    df=df[selected]
    print(df)
    input("\nPress ENTER to return to menu")




def visualise_data():
    clear_screen()

    print('╔════════════════════════════════════════════╗ \n║              Visualise Data                ║\n╠════════════════════════════════════════════╣\n║ 1 > Extracurricular Hours / School Opinion ║\n║ 2 > Extracurricular Hours / Breaak Opinion ║\n║ 3 > School Opinion / Break Opinion         ║\n║ 4 > Return                                 ║\n╠════════════════════════════════════════════╣\n║  Enter Option (1-4) to continue            ║\n╚════════════════════════════════════════════╝')    
    optionv = input('Inupt: ')

    if optionv == '1': # Specifc graphs for each data combination, due to the limited total
        print('Close graph to continue')
        total_df = pd.read_csv('Data Science Project.csv')
        total_df['How many hours of extracurricular do you take part in a week?'] = \
            pd.to_numeric(total_df['How many hours of extracurricular do you take part in a week?'], errors='coerce') #converts non numbers to NaN allowing for the graph to be plotted without error, errors = 'coerce' being a new function
        total_df_sorted = total_df.sort_values(by='How many hours of extracurricular do you take part in a week?') 
        total_df_sorted = total_df_sorted .reset_index(drop=True)
       
        total_df_sorted.plot( # Creates graphy through matplotlib allowing for easy visualisation of data
                kind='bar', # Best, although not perfect graph to reperesnt data
                y='What is your opinion of school?',
                x='How many hours of extracurricular do you take part in a week?',
                color='green',
                alpha=0.3,
                title='Correlation of extracurricular hours and opinion on school'
                )
        
        plt.show()
        visualise_data() # Returns to visualise menu

    elif optionv == '2':
        print('Close graph to continue')
        total_df = pd.read_csv('Data Science Project.csv')
        total_df['How many hours of extracurricular do you take part in a week?'] = \
            pd.to_numeric(total_df['How many hours of extracurricular do you take part in a week?'], errors='coerce')
        total_df_sorted = total_df.sort_values(by='How many hours of extracurricular do you take part in a week?') 
        total_df_sorted = total_df_sorted .reset_index(drop=True)
        
        total_df_sorted.plot(
                kind='bar',
                y='What is your opinion of breaktime?',
                x='How many hours of extracurricular do you take part in a week?',
                color='blue',
                alpha=0.3,
                title='Correlation of extracurricular hours and opinion on breaktime'
                )
        
        plt.show()
        visualise_data()

    elif optionv == '3':
        print('Close graph to continue')
        total_df = pd.read_csv('Data Science Project.csv')
        total_df['What is your opinion of breaktime?'] = \
            pd.to_numeric(total_df['What is your opinion of breaktime?'], errors='coerce')
        total_df_sorted = total_df.sort_values(by='What is your opinion of breaktime?') 
        total_df_sorted = total_df_sorted .reset_index(drop=True)
        
        total_df_sorted.plot(
                kind='bar',
                y='What is your opinion of school?',
                x='What is your opinion of breaktime?',
                color='red',
                alpha=0.3,
                title='Correlation of opinion on school and opinion on breaktime'
                )
        
        plt.show()
        visualise_data()

    elif optionv == '4':
        pass

    else:
        print("Invalid selection. Please choose a number between 1 and 5.")
        visualise_data()

def search_data():
    clear_screen()
    sdf = pd.read_csv('Data Science Project.csv')
    
    print('╔════════════════════════════════════════════╗ \n║                Search Data                 ║\n╠════════════════════════════════════════════╣\n║ 1 > Extra Curricualar Hours / Week?        ║\n║ 2 > What is your opinion of school?        ║\n║ 3 > What is your opinion of breatime?      ║\n║ 4 > Return                                 ║\n╠════════════════════════════════════════════╣\n║  Enter Option (1-4) to continue            ║\n╚════════════════════════════════════════════╝')    
    column_selected = input('Inupt: ') # Selects what field to search in
    
    if column_selected != '4': # All options except return

        search = input("Enter the string/value to search for: ") # tells system what to search for
        clear_screen()

        if column_selected == '1': # Converts input to existing fields
            column_selected = 'How many hours of extracurricular do you take part in a week?'
        elif column_selected == '2':
            column_selected = 'What is your opinion of school?'
        elif column_selected == '3':
            column_selected = 'What is your opinion of breaktime?'
        else:
            print("Invalid selection. Please choose a number between 1 and 4.")
            search_data()
        
        sdf = sdf[sdf[column_selected].astype(str) == search] #.astype(str) is used to allow for 12 to equal '12', as shown in my .csv
        print(sdf)

        input("\nPress ENTER to return to menu")
        search_data()  
    
    elif column_selected == '4':
        pass
    else:
        print("Invalid selection. Please choose a number between 1 and 4.")
        search_data()


def mean_data():
    clear_screen()

    print('╔════════════════════════════════════════════╗ \n║              Fields to Analyse             ║\n╠════════════════════════════════════════════╣\n║ 1 > Extra Curricualar Hours / Week?        ║\n║ 2 > What is your opinion of school?        ║\n║ 3 > What is your opinion of breatime?      ║\n║ Return → Next Section                      ║\n╠════════════════════════════════════════════╣\n║  Enter Option (1-3) to continue            ║\n╚════════════════════════════════════════════╝')    
    data_t = input('Inupt: ')

    clear_screen()

    print('╔════════════════════════════════════════════╗ \n║           Descriptive Statistics           ║\n╠════════════════════════════════════════════╣\n║ 1 > Mean                                   ║\n║ 2 > Mode                                   ║\n║ 3 > Max                                    ║\n║ 4 > Min                                    ║\n║ 5 > Range                                  ║\n║ 6 > Return                                 ║\n╠════════════════════════════════════════════╣\n║  Enter Option (1-6) to continue            ║\n╚════════════════════════════════════════════╝')    
    optionm = input('Inupt: ')
    
    clear_screen()

    # Compacting this function by having one set of if statments through use of a variable, would be much more efficient and space effective, but I have left it in this format to make it more readable and easier to understand. (No time...)
    # This is super iniefficient
    if optionm == '1': # Finds median, which is the average value
        if data_t == '1': # What field to calculate statistics on
            total_df = pd.read_csv('Data Science Project.csv')
            mean_value = total_df['How many hours of extracurricular do you take part in a week?'].mean()
            print(f'Mean: {mean_value}') # Prints Mean: next to calculated mean value
            input('Press ENTER to return to menu')
            mean_data()
        elif data_t == '2':
            total_df = pd.read_csv('Data Science Project.csv')
            mean_value = total_df['What is your opinion of school?'].mean()
            print(f'Mean: {mean_value}')
            input('Press ENTER to return to menu')
            mean_data()
        elif data_t == '3':
            total_df = pd.read_csv('Data Science Project.csv')
            mean_value = total_df['What is your opinion of breaktime?'].mean()
            print(f'Mean: {mean_value}')
            input('Press ENTER to return to menu')
            mean_data()
        else:
            print("Invalid selection. Please choose a number between 1 and 4.")
            mean_data()

    elif optionm == '2': # Finds mode, which is the most common value
        if data_t == '1':
            total_df = pd.read_csv('Data Science Project.csv')
            mode_value = total_df['How many hours of extracurricular do you take part in a week?'].mode()[0]
            print(f'Mode: {mode_value}')
            input('Press ENTER to return to menu')
            mean_data()
        elif data_t == '2':
            total_df = pd.read_csv('Data Science Project.csv')
            mode_value = total_df['What is your opinion of school?'].mode()[0]
            print(f'Mode: {mode_value}')
            input('Press ENTER to return to menu')
            mean_data()
        elif data_t == '3':
            total_df = pd.read_csv('Data Science Project.csv')
            mode_value = total_df['What is your opinion of breaktime?'].mode()[0]
            print(f'Mode: {mode_value}')
            input('Press ENTER to return to menu')
            mean_data()
        else:
            print("Invalid selection. Please choose a number between 1 and 4.")
            mean_data()

    elif optionm == '3': # Finds max, which is the highest value
        if data_t == '1':
            total_df = pd.read_csv('Data Science Project.csv')
            max_value = total_df['How many hours of extracurricular do you take part in a week?'].max()
            print(f'Max: {max_value}')
            input('Press ENTER to return to menu')
            mean_data()
        elif data_t == '2':
            total_df = pd.read_csv('Data Science Project.csv')
            max_value = total_df['What is your opinion of school?'].max()
            print(f'Max: {max_value}')
            input('Press ENTER to return to menu')
            mean_data()
        elif data_t == '3':
            total_df = pd.read_csv('Data Science Project.csv')
            max_value = total_df['What is your opinion of breaktime?'].max()
            print(f'Max: {max_value}')
            input('Press ENTER to return to menu')
            mean_data()
        else:
            print("Invalid selection. Please choose a number between 1 and 4.")
            mean_data()

    elif optionm == '4': # Finds min, which is the lowest value
        if data_t == '1':
            total_df = pd.read_csv('Data Science Project.csv')
            min_value = total_df['How many hours of extracurricular do you take part in a week?'].min()
            print(f'Min: {min_value}')
            input('Press ENTER to return to menu')
            mean_data()
        elif data_t == '2':
            total_df = pd.read_csv('Data Science Project.csv')
            min_value = total_df['What is your opinion of school?'].min()
            print(f'Min: {min_value}')
            input('Press ENTER to return to menu')
            mean_data()
        elif data_t == '3':
            total_df = pd.read_csv('Data Science Project.csv')
            min_value = total_df['What is your opinion of breaktime?'].min()
            print(f'Min: {min_value}')
            input('Press ENTER to return to menu')
            mean_data()
        else:
            print("Invalid selection. Please choose a number between 1 and 4.")
            mean_data()

    elif optionm == '5': # Finds range, which is the difference between the max and min values
        if data_t == '1':
            total_df = pd.read_csv('Data Science Project.csv')
            range_value = total_df['How many hours of extracurricular do you take part in a week?'].max() - total_df['How many hours of extracurricular do you take part in a week?'].min()
            print(f'Range: {range_value}')
            input('Press ENTER to return to menu')
            mean_data()
        elif data_t == '2':
            total_df = pd.read_csv('Data Science Project.csv')
            range_value = total_df['What is your opinion of school?'].max() - total_df['What is your opinion of school?'].min()
            print(f'Range: {range_value}')
            input('Press ENTER to return to menu')
            mean_data()
        elif data_t == '3':
            total_df = pd.read_csv('Data Science Project.csv')
            range_value = total_df['What is your opinion of breaktime?'].max() - total_df['What is your opinion of breaktime?'].min()
            print(f'Range: {range_value}')
            input('Press ENTER to return to menu')
            mean_data()
        else:
            print("Invalid selection. Please choose a number between 1 and 4.")
            mean_data()

    elif optionm == '6': # Return to menu
        pass

    else:
        print("Invalid selection. Please choose a number between 1 and 6.")
        mean_data()