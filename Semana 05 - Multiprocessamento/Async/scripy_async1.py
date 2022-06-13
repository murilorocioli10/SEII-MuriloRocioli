import asyncio
from telnetlib import AYT


async def main():
    print("tim")
    # await foo("text")
    task = asyncio.create_task(foo("text"))
    await asyncio.sleep(0.5)
    print("finished")


async def foo(text):
    print(text)
    await asyncio.sleep(10)


asyncio.run(main())
