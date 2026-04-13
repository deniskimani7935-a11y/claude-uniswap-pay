import os
import httpx
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class PriceFeedClient:
    async def get_eth_price(self):
        logger.info("Getting ETH price...")
        # Return mock price for testing
        return 2850.50
