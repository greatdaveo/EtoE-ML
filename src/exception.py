import sys
import logging


def error_message_detail(error: Exception) -> str:
    _, _, exc_tb = sys.exc_info()
    if exc_tb is None:
        return str(error)
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{exc_tb.tb_lineno}] "
        f"error message [{error}]"
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error: Exception):
        super().__init__(str(error))
        self.error_message = error_message_detail(error)

    def __str__(self):
        return self.error_message


# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e)
