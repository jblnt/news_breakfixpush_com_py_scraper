from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, Date, Text, CHAR

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

#engine=create_engine('sqlite:///db.sqlite3')
#engine=create_engine('mysql+mysqldb://jblnt:rMaKukBWHqnP8a@localhost/django_newsapp')
engine = create_engine('postgresql+psycopg2://jblnt:zk5WgHFqSu@localhost:5432/django')

Base.metadata.create_all(engine)
