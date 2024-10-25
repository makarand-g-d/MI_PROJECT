import logging
import os
from datetime import datetime

# Generate the log file name with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the directory path for the logs folder
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuring the logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s - %(name)s - %(levelname)s - %(message)s]",
    level=logging.INFO,
)

logging.info("Logging setup complete.")

