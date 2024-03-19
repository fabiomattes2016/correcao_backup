import os
from datetime import datetime

# Diretório de downloads
diretorio_downloads = './downloads'

# Inicio arquivo
prefixo = 'envelope_backup_'
extensao = '.zip'

# Obtendo a data atual
data_atual_underscore = datetime.now().strftime("%m_%d_%Y").lstrip('0').replace('_0', '_')
data_atual_ponto = datetime.now().strftime("%d.%m.%Y")

# Lista dos arquivos no diretório de downloads
arquivos = os.listdir(diretorio_downloads)

# Procurando o arquivo com a data atual no nome
arquivo_atual = None

for arquivo in arquivos:
    # Verificando se o arquivo termina com o padrão e a data atual
    if arquivo.endswith(data_atual_underscore + extensao):
        # Pegando o nome do arquivo atual
        arquivo_atual = prefixo + data_atual_underscore + extensao
    elif arquivo.endswith(data_atual_ponto + extensao):
        arquivo_atual = prefixo + data_atual_ponto + extensao

# Verificando se o arquivo foi encontrado
if arquivo_atual:
    print(f"O arquivo atual é: {arquivo_atual}")
else:
    print("Nenhum arquivo com a data atual foi encontrado.")



