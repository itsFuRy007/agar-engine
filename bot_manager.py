from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class BotState(str, Enum):
    STOPPED = "stopped"
    NOT_IMPLEMENTED = "not_implemented"
    CONNECTED = "connected"
    ERROR = "error"


@dataclass
class Bot:
    bot_id: int
    nickname: str
    state: BotState = BotState.STOPPED
    target_uid: Optional[str] = None
    last_error: Optional[str] = None


@dataclass
class BotManager:
    bots: dict[int, Bot] = field(default_factory=dict)

    def create_bots(self, count: int, nickname_prefix: str = "Bot") -> None:
        if not 1 <= count <= 50:
            raise ValueError("Count must be between 1 and 50.")

        for bot_id in range(1, count + 1):
            self.bots.setdefault(
                bot_id,
                Bot(bot_id=bot_id, nickname=f"{nickname_prefix}{bot_id}")
            )

    def set_target(self, uid: str) -> None:
        uid = uid.strip()
        if not uid:
            raise ValueError("UID cannot be empty.")

        for bot in self.bots.values():
            bot.target_uid = uid

    def start_bot(self, bot_id: int) -> None:
        bot = self.bots.get(bot_id)
        if bot is None:
            raise ValueError(f"Bot {bot_id} does not exist.")

        bot.state = BotState.NOT_IMPLEMENTED
        bot.last_error = "Game connection is not implemented yet."

    def stop_bot(self, bot_id: int) -> None:
        bot = self.bots.get(bot_id)
        if bot is None:
            raise ValueError(f"Bot {bot_id} does not exist.")

        bot.state = BotState.STOPPED
        bot.last_error = None

    def start_all(self) -> None:
        for bot in self.bots.values():
            self.start_bot(bot.bot_id)

    def stop_all(self) -> None:
        for bot in self.bots.values():
            self.stop_bot(bot.bot_id)

    def status(self) -> list[dict]:
        return [
            {
                "id": bot.bot_id,
                "nickname": bot.nickname,
                "state": bot.state.value,
                "target_uid": bot.target_uid,
                "last_error": bot.last_error,
            }
            for bot in self.bots.values()
        ]


if __name__ == "__main__":
    manager = BotManager()
    manager.create_bots(3)
    manager.start_all()
    for bot in manager.status():
        print(bot)
