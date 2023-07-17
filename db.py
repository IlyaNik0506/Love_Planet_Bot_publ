from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from gui_frames import LogFrame
from settings import DB_NAME
from models import Base, Simp


def db_engine():
    '''Создает базу данных(БД) и таблицы, возвращает экземпляр движка,
    если уже создана, то просто возвращает экземпляр движка'''
    engine = create_engine(f'sqlite:///{DB_NAME}', echo=True)
    Base.metadata.create_all(engine)
    return engine


def db_session():
    '''Возвращает объект сессии для работы с данными в БД'''
    engine = db_engine()
    return sessionmaker(bind=engine)


def add_simp(data: list):
    '''Добавляет экземпляр контакта в БД'''
    simp = Simp(
        name=data[0], age=data[1], region=data[2], link=data[3], phone=data[4],
        chat=data[5]
    )
    session = db_session()
    with session() as session:
        session.add(simp)
        session.commit()


def update_simp(data: list):
    '''Обновляет экземпляр контакта в БД'''
    session = db_session()
    with session() as session:
        simp = session.query(Simp).filter_by(link=data[3]).first()
        simp.phone = data[4]
        simp.chat = data[5]
        session.commit()


def check_simp(data: list):
    '''Проверяет наличие экземпляра контакта в БД'''
    session = db_session()
    with session() as session:
        check = session.query(Simp).filter_by(link=data[3]).count()
        session.commit()
        return 0 if check != 0 else 1


def add_update_simp(logger: LogFrame, contact_info: list):
    " В зависимости наличия контакта в БД добавляет или обновляет данные. "
    if check_simp(contact_info):
        logger.print_to_log(f'Добавил переписку c {contact_info[0]}.')
        add_simp(contact_info)
    else:
        logger.print_to_log(f'Обновил переписку с {contact_info[0]}.')
        update_simp(contact_info)
