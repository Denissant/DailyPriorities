from app import db


class Task(db.Model):
    """
    contains tasks and their priorities
    """
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    priority = db.Column(db.Integer)

    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority

    def __repr__(self):
        return f'{self.id}. {self.title}'

    @classmethod
    def add(cls, title, description, priority):
        task = cls(title, description, priority)
        db.session.add(task)
        db.session.commit()
