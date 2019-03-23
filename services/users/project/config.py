""" Enviroment configuration file """


class BaseConfig:
    """ Base Configuration """
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """ Development Configurations """
    pass


class TestingConfig(BaseConfig):
    """ Testing Configurations """
    TESTING = True


class ProductionConfig(BaseConfig):
    """ Production Configurations """
    pass


app_config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}