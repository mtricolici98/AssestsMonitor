from DB.database import Base, Session
from datetime import datetime
from sqlalchemy import Column, Integer, String, Date, Text


class TelegramUser(Base):
    __tablename__ = 'telegram_users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    binance_key = Column(Text, nullable=False)
    debank_key = Column(Text)
    registration_date = Column(Date(), default=datetime.now)

    def __repr__(self):
        return f"{self.first_name}, {self.last_name}, registered on {self.registration_date}"

    def __str__(self):
        return repr(self)

Base.metadata.create_all()
