import sys
from src.logger import logger

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()                        #_,_ used to ignore the first two items returned by exc_info() and exc_tb assgined to third item which is trackback object
    file_name = exc_tb.tb_frame.f_code.co_filename              #This line extracts the name of the file that raised the exception from the traceback object using the tb_frame.f_code.co_filename attribute.
    error_message  = "Error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message


