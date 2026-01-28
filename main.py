import time
import logging
from monitor import monitoramento_preco
from config_log import initial_config 
from dotenv import load_dotenv
import os

load_dotenv()

URL_PRODUCT = os.getenv("URL_PRODUCT")
PRODUCT_NAME = os.getenv("PRODUCT_NAME")
PRODUCT_PRICE = os.getenv("PRODUCT_PRICE")
DESIRED_PRICE = float(os.getenv("DESIRED_PRICE", 0))

# Entry point oficial do python
if __name__ == "__main__":
    initial_config()

    logging.warning(f"Iniciando monitoramento, Pressione ctrl+C para parar")
    try:
        while True:
            monitoramento_preco(URL_PRODUCT, PRODUCT_NAME, PRODUCT_PRICE, DESIRED_PRICE)
            time.sleep(60)
    except KeyboardInterrupt:
        logging.info("Monitoramento parado pelo usuario")