import logging

cfg_logger = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "detailed": {
            "class": "logging.Formatter",
            "format": "%(asctime)s [%(levelname)8s] | [%(filename)s:%(lineno)d] | %(processName)-10s : %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "()" : "__main__.ColoredFormatter",
            "format": "%(asctime)s [%(levelname).1s] : %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "INFO"
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "log.log",
            "mode": "a",
            "formatter": "detailed",
            "level": "DEBUG"
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "DEBUG"
    },
}
from colorama import Back, Fore, Style

COLORS = {
    "WARNING": Fore.YELLOW,
    "INFO": Fore.CYAN,
    "DEBUG": Fore.BLUE,
    "CRITICAL": Fore.YELLOW,
    "ERROR": Fore.RED,
}

class ColoredFormatter(logging.Formatter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def format(self, record):
        msg = super().format(record)

        levelname = record.levelname
        if hasattr(record, "color"):
            return f"{record.color}{msg}{Style.RESET_ALL}"
        if levelname in COLORS:
            return f"{COLORS[levelname]}{msg}{Style.RESET_ALL}"
        return msg


if __name__ == "__main__":
    import logging.config
    logging.config.dictConfig(cfg_logger)
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

    cfg_logger["handlers"]["file"]["filename"] = "test.log"


    make_err()
    log_msg()