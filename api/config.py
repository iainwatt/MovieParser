import os


class Config:

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DB = {
        'username': 'root',
        'password': 'root0000',
        'host': '127.0.0.1',
        'database': 'lingswap_dev'
    }


class TestingConfig(Config):
    DB = {
        'username': 'root',
        'password': 'root0000',
        'host': '127.0.0.1',
        'database': 'lingswap_test'
    }


class ProductionConfig(Config):
    DB = {
        'username': os.environ.get('DB_USER', ''),
        'password': os.environ.get('DB_PASSWORDS', ''),
        'host': os.environ.get('DB_HOST', ''),
        'database': os.environ.get('DB_NAME', '')
    }


env_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
