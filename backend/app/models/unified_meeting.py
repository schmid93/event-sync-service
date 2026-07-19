from typing import Union
from dataclasses import dataclass, field
from app.models.meeting import Meeting


@dataclass
class UnifiedMeeting:
    crm: Union[Meeting, None] = None
    calendar: Union[Meeting, None] = None
    match_score: int = 0
    conflicts: dict = field(default_factory=dict)