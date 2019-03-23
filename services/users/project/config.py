""" Enviroment configuration file """

import os


class BaseConfig:
    """ Base Configuration """
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """ Development Configurations """
    SQLALCHEMY_DATABASE_URI = os.environ.get( 'DATABASE_URL')


class TestingConfig(BaseConfig):
    """ Testing Configurations """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
    """ Production Configurations """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


app_config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}