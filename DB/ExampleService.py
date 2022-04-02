from datetime import datetime

from DB.TelegramUser import TelegramUser
from DB.database import Session


class ExampleService:

    def __init__(self, session=None):
        self.session = session or Session()

    def get_user(self, id):
        return None if self.session.query(TelegramUser).count() == 0 else self.session.query(TelegramUser).filter(
            TelegramUser.id == id).one()

    def find_or_register_new_user(self, id, first_name, last_name, binance_key):
        user = self.get_user(id)
        if user != None:
            return user
        else:
            return TelegramUser.register_new_user(self, id, first_name, last_name, binance_key)

    def register_new_user(self, id, first_name, last_name, binance_key):
        my_user = TelegramUser(
            id=id,
            first_name=first_name,
            last_name=last_name,
            binance_key=binance_key,
            registration_date=datetime.now()
        )

        self.session.add(my_user)  # Add user to the session
        self.session.commit()  # Save changes to the database
        self.session.close()

        return my_user
