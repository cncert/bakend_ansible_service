# encoding: utf-8
#  'mysql+pymysql://lmapp:lmapp@localhost/smp'
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    JWT_SECRET_KEY = 'xcbdjkr_dfdfdf_fdefm,_eweewdf!?.'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


