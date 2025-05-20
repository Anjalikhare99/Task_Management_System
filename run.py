from app import create_app, db
from flask.cli import with_appcontext
import click

app = create_app()

@app.cli.command("create-db")
@with_appcontext
def create_db():
    db.create_all()
    print("Database tables created.")
