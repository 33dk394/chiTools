import logging
import logging.config

from chitools import chitool
from chitools.utils import proj_logger

proj_logger.setlogger(log_path="res/log", debug_mode=True)
logger = logging.getLogger(__name__)

def main():
    proj_logger.test_log()
    chitool.main()
    
if __name__ == "__main__":# pragma: no cover
    main()