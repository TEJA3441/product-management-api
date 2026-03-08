import logging

logging.basicConfig(
    filename="logs/activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

logger = logging.getLogger()


def log_action(message: str):

    logger.info(message)