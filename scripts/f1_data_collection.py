import pandas as pd
import glob
import os

#Função que carrega os dados brutos

def load_data():

  #Listar todos os arquivos csv em um diretorio
    csv_files = glob.glob('data/*.csv')

  #Criar um novo dataframe para armazenar os dados de todos os arquivos
    combined_df = pd.DataFrame()

  
  #Loop por cada arquivo CSV e anexe seu conteúdo ao dataframe combinado
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        combined_df = pd.concat([combined_df, df])

    print(combined_df)

if __name__ == "__main__":
    load_data()