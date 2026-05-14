import pandas as pd
import os, time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def total_data():
    total_df = pd.read_csv('Data Science Project.csv')
    print(total_df)
    print('')
    rm = input('Press ENTER to return to menu')
def visualise_data():
    pass

def search_data():
    pass

def mean_data():
    pass

def update_data():
    pass

