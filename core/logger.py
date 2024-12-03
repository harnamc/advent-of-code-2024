import logging


def get_logger(name=__name__, log_level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    if not logger.hasHandlers():
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger
