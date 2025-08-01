import sys
import logger

def error_message_details(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
        filename, line_number, str(error)
    )                                                            
    
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)

    def __str__(self):
        return self.error_message
    

# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logger.logging.error("An error occurred: %s", e)
#         raise CustomException(e, sys) from e