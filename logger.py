import logging 

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(level)s | %(message) s",
    handlers=[
        logging.FileHandler("logs/app.log"),

    ],
)
logger = logging.getLogger(__name__)

