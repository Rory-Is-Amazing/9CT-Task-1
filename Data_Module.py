import pandas as pd
import matplotlib.pyplot as plt
import os, time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def total_data():
    total_df = pd.read_csv('Data Science Project.csv')
    total_df.sort_values('How many hours of extracurricular do you take part in a week?') # BROOOO Not workin
    print(total_df)
    print('')
    rm = input('Press ENTER to return to menu')
def visualise_data():
    total_df = pd.read_csv('Data Science Project.csv')
    total_df.sort_values(by='What is your opinion of school?') # BROOOO Not workin
    total_df.plot(
               kind='bar',
               x='How many hours of extracurricular do you take part in a week?',
               y='What is your opinion of school?',
               color='green',
               alpha=0.3,
               title='Correlation of extracurricular hours and opinion on school'
              )
    plt.show()
    

def search_data():
    pass

def mean_data():
    pass

def update_data():
    pass

