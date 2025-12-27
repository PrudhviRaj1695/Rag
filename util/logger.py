import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Create logger
logger = logging.getLogger("rag_app")
logger.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

# File handler (rotates at 5MB)
file_handler = RotatingFileHandler(
    LOG_FILE, maxBytes=5_000_000, backupCount=3
)
file_handler.setFormatter(formatter)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Avoid duplicate logs
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
