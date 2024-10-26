import logging
import os
from datetime import datetime

# Define the log file path and name
log_directory = "logs"
os.makedirs(log_directory, exist_ok=True)
log_file = os.path.join(log_directory, f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,  # You can change this to DEBUG for more detailed logs
    format='[%(asctime)s - %(levelname)s] %(message)s'
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

def log_warning(message):
    logging.warning(message)

def log_debug(message):
    logging.debug(message)
    
from logger import log_info, log_error

# Example of logging in your pipeline
log_info("Starting the data preprocessing step.")
# ... data preprocessing code
log_info("Data preprocessing completed.")

class CustomException(Exception):
    def __init__(self, message, error_details):
        super().__init__(message)
        self.message = message
        self.error_details = error_details

    def __str__(self):
        return f"{self.message} - {self.error_details}"

import logging
import sys

def log_exception(exception):
    logging.error("An error occurred: %s", str(exception))

from exception import CustomException, log_exception

try:
    # Your code that might raise exceptions
    model = load_model()  # Example operation that might fail
except Exception as e:
    custom_exception = CustomException("Failed to load the model", sys.exc_info())
    log_exception(custom_exception)
    raise custom_exception  # Optionally re-raise the exception



