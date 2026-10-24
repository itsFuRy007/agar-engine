import asyncio
from dataclasses import dataclass
from enum import Enum
from typing import Optional

import websockets
from websockets.asyncio.client import ClientConnection


class ConnectionState(str, Enum):
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    ERROR = "error"


@dataclass
class GameClient:
    client_id: str
    state: ConnectionState = ConnectionState.DISCONNECTED
    last_error: Optional[str] = None
    _ws: Optional[ClientConnection] = None

    async def connect(self, uri: str) -> None:
        if self._ws is not None:
            raise RuntimeError("Client is already connected.")

        if not uri.startswith("wss://"):
            raise ValueError("A secure wss:// endpoint is required.")

        self.state = ConnectionState.CONNECTING
        self.last_error = None

        try:
            self._ws = await websockets.connect(
                uri,
                open_timeout=10,
                close_timeout=5,
                ping_interval=20,
                ping_timeout=20,
                max_size=2**20,
            )
            self.state = ConnectionState.CONNECTED
        except Exception as exc:
            self.state = ConnectionState.ERROR
            self.last_error = f"{type(exc).__name__}: {exc}"
            self._ws = None
            raise

    async def send(self, message: str | bytes) -> None:
        if self._ws is None:
            raise RuntimeError("Client is not connected.")
        await self._ws.send(message)

    async def receive(self) -> str | bytes:
        if self._ws is None:
            raise RuntimeError("Client is not connected.")
        return await self._ws.recv()

    async def disconnect(self) -> None:
        ws, self._ws = self._ws, None
        if ws is not None:
            await ws.close()
        self.state = ConnectionState.DISCONNECTED
        self.last_error = None


async def main() -> None:
    client = GameClient(client_id="test-1")
    print({
        "client_id": client.client_id,
        "state": client.state.value,
        "note": "No game server configured; no game connection attempted.",
    })


if __name__ == "__main__":
    asyncio.run(main())
