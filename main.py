import bot
import asyncio
from dotenv import load_dotenv

load_dotenv()
loop = asyncio.get_event_loop()
loop.run_until_complete(bot.main())