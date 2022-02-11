from pydantic import BaseModel
from typing import Optional, List


class MandrillData(BaseModel):
    event: Optional[str] = None
    event_id: Optional[int] = None
    ts: Optional[str] = None
    message_ts: Optional[str] = None
    subject: Optional[str] = None
    email: Optional[str] = None
    sender: Optional[str] = None
    state: Optional[str] = None
    message_id: int
    time_opened: Optional[str] = None
    time_clicked: Optional[str] = None
    url_clicked: Optional[str] = None
