from chitools import chitool

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

def main():
    logger.info("This is main")
    chitool.main()
    
if __name__ == "__main__":# pragma: no cover
    main()