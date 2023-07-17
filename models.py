from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Simp(Base):
    '''
    Модель контакта на основе полученной информации\n
    Состоит:\n
    \tid - задаётся автоматически\n
    \tname - имя\n
    \tage - возраст\n
    \tregion - регион проживания\n
    \tlink - ссылка на профиль\n
    \tphone - телефон\n
    \tchat - переписка\n
    \tchat - переписка\n
    '''
    __tablename__ = "simp_db"

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    age = Column(Integer)
    region = Column(String(150))
    link = Column(String(300), unique=True)
    phone = Column(String(150), nullable=True)
    chat = Column(Text)
    date = Column(DateTime, nullable=True, default=datetime.now)
