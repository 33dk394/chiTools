import logging
import logging.config

from chitools import chitool
from chitools.utils import proj_logger

proj_logger.setlogger()
logger = logging.getLogger(__name__)

def main():
    logger.debug("This is DEBUG")
    logger.info("This is INFO")
    logger.warning("This is WARN")
    logger.error("This is ERROR")
    logger.critical("This is CRITICAL")
    # chitool.main()
    
if __name__ == "__main__":# pragma: no cover
    main()