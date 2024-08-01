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

def create_visualizations(df):
    # Visualização 1: Distribuição da Data de Nascimento
    plt.figure(figsize=(10, 6))
    sns.histplot(df['dob'], bins=20, kde=True)
    plt.title('Distribuição das Datas de Nascimento')
    plt.xlabel('Data de Nascimento')
    plt.ylabel('Frequência')
    plt.xticks(rotation=45)
    plt.show()

    # Visualização 2: Contagem de Nacionalidades
    plt.figure(figsize=(12, 8))
    sns.countplot(y='nationality', data=df, order=df['nationality'].value_counts().index)
    plt.title('Contagem de Nacionalidades')
    plt.xlabel('Contagem')
    plt.ylabel('Nacionalidade')
    plt.show()

    # Visualização 3: Gráfico de Barras de Sobrenomes
    plt.figure(figsize=(12, 8))
    top_surnames = df['surname'].value_counts().nlargest(20).index
    sns.countplot(y='surname', data=df[df['surname'].isin(top_surnames)], order=top_surnames)
    plt.title('Top 20 Sobrenomes dos Motoristas')
    plt.xlabel('Contagem')
    plt.ylabel('Sobrenome')
    plt.show()

if __name__ == "__main__":
    df = load_cleaned_data()
    create_visualizations(df)