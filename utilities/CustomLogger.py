import logging

class LogGen:
    @staticmethod
    def logger():
        logger = logging.getLogger(
            __name__)  # at run time it will passses the name of the file so that we can capture the test case name

        # To print the log in file

        # For File

        #fileHandler = logging.FileHandler('../Logs/logfile.log')
        fileHandler = logging.FileHandler('.\\Logs\\logfile.log')
        #fileHandler = logging.FileHandler('C:\\Users\deshmuks\\PycharmProjects\\PythonSelfFramework\\nopcommerceApp\\Logs\\logfile.log')

        # For Format of the logs
        formatter = logging.Formatter("%(asctime)s :%(levelname)s  :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # will filehandler object i.e. location of file
        logger.setLevel(logging.INFO)
        return logger
"""
        #logging.basicConfig(filename='../Logs/automation.log',
                            #format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        logging.basicConfig(filename='.\\Logs\\automation.log',
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

 """
