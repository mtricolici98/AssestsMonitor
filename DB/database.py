from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(r'sqlite:///C:\Users\Eugen\PycharmProjects\AssestsMonitor\AssestsMonitor.db')
Base = declarative_base(engine)
Session = sessionmaker(bind=engine)