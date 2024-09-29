import asyncio
import websockets


async def echo_plus_server(websocket):
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send(f"Echo: {message} from server")


async def main():
    async with websockets.serve(echo_plus_server, "localhost", 8765):
        print("Server started on ws://localhost:8765")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
