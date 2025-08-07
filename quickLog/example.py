import logging
import inspect
import os
from scripts.logUtility import logMaker, log_decoexampl

@log_deco
def printLogLocation(parent_directory):
    logger = logging.getLogger(__name__)
    funcName = inspect.currentframe().f_code.co_name
    log2 = logger.getChild(funcName)
    log2.info(parent_directory)
    

    
if __name__ == "__main__":
    parent_directory = r"C:\my\cool\directory"
    file_name = "newLog"
    logMaker(parent_directory, file_name)
    logger = logging.getLogger(__name__)
    logger.info('Logging established successfully')
    printLogLocation(parent_directory)
    