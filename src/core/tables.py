from datetime import datetime

import sqlalchemy
from databases import Database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine,
    Column,
    BigInteger,
    String,
    Integer,
    ForeignKey,
    exc,
    DATETIME, DateTime, text, Boolean
)
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from .settings import Settings

Base = declarative_base()

engine = create_engine(
    Settings.DB_URL
)

from src.bot.utils import texts


# back_call = 0. quiz = 1
class AfterQuiz(Base):
    __tablename__ = "after_quiz"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), default=None)
    phone = Column(String(20), default=None)
    parameter1 = Column(String(100), default=None)
    parameter2 = Column(Integer, default=None)
    parameter3 = Column(String(100), default=None)
    parameter4 = Column(BigInteger, default=None)
    created_at = Column(DateTime, default=datetime.now, server_default=text('now()'))
    status = Column(String(40), default=None)
    sent = Column(Boolean, default=False)
    type_number = Column(Integer, default=None)

    def __repr__(self):
        return f"{self.name} | {self.phone}"


Base.metadata.create_all(engine)
session_marker = sessionmaker(bind=engine)


@contextmanager
def get_session():
    session = session_marker()
    try:
        yield session
        session.commit()
    except exc.SQLAlchemyError:
        session.rollback()
        raise
    finally:
        session.close()


def crete_after_quiz(name, phone, parameter1=None, parameter2=None, parameter3=None, parameter4=None, type_number=0):
    status = texts.statuses[0]
    with get_session() as session:
        session.add(
            AfterQuiz(name=name, phone=phone, parameter1=parameter1,
                      parameter2=parameter2, parameter3=parameter3,
                      parameter4=parameter4, type_number=type_number, status=status
                      ))

    return True


# quiz
def get_new_quizzes():
    session = session_marker(expire_on_commit=False)
    quizs = session.query(AfterQuiz).filter(AfterQuiz.sent == False).all()
    session.close()
    return quizs


def update_current_quiz_sent(quiz: AfterQuiz):
    with get_session() as session:
        session.query(AfterQuiz).filter(AfterQuiz.id == quiz.id).update(
            {
                AfterQuiz.sent: True,
                AfterQuiz.status: quiz.status if quiz.status is not None else quiz.status
            }
        )
        return True


def get_by_id_quiz(quiz_id):
    session = session_marker(expire_on_commit=False)
    quiz: AfterQuiz = session.query(AfterQuiz).filter(AfterQuiz.id == quiz_id).first()
    session.close()
    return quiz
