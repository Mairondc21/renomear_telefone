import os
import pandas as pd

def renomear_arquivos(diretorio_arquivos, arquivo_csv):
    df = pd.read_csv(arquivo_csv,delimiter=';')
    
    # Verifica se as colunas TEL_FEITO e codigos estão presentes
    if 'TEL_FEITO' not in df.columns or 'CODIGO' not in df.columns:
        raise ValueError("As colunas 'TEL_FEITO' e 'codigos' devem estar presentes no arquivo CSV.")
    
   
    for nome_arquivo in os.listdir(diretorio_arquivos):
        numero_arquivo = nome_arquivo[9:20]
        numero_arquivo = ''.join(filter(str.isdigit, numero_arquivo))
        
        
        if numero_arquivo in df['TEL_FEITO'].astype(str).values:
            
            codigo_novo = df.loc[df['TEL_FEITO'].astype(str) == numero_arquivo, 'CODIGO'].values[0]
            
            
            novo_nome = f"{codigo_novo}{os.path.splitext(nome_arquivo)[1]}"
            
            
            caminho_antigo = os.path.join(diretorio_arquivos, nome_arquivo)
            caminho_novo = os.path.join(diretorio_arquivos, novo_nome)
            
            # Renomeia o arquivo
            os.rename(caminho_antigo, caminho_novo)
            print(f"Arquivo {nome_arquivo} renomeado para {novo_nome}")


caminho_pasta = r'C:\Users\mairon.costa\OneDrive - Expertise Inteligência e Pesquisa de Mercado\expertise_mairon\2024\Audio_Cielo_Mensal\audio\IN'
arquivo = './dados/tel_e_codigos.csv'

renomear_arquivos(caminho_pasta, arquivo)