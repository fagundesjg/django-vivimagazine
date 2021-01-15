import os


class Configs:
    SECRET_KEY = os.getenv('SECRET_KEY', 'batata')
