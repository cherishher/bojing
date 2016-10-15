# -*- coding: utf-8 -*-
# @Date    : 2016/10/1  20:51
# @Author  : 490949611@qq.com
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from db import engine

Base = declarative_base()

class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(96), nullable=False)
    time = Column(String(96),nullable=False)
    profile = Column(String(1024),nullable=False)



if __name__ == '__main__':
	Base.metadata.create_all(engine)