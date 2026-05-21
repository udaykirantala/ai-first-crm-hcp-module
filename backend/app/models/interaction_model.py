from sqlalchemy import Column, Integer, String

from app.database.db import Base


class Interaction(Base):

    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_name = Column(String(255))

    hospital = Column(String(255))

    interaction_type = Column(String(100))

    date = Column(String(100))

    time = Column(String(100))

    attendees = Column(String(500))

    topic = Column(String(500))

    materials_shared = Column(String(500))

    samples_distributed = Column(String(500))

    sentiment = Column(String(100))

    outcomes = Column(String(500))

    follow_up = Column(String(500))

    summary = Column(String(1000))

    followup_recommendation = Column(String(1000))