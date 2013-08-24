from todo import bcrypt
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean, Float
from sqlalchemy.orm import relationship
from database import Base


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    tasks = relationship('Task', backref='category')

    def __init__(self, name=None):
        self.name = name

    def info(self):
        category_dict = dict()
        category_dict['id'] = self.id
        category_dict['name'] = self.name
        return category_dict

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    due_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    description = Column(String(150), nullable=False)
    notes = Column(Text)
    complete = Column(Boolean)
    latitude = Column(Float)
    longitude = Column(Float)
    attachment = Column(Text)

    def __init__(self, due_date=None, description=None, user_id=None, notes=None, complete=False, latitude=None, longitude=None, attachment=None, category_id=None):
        self.description = description
        self.due_date = due_date
        self.user_id = user_id
        self.notes = notes
        self.complete = complete
        self.latitude = latitude
        self.longitude = longitude
        self.attachment = attachment
        self.category_id = category_id

    def __repr__(self):
        return '<Task %r>' % (self.description)

    def info(self):
        task_dict = dict()
        task_dict['id'] = self.id
        task_dict['description'] = self.description
        task_dict['user_id'] = self.user_id
        task_dict['notes'] = self.notes
        task_dict['complete'] = self.complete
        task_dict['latitude'] = self.latitude
        task_dict['longitude'] = self.longitude
        task_dict['attachment'] = self.attachment
        task_dict['category_id'] = self.category_id
        category = Category.query.get(self.category_id)
        task_dict['category_name'] = category.name
        return task_dict


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False)
    password = Column(String(60), nullable=False)  # Stored as hash
    tasks = relationship('Task', backref='user')

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % (self.username)

    def info(self):
        user_dict = dict()
        user_dict['id'] = self.id
        user_dict['name'] = self.username
        return user_dict

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def is_valid(self, password=None):
        return bcrypt.check_password_hash(self.password, password)
