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
            "format": "%(asctime)s [%(levelname)s] : %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "colored": {
            "()" : "__main__.proj_logger.ColoredFormatter",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "colored",
            "level": "DEBUG"
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
