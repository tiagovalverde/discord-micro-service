import logging
from config import Config

# App Configuration
config = Config()

# Logger
logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s"
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
