import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def load_cleaned_data():
    data_folder = os.path.join('data')
    file_name = 'drivers_processed_data.csv'
    file_path = os.path.join(data_folder, file_name)
    
    df = pd.read_csv(file_path)
    return df

def perform_eda(df):
    # Estatísticas Descritivas
    print("Estatísticas Descritivas:")
    print(df.describe())
    
    # Visualizações das datas de nascimento
    plt.figure(figsize=(10, 6))
    sns.histplot(df['dob'], bins=20, kde=True)
    plt.title('Distribuição das Datas de Nascimento')
    plt.xlabel('Data de Nascimento')
    plt.ylabel('Frequência')
    plt.show()


    # Visualização da nacionalidade
    plt.figure(figsize=(12, 6))
    sns.countplot(y='nationality', data=df, order=df['nationality'].value_counts().index)
    plt.title('Contagem de Nacionalidades')
    plt.xlabel('Contagem')
    plt.ylabel('Nacionalidade')
    plt.show()

if __name__ == "__main__":
    df = load_cleaned_data()
    perform_eda(df)
