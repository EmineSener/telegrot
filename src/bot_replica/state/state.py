from typing import List

from src.common.logger import Logger
from src.scraper.scraper import Scraper
from src.bot_replica.state.admin_state import AdminState
from src.bot_replica.state.announcement_state import AnnouncementState
from src.bot_replica.state.chat_state import ChatState

logger = Logger.getLogger()


class ReplicaState:
    announcement: AnnouncementState
    chat: ChatState
    admin: AdminState

    def __init__(self) -> None:
        ReplicaState.announcement = AnnouncementState()
        ReplicaState.chat = ChatState()
        ReplicaState.admin = AdminState()
        