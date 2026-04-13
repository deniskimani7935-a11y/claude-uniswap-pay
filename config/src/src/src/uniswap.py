import os
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class UniswapTrader:
    async def buy_eth(self, usd_amount: float):
        logger.info(f"Would buy ${usd_amount} worth of ETH")
        return {"status": "simulated", "usd_amount": usd_amount}
