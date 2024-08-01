import pandas as pd
import os

#Função que carrega os dados brutos

def load_data():
    data_folder = os.path.join('data')
    file_name = 'drivers.csv'
    file_path = os.path.join(data_folder, file_name)
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())