from typing import Dict


class CategoryConfig:
    def __init__(self) -> None:
        self.archived = None
        self.upcoming_events = None


class ChannelConfig:
    def __init__(self) -> None:
        self.date_of_channel_id: Dict[str, str] = {}


class GeneralConfig:
    def __init__(self) -> None:
        self.reminder = True

class Config:
    def __init__(self) -> None:
        self.category = CategoryConfig()
        self.channel = ChannelConfig()
        self.general = GeneralConfig()
