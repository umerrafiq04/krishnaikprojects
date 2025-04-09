import sys 
import logging
# from logger import logging
from src.logger import logging

'''The sys library in Python provides functions and variables to interact with the Python interpreter. 
It allows you to access command-line arguments, manipulate the Python runtime environment, 
and manage input/output streams.'''

# whenever erros comes display this custom msg
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()  #exc_t:file,line no etc where eror occured
    file_name=exc_tb.tb_frame.f_code.co_filename

    error_message="Error occured in python script name [{0}] line no [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message


if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("divided by zero error") # it will not get logged?why?
        raise CustomException(e,sys)