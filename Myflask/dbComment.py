from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

engine = create_engine('mysql+pymysql://root:994410@localhost:3306/books')
Base = declarative_base()

class Comment(Base):

    __tablename__ = 'comments'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    title_name = Column(String(64) )
    ctent = Column(String(100), nullable=False, index=True)
    time = Column(String(64), primary_key=True)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)
Base.metadata.create_all(engine)