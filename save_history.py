import logging
import csv
from datetime import datetime
import os

FILE_NAME = 'historico_preco.csv'

def save_history_csv(name, price):
    arquivo = FILE_NAME

    existe = os.path.exists(arquivo)

    try:
        with open(arquivo, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            if not existe:
                writer.writerow('Data_Hora', 'Produto', 'Preço')

            data_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            writer.writerow([data_atual, name, price])
            logging.info(f"Dados salvos no histórico CSV.")

    except Exception as e:
        import logging
        logging.error(f"Erro as salvar no CSV: {e}")

