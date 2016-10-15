# -*- coding: utf-8 -*-
# @Date    : 2016/10/1  20:51
# @Author  : 490949611@qq.com
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from db import engine

Base = declarative_base()

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    name = Column(String(96), nullable=False)
    phonenum = Column(String(96),nullable=False)
    email = Column(String(96),nullable=False)
    message = Column(String(1024),nullable=False)


if __name__ == '__main__':
	Base.metadata.create_all(engine)