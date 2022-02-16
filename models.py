from sqlalchemy import Column, Integer, String
from database import Base


class MandrillResponse(Base):
    __tablename__ = "mandrill_responses"

    event = Column(String)
    event_id = Column(Integer)
    ts = Column(String)
    message_ts = Column(String)
    subject = Column(String)
    email = Column(String)
    sender = Column(String)
    state = Column(String)

    # message ID is the primary key
    message_id = Column(Integer, primary_key=True)
    time_opened = Column(String)
    time_clicked = Column(String)
    url_clicked = Column(String)
