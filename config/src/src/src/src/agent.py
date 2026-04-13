import os
import logging
from src.price_feed import PriceFeedClient
from src.uniswap import UniswapTrader
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class DeFiAgent:
    def __init__(self):
        self.price_feed = PriceFeedClient()
        self.trader = UniswapTrader()
        self.price_threshold = 3000
        self.buy_amount_usd = 5.0
    
    async def process_prompt(self, user_prompt: str):
        eth_price = await self.price_feed.get_eth_price()
        logger.info(f"ETH Price: ${eth_price}")
        
        if eth_price < self.price_threshold:
            logger.info(f"Price below ${self.price_threshold}, executing buy...")
            result = await self.trader.buy_eth(self.buy_amount_usd)
            return {"action": "BUY_EXECUTED", "price": eth_price, "result": result}
        else:
            logger.info(f"Price above threshold, no action")
            return {"action": "NO_ACTION", "price": eth_price}
