from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_exec import Articles, Base


#engine=create_engine('sqlite:///db.sqlite3')
engine=create_engine('mysql+mysqldb://jblnt:rMaKukBWHqnP8a@localhost/django_newsapp')

Base.metadata.create_all(engine)

dbSession=sessionmaker(bind=engine)
session=dbSession()

def articleDBInsert(aTitle, aSlug, aContent, aTag, aSource, aDate, aImages):
    new_article=Articles(title=aTitle, slug=aSlug, content=aContent, tag=aTag, source=aSource, date=aDate, images=aImages)
    session.add(new_article)
