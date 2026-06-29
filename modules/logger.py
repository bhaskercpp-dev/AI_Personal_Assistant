import logging
import os

# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/assistant.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

def log_warning(message):
    logging.warning(message)