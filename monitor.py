import requests
from bs4 import BeautifulSoup
import send_email
from save_history import save_history_csv
import logging

# User-Agent serve para o site nao achar que vc é um robô malicioso
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def monitoramento_preco(url_product, product_name, product_price, derired_price):

    try:
        # pegar conteúdo da pagina
        page = requests.get(url_product, headers=HEADERS)
        soup = BeautifulSoup(page.content, 'html.parser')

        if product_name and product_price:
            # localizando o titulo e o preço
            title = soup.find(class_= product_name).get_text().strip()
            price_text = soup.find(class_=product_price).get_text().strip()

            # converde o preco para numero
            clean_price = price_text.replace("R$", "").replace(".", "").replace(",", ".").strip()
            final_price = float(clean_price)

            logging.info(f"produto: {title[:20]} | Preço: R$ {final_price:.2f}")

            # logica de alerta
            if final_price < derired_price:
                logging.warning(f"META ATIGIDA: R$ {final_price:.2f}")
                 
                save_history_csv(title, final_price)
                send_email(title, final_price)
            else:
                logging.info("ainda está caro para dedel...")

    except Exception as e:
        logging.error(f"Ocorreu um erro: {e}")