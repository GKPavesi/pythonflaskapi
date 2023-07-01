from dotenv import load_dotenv

import os
import string
import random

load_dotenv()

random_str = string.ascii_letters + string.digits + string.ascii_uppercase

SECRET_KEY = ''.join(random.choice(random_str) for i in range(12))
SQLALCHEMY_TRACK_NOTIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
DEBUG = False if os.getenv('ENVIRONMENT') == 'production' else True
