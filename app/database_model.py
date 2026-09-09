from sqlalchemy import column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base 


Base = declarative_base()


class Todo(Base):

    __tablename__ = "Todo"

    id = column(Integer, primary_key=True, Index=True)
    title = column(String)
    description = column(String)
    completed = column(Boolean)