"""
Main connection to SQL Server for use throughout
"""
from sqlalchemy import create_engine
from .settings import SQL_CONNECTION_STRING


class ServerConnection:
    """
    Server connection object for use in Pandas dfs or ad-hoc queries
    """

    def __init__(self):
        self.engine = create_engine(SQL_CONNECTION_STRING) # for use in pandas connections
        self.connection = self.engine.connect() # for use in ad-hoc queries if necessary
