"""
Global settings file
"""

# SQL Server Connection Properties
SQL_HOST = 'DESKTOP-K7UF6T9\SQLEXPRESS' # your server name here (open SSMS, top of Object Explorer)
SQL_DATABASE = 'ChinaBank' # or your database that you prefer to use
SQL_USERNAME = 'pylogin'  # username per the setup documentation
SQL_PASSWORD = 'pypass' # password per the setup documentation
SQL_CONNECTION_STRING = 'DRIVER={SQL Server};SERVER='+SQL_HOST+\
    ';DATABASE='+SQL_DATABASE+';UID='+SQL_USERNAME+';PWD='+ SQL_PASSWORD # full connection string
