import asyncio
import websockets


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as ws:
        msg = "Hello, websocket!"
        print(f"Sending message: {msg}")
        await ws.send(msg)
        response = await ws.recv()
        print(f"Received response: {response}")


if __name__ == "__main__":
    asyncio.run(hello())
