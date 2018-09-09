import os

class Config:
	SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
	SECRET_KEY = os.environ.get("SECRET_KEY")
	UPLOADED_PHOTOS_DEST = 'app/static/photos'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
	SUBJECT_PREFIX = 'PITCH'
	SENDER_EMAIL = 'benkaranja43@gmail.com'



class ProdConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
