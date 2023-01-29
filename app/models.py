from sqlalchemy import Column, Integer, SmallInteger, Float
from .database import Base


class clicks(Base):
    __tablename__ = "clicks"
    id = Column(Integer, primary_key=True, nullable=False)
    x = Column(Float, nullable=False, server_default = '0')
    y = Column(Float, nullable=False, server_default = '0')
    cluster_id = Column(SmallInteger, nullable=False, server_default = '-1')