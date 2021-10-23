"""
Global settings file
"""
from sqlalchemy.engine import URL

# SQL Server Connection Properties
SQL_HOST = 'DESKTOP-8TLT5OK\SQLEXPRESS' # your server name here (open SSMS, top of Object Explorer)
SQL_DATABASE = 'ChinaBank' # or your database that you prefer to use
SQL_USERNAME = 'pylogin'  # username per the setup documentation
SQL_PASSWORD = 'pypass' # password per the setup documentation
SQL_CONNECTION_STRING = URL.create(
    "mssql+pyodbc",
    username=SQL_USERNAME,
    password=SQL_PASSWORD,
    host=SQL_HOST,
    port=1433,
    database=SQL_DATABASE,
    query={
        "driver":"SQL Server",
        "authentication": "ActiveDirectoryIntegrated",
    }
)
