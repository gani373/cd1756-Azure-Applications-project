import os

class Config(object):
    # Flask app security
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Azure Blob Storage
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER')
    
    # SQL Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Authentication
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    AUTHORITY = os.environ.get("AUTHORITY")
    REDIRECT_PATH = os.environ.get("REDIRECT_PATH")
    SCOPE = os.environ.get("SCOPE").split(' ') if os.environ.get("SCOPE") else ["User.Read"]

    SESSION_TYPE = "filesystem"
