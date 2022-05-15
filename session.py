from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DB_URL


engine = create_engine(DB_URL, echo=True)
Session = sessionmaker(bind=engine)
