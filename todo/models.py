from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean, Float
from sqlalchemy.orm import relationship
from database import Base


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    due_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    category = Column(String(150))
    description = Column(String(150), nullable=False)
    notes = Column(Text)
    complete = Column(Boolean)
    latitude = Column(Float)
    longitude = Column(Float)
    attachment = Column(Text)

    def __init__(self, due_date=None, description=None, user_id=None, notes=None, complete=False, latitude=None, longitude=None, attachment=None, category=None):
        self.description = description
        self.due_date = due_date
        self.user_id = user_id
        self.notes = notes
        self.complete = complete
        self.latitude = latitude
        self.longitude = longitude
        self.attachment = attachment
        self.category = category

    def __repr__(self):
        return '<Task %r>' % (self.name)

    def info(self):
        task_dict = dict()
        task_dict['id'] = self.id
        task_dict['description'] = self.description
        task_dict['user_id'] = self.user_id
        task_dict['notes'] = self.notes
        task_dict['complete'] = self.complete
        task_dict['latitude'] = self.notes
        task_dict['longitude'] = self.complete
        task_dict['attachment'] = self.attachment


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    password = Column(String(60), nullable=False)  # Stored as hash
    tasks = relationship('Task', backref='user')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<User %r>' % (self.name)

    def info(self):
        user_dict = dict()
        user_dict['id'] = self.id
        user_dict['name'] = self.name
        return user_dict
