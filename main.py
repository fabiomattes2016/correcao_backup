import os
import logging
from datetime import datetime


logger = logging.getLogger(datetime.now().strftime("%H:%M:%S"))
logging.basicConfig(
    filename=f"{datetime.now().strftime("%d%m%Y")}.log", 
    encoding='utf-8',
    datefmt='%d/%m/%Y %H:%M:%S',
    level=logging.INFO, 
    force=True
)

# Diretório de downloads
logger.info('Selecionando diretório de downloads')
diretorio_downloads: str = './downloads'

# Inicio arquivo
prefixo: str = 'envelope_backup_'
extensao: str = '.zip'

# Obtendo a data atual e gerando padrões
logger.info('Gerando padrões de arquivo')
data_atual_underscore: str = datetime.now().strftime("%m_%d_%Y").lstrip('0').replace('_0', '_') # <- Remove o 0 do dia
data_atual_ponto: str = datetime.now().strftime("%d.%m.%Y")

# Lista dos arquivos no diretório de downloads
logger.info('Buscando arquivos do diretório de downloads')
arquivos: list[str] = os.listdir(diretorio_downloads)

# Procurando o arquivo com a data atual no nome
arquivo_atual = None

try:
    for arquivo in arquivos:
        # Verificando se o arquivo termina com o padrão e a data atual
        if arquivo.endswith(data_atual_underscore + extensao):
            # Pegando o nome do arquivo atual
            arquivo_atual = prefixo + data_atual_underscore + extensao
            logger.info(f"Arquivo encontrado: {arquivo}")
        elif arquivo.endswith(data_atual_ponto + extensao):
            arquivo_atual = prefixo + data_atual_ponto + extensao
            logger.info(f"Arquivo encontrado: {arquivo}")
except:
    logger.error('Ocorreu um erro ao buscar arquivos')

# Verificando se o arquivo foi encontrado
if arquivo_atual:
    print(f"O arquivo atual é: {arquivo_atual}")
else:
    print("Nenhum arquivo com a data atual foi encontrado.")
