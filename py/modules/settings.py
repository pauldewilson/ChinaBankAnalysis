"""
Global settings file
"""
import os
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

def list_parent_and_subdirs(rootdir):
    """
    Recursively returns all subdirectories of provided rootdir
    For use in SCRAPER_TARGET_DIRECTORIES if required
    """
    dirs = [rootdir]
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            dirs.append(d)
            list_parent_and_subdirs(d)
    return dirs

# Scraper settings
SCRAPER_VALID_FILETYPES = ['xlsx', 'xlsm']
SCRAPER_TARGET_DIRECTORIES = list_parent_and_subdirs(r'C:\Users\me\Desktop\test')
SCRAPER_TOTAL_COLUMNS = 300
SCRAPER_TOTAL_ROWS = 4000
