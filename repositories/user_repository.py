from domain.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class UserRepository:
    def __init__(self):
        engine = create_engine('mysql://root:root@localhost:3306/appa')
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create(self, user):
        self.session.add(user)
        self.session.commit()

    def get_by_id(self, user_id):
        return self.session.query(User).filter_by(id=user_id).first()

