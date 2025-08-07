
'''logMakaer func defines a logger '__main__' when initiated. Requires
a valid parent directory, file name in str format as arguments.

log children can be initiated by calling the base logging function '.getChildren()'
on the class object.

use of @log will log a starting and ending of the functions 
a child of __main__ for easier debug.
'''


import logging
from datetime import datetime
import os


def logMaker(parent_directory: str, file_name: str = 'scriptLog') -> logging.Logger:
    
    #confirm dtypes for arguments

    if type(parent_directory) != str:
        raise Exception("Argument 'parent_directory' requires type: str as input")
    elif type(file_name) != str:
        raise Exception("Argument 'file_name' requires type: str as input")
    elif os.path.exists(parent_directory) != True:
        raise Exception(f"parent_directory '{parent_directory}' does not exist")
    
    
    #convert file name and parent directory to literal path for logger
    today = datetime.now().date().strftime('%m%d%Y')
    rel_log_path = file_name + f"_{today}.LOG"
    lit_log_path = os.path.join(parent_directory, rel_log_path)
    
    #define logger as __main__
    logger = logging.getLogger('__main__')
    
    #initiate handler classes
    fh = logging.FileHandler(lit_log_path)
    ch = logging.StreamHandler() 
    
    #set handler formatting
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    #set handler levels
    fh.setLevel(logging.INFO)
    ch.setLevel(logging.INFO)
    
    #add handlers to __main__ logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.setLevel(logging.INFO)

    
    return logger
    

def log_deco(func):

    def wrapper(*args, **kwargs):
        log = logging.getLogger('__main__')
        log2 = log.getChild(func.__name__)
        log2.info(f"Starting {func.__name__}")
        func(*args, **kwargs)
        log2.info(f"{func.__name__} has completed")
    return wrapper

    