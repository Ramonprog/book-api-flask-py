from sqlalchemy.dialects.postgresql import UUID, TEXT
from sqlalchemy import func
from db import db

class Book(db.Model):
  __tablename__ = 'book'

  id = db.column(UUID(as_uuid=True), primary_key=True, default=func.uuid_genaret_v4)
  title = db.Column(db.String(255), nullable=False)
  author = db.Column(db.String(255), nullable=False)
  description = db.Column(TEXT, nullable=False)
  isFavorite = db.Column(db.Boolean, nullable=True, default=False)
  isReading = db.Column(db.Boolean, nullable=True, default=False)
  isFinished = db.Column(db.Boolean, nullable=True, default=False)
  created_at = db.Column(db.DateTime, nullable=False, default=func.now())
  updated_at = db.Column(db.DateTime, nullable=False, default=func.now())

  def to_dict(self):
    return {
      'id': str(self.id),
      'title': self.title,
      'author': self.author,
      'description': self.description,
      'isFavorite': self.isFavorite,
      'isReading': self.isReading,
      'isFinished': self.isFinished,
      'created_at': self.created_at,
      'updated_at': self.updated_at
    }