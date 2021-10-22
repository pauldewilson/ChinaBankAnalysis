"""
Global settings file
"""

# SQL Server Connection Properties
SQL_HOST = 'DESKTOP-8TLT5OK\SQLEXPRESS' # your server name here (open SSMS, top of Object Explorer)
SQL_DATABASE = 'ChinaBank' # or your database that you prefer to use
SQL_USERNAME = 'pylogin'  # username per the setup documentation
SQL_PASSWORD = 'pypass' # password per the setup documentation
SQL_CONNECTION_STRING = f'mssql+pyodbc://{SQL_USERNAME}:{SQL_PASSWORD}\
    @{SQL_HOST}/{SQL_DATABASE}?driver=SQL Server' # full connection string
