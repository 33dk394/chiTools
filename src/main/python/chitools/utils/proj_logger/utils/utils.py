import logging
import logging.config

if __package__:
    from .. import configs

def setlogger():
    logging.config.dictConfig(configs.cfg_logger)
    # logging.info("\033[2J")

if __name__ == "__main__":
    import sys
    sys.path.append("./src/main/python/chitools/utils/proj_logger")
    import configs, formatters
    configs.cfg_logger["handlers"]["file"]["filename"] = "./test.log"
    configs.cfg_logger["formatters"]["colored"]["()"] = "__main__.formatters.ColoredFormatter"
    setlogger()
    logger = logging.getLogger(__name__)

    def make_err():
        try:
            _ = 1/0
        except Exception as e:
            logger.error(f'Error: {e}', exc_info=True)

    def log_msg():
        logger.debug("This is DEBUG")
        logger.info("This is INFO")
        logger.warning("This is WARN")
        logger.error("This is ERROR")
        logger.critical("This is CRITICAL")


    make_err()
    log_msg()