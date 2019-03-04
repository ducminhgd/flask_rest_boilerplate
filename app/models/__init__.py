from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

db = SQLAlchemy()
migrate = Migrate(db=db)


def init_db(app, **kwargs):
    # db.app = app
    db.init_app(app)
    migrate.init_app(app)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    from app.models.role_model import RoleModel


class BaseModel(db.Model):
    """Base Model with created_at and updated_at"""
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
