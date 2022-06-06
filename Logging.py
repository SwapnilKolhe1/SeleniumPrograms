import logging

# Create and configure logger
logging.basicConfig(filename="CT9.log", format='%(asctime)s %(message)s', filemode='w')

logger = logging.getLogger("Logger_Name")       # Create logger object with configuration and name

logger.setLevel(logging.DEBUG)

logger.error("Your error message!")
logger.critical("Your critical message!")
logger.debug("Your debug message!")
logger.info("Your info message!")
logger.warning("Your warning message!")

