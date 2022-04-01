from database import Base, Session
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

    @staticmethod
    def find_or_register_new_user(id, first_name, last_name, binance_key):
        user = TelegramUser.get_user(id)
        if user != None:
            return user
        else:
            return TelegramUser.register_new_user(id, first_name, last_name, binance_key)

    @staticmethod
    def register_new_user(id, first_name, last_name, binance_key):
        my_user = TelegramUser(
            id=id,
            first_name=first_name,
            last_name=last_name,
            binance_key=binance_key,
            registration_date=datetime.now()
        )

        session = Session()  # Create new session
        session.add(my_user)  # Add user to the session
        session.commit()  # Save changes to the database

        return my_user

    @staticmethod
    def get_user(id):
        session = Session()
        my_user = session.query(id).filter(TelegramUser.id == id).one()
        if my_user:
            return my_user
        else:
            return None

Base.metadata.create_all()
