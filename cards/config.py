class DevelopmentConfig(object):
    DATABASE_URI = "sqlite:///cards-development.db"
    DEBUG = True

class TestingConfig(object):
    DATABASE_URI = "sqlite://"
    DEBUG = True