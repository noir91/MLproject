import logging
import os
from datetime import datetime

# log file name will be the current time of the log.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Path of log file
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE) # join(os.getcwd(), naming convention 1st logs, 2nd LOG_FILE(current_datetime))
os.makedirs(logs_path, exist_ok= True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE,
    level = logging.INFO,
    format = '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    
)

# Test logger.py
if __name__ == "__main__":
    logging.info('Logging has started')