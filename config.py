import os

TESTING = True
DEBUG = True
FLASK_ENV = 'development'
STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'
SECRET_KEY = '\xb3\xe6\x18\xfe\xde\xfa\xf2h\xf3\x14\x90\x9b\xa8\x85\xe1\xeb\x81o=\tI\xe9\x8f\x11'

#MYSQL CONFIGS
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'Root@123'
MYSQL_DB = 'SEMDB'

#SQLAlchemy CONFIGS
SQLALCHEMY_DATABASE_URI = 'mysql://root:Root@123@localhost/SEMDB'

#Celery config
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# aws
S3_BUCKET = os.environ.get("S3_BUCKET")
S3_KEY = os.environ.get("S3_KEY")
S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
