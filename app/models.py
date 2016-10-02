from .extentions import db
from sqlalchemy import func

class Entity:
    id = db.Column(db.Integer, primary_key=True)

class TimestampMixin:
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

class FirstModel(db.Model,Entity,TimestampMixin):
    parent_id = db.Column(db.Integer, db.ForeignKey('first_model.id'), index=True)
    parent_relationship = db.relationship('FirstModel', backref=db.backref('parent', remote_side='FirstModel.id'))
    title = db.Column(db.String)
    description = db.Column(db.String)

    def __init__(self,id,created_at,updated_at,parent_id,title,description):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.parent_id = parent_id
        self.title = title
        self.description = description
    
    


