from app.models import db, BaseModel


class RoleModel(BaseModel):
    """User's role"""
    __tablename__ = 'role'
    __bind_key__ = 'default'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
