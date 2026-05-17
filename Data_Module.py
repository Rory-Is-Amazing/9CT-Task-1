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
    pass
    # UI that allows for choice of comparions
    # Select prebuilt options for field comparison

def visualise_data():
    print('Close graph to return to menu')
    total_df = pd.read_csv('Data Science Project.csv')
    total_df['How many hours of extracurricular do you take part in a week?'] = \
        pd.to_numeric(total_df['How many hours of extracurricular do you take part in a week?'], errors='coerce')
    total_df_sorted = total_df.sort_values(by='How many hours of extracurricular do you take part in a week?') 
    total_df_sorted = total_df_sorted .reset_index(drop=True) # Fixes graph order
    total_df_sorted.plot(
               kind='barh',
               y='What is your opinion of school?',
               x='How many hours of extracurricular do you take part in a week?',
               color='green',
               alpha=0.3,
               title='Correlation of extracurricular hours and opinion on school'
              )
    plt.show()

def search_data():
    pass
    # Search data for specific values
    # Possibly sort data

def mean_data():
    pass
    # Bring up means for each field