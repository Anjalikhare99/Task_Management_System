from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    from .routes import users, projects, tasks

    app = Flask(__name__)
    app.config.from_object("config.Config")
    db.init_app(app)

    migrate.init_app(app, db)

    app.register_blueprint(users.bp)
    app.register_blueprint(projects.bp)
    app.register_blueprint(tasks.bp)

    return app