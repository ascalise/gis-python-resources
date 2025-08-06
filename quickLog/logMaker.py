
# logMakaer func defines a logger '__main__' when initiated. Requires
# a valid parent directory, file name in str format as arguments.

# log children can be initiated by calling the base logging function '.getChildren()'
# on the class object.

#use of @log will log a starting and ending of the function
# s a child of __main__ for easier debug.


from devPackages.dependencies import *


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
    

def log(func):

    def wrapper(*args, **kwargs):
        log = logging.getLogger('__main__')
        log2 = log.getChild(func.__name__)
        log2.info(f"Starting {func.__name__}")
        func(*args, **kwargs)
        log2.info(f"{func.__name__} has completed")
    return wrapper

#sample code

# @log
# def printLogLocation(parent_directory):
#     log = logging.getLogger(__name__)
#     funcName = inspect.currentframe().f_code.co_name
#     log2 = log.getChild(funcName)
#     log2.info(parent_directory)
    

    
# if __name__ == "__main__":
#     parent_directory = r"C:\Users\austi\OneDrive - North West Utility District\pythonProjects\loggingProjects\testing"
#     file_name = "yesNew"
#     logMaker(parent_directory, file_name)
#     logger = logging.getLogger(__name__)
#     logger.info('Logging established successfully')
#     printLogLocation(parent_directory)
    
    