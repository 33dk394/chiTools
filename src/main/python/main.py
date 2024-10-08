import logging
import logging.config

from chitools import chitool
from chitools.utils.proj_logger import proj_logger

logging.config.dictConfig(proj_logger.cfg_logger)
logger = logging.getLogger(__name__)

def main():
    logger.info("This is main")
    chitool.main()
    
if __name__ == "__main__":# pragma: no cover
    main()