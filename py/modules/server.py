"""
Main connection to SQL Server for use throughout
"""
import pyodbc
from .settings import SQL_CONNECTION_STRING


class ServerConnection:
    """
    Server connection object for use in Pandas dfs or ad-hoc queries
    """

    def __init__(self):
        self.connection = pyodbc.connect(SQL_CONNECTION_STRING) # for use in pandas connections
        self.cursor = self.connection.cursor() # for use in ad-hoc queries if necessary
