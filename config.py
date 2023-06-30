import os
from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_TRACK_NOTIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
DEBUG = False if os.getenv('ENVIRONMENT') == 'production' else True