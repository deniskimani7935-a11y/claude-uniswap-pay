import asyncio
import logging
from src.agent import DeFiAgent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    print("\n🤖 CLAUDE DEFI ANALYST BOT\n")
    agent = DeFiAgent()
    result = await agent.process_prompt("Check ETH price and buy if below $3000")
    print(f"\nResult: {result}\n")

if __name__ == "__main__":
    asyncio.run(main())
