import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Myflask.dbconnection import User

engine = create_engine('mysql+pymysql://root:994410@localhost:3306/books')
ed_user = User( username='ed', password='Ed Jones', email='edsnickname')
Session = sessionmaker(bind=engine)
session = Session()
session.add(ed_user)
session.commit()

for user in session.query(User).filter(User.username == 'ed').all():
    print(user.id)


