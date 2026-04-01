from os import environ

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL', 'sqlite:///crm.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = environ.get('SECRET_KEY', 'supersecretkey')

# To use MySQL:
# export DATABASE_URL='mysql+pymysql://root:password@localhost/crm'
# or set in PowerShell:
# $env:DATABASE_URL = 'mysql+pymysql://root:password@localhost/crm'
# Make sure package cryptography is installed for sha256/caching_sha2 auth:
# pip install cryptography
