from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Meeting:
    # Required fields (no defaults) first
    source: str
    source_id: str
    title: str
    owner: str
    
    # Optional fields with defaults
    client_name: Optional[str] = None
    client_company: Optional[str] = None
    start: Optional[datetime] = None
    location: Optional[str] = None
    status: str = "pending"          
    notes: Optional[str] = None
