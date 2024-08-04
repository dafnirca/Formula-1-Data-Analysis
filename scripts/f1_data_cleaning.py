import pandas as pd
import glob

def load_and_clean_data():
    # Listar todos os arquivos CSV no diretório 'data'
    csv_files = glob.glob('data/*.csv')

    # Criar um DataFrame vazio para armazenar os dados combinados
    combined_df = pd.DataFrame()

    # Loop por cada arquivo CSV e anexar seu conteúdo ao DataFrame combinado
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    # Remover duplicatas
    combined_df.drop_duplicates(inplace=True)

    # Preencher valores nulos (ajustar conforme necessário)
    combined_df.fillna(method='ffill', inplace=True)

    # Converter colunas para os tipos apropriados (ajustar conforme necessário)
    if 'data' in combined_df.columns:
        combined_df['data'] = pd.to_datetime(combined_df['data'])

    return combined_df

if __name__ == "__main__":
    data = load_and_clean_data()
    print(data.head())
    data.to_csv('cleaned_data.csv', index=False)
