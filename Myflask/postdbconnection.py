from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

engine = create_engine('mysql+pymysql://root:994410@localhost:3306/books')
Base = declarative_base()


class User2(Base):
    __tablename__ = 'post'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    title = Column(String(64), primary_key=True)
    name = Column(String(64), primary_key=True)
    depart = Column(String(64), primary_key=True)
    ctent = Column(String(1000), nullable=False, index=True)
    time = Column(String(64), primary_key=True)
    url = Column(String(64), primary_key=True)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)

Base.metadata.create_all(engine)


