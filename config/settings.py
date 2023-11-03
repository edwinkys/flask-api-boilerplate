from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Should be False in production.
DEBUG = getenv("DEBUG") == "true" or False

# Required by Flask for security.
SECRET_KEY = getenv("SECRET_KEY", "secretkey")
