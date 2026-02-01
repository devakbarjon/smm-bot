import logging
import logging.handlers
import os


def setup_logging():
    log_dir = "app/data/logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    file_handler = logging.handlers.RotatingFileHandler(
        os.path.join(log_dir, "bot.log"), maxBytes=1024 * 1024 * 5, backupCount=5
    )

    # Set levels for handlers
    console_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)

    # Create formatters and add it to handlers
    console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)
    file_handler.setFormatter(file_format)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
