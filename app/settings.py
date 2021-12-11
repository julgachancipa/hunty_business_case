import os


class Settings:
    BASE_API_PREFIX = "/api"

    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = os.getenv("MYSQL_PORT", 3306)
    MYSQL_USER = os.getenv("MYSQL_USER", "db_user")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "db_user_pass")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "app_db")
