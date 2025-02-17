import sys
import logger

def error_message_detail(error, error_detail:sys):
    # Gives detailed information about the exception
    _, _, exc_tb = error_detail.exc_info()
    # Getting filename
    file_name =  exc_tb.tb_frame.f_code.co_filename

    # Custom error message
    error_message = "An error has occured in python script,  Name: [{0}]  Line number: [{1}]  Error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        # calling super.__init__ inheriting Exception's init
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail= error_detail)

    def __str__(self):
        # returns the error message.
        return self.error_message 

# Test exception.py
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logger.logging.info('dividing by zero') 
        raise CustomException(e, sys)
    
    