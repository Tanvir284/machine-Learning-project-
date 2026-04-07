import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
LOGS_PATH = os.path.join(BASE_DIR, "logs")
os.makedirs(LOGS_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOGS_PATH, LOG_FILE)
open(LOG_FILE_PATH, "a", encoding="utf-8").close()

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    force=True,
)


