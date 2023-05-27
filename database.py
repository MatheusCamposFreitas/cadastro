from sqlalchemy import create_engine
from domain.user import User

engine = create_engine('mysql://root:root@localhost:3306/appa')  # URL de conexão do SQLite
User.metadata.create_all(engine)
