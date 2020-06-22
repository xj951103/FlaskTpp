

def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE")
    driver = dbinfo.get("DRIVER")
    user = dbinfo.get("USER")
    password = dbinfo.get("PASSWORD")
    db = dbinfo.get("DB")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, db)
    # return "{}://{}:{}@{}:{}/{}".format(engine, user, password, host, port, db)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRECT_KEY = "jonathan",


class DevelopConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "USER": "root",
        "PASSWORD": "root",
        "DRIVER": "pymysql",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "DB": "flaskApi"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class TestConfig(Config):
    TESTING = True
    dbinfo = {
        "ENGINE": "mysql",
        "USER": "root",
        "PASSWORD": "root",
        "DRIVER": "pymysql",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "DB": "flaskApi"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagineConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "USER": "root",
        "PASSWORD": "root",
        "DRIVER": "pymysql",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "DB": "flaskApi"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "USER": "root",
        "PASSWORD": "root",
        "DRIVER": "pymysql",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "DB": "flaskApi"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    "develop": DevelopConfig,
    "testing": TestConfig,
    "staging": StagineConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}