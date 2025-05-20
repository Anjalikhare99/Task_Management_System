import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:python%40885@localhost/task_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "your_secret_key_here"
