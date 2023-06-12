from db import Base
from sqlalchemy import Integer, Column, String

class Users(Base):
    __tablename__ = "Images"
    id = Column(Integer, primary_key=True, index=True)
    f_name = Column(String(50), index=True)
    m_name = Column(String(50), index=True)
    l_name = Column(String(50), index=True)
    user_label = Column(String(255), index=True)