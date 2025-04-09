import logging
import os
from datetime import datetime
'''
The logging module in Python is used to record messages for debugging 
and tracking events in an application. It helps in logging errors, warnings,
 and other information instead of using print().

Example:
import logging
logging.warning("This is a warning message!")
'''

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("This is an info message!") 