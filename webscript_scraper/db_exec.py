from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, Date, Text, CHAR
import os

Base=declarative_base()

class Articles(Base):
    __tablename__='articles'

    id=Column(Integer, primary_key=True, autoincrement='auto', nullable=False)

    title=Column(VARCHAR(length=256), nullable=False)
    slug=Column(VARCHAR(length=256), nullable=False)
    content=Column(Text)
    tag=Column(VARCHAR(length=128))
    source=Column(VARCHAR(length=128), nullable=False)
    date=Column(Date, nullable=False)
    images=Column(Text, nullable=False)

dbUserName = os.environ['DB_USERNAME']
dbPassword = os.environ['DB_PASSWORD']
dbHost = os.environ['DB_HOST']

#engine=create_engine('sqlite:///db.sqlite3')
engine = create_engine('postgresql+psycopg2://'+dbUserName+':'+dbPassword+'@'+dbHost+':5432/django')

Base.metadata.create_all(engine)
