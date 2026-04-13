import asyncio
from src.agent import DeFiAgent

async def test():
    agent = DeFiAgent()
    result = await agent.process_prompt("Test")
    print(f"Test result: {result}")

asyncio.run(test())
