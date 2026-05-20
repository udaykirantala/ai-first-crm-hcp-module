from sqlalchemy import Column, Integer, String

from app.database.db import Base


class Interaction(Base):

    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_name = Column(String(255))
    hospital = Column(String(255))
    topic = Column(String(255))
    sentiment = Column(String(255))
    follow_up = Column(String(255))

    summary = Column(String(500))

    followup_recommendation = Column(String(500))