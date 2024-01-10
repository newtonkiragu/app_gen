from flask_appbuilder.security.sqla.models import User
from sqlalchemy import Column, Integer, ForeignKey, String, Sequence, Table
from sqlalchemy.orm import relationship, backref
from flask_appbuilder import Model


class MyUser(User):
    __tablename__ = "ab_user"
    extra = Column(String(256))
