import pandas as pd
import os 

#Função que limpa os dados
def clean_data(df):

# Remoção de valores ausentes nas colunas 'forename' e 'surname'
    df.dropna(subset=['forename', 'surname'], inplace=True)

    # Converção da coluna 'dob' (data de nascimento/date of birth)
    
    df['dob'] = pd.to_datetime(df['dob'])

    return df


if __name__ == "__main__":
    data_folder = os.path.join('data')
    file_name = 'drivers.csv'
    file_path = os.path.join(data_folder, file_name)

    df = pd.read_csv(file_path)
    df = clean_data(df)

    processed_folder = os.path.join('data')
    processed_file_path = os.path.join(processed_folder, 'drivers_processed_data.csv')

    df.to_csv(processed_file_path, index=False)
