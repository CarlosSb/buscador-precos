import logging

def initial_config():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("monitor.log"),
            logging.StreamHandler()
        ]
    )
    logging.info("Sistem de logging configurado com sucesso.")