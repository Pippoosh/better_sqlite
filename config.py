import sqlite3


class Config:
    def __init__(self, connection: str):
        """
        Initialize the Config class with a database connection.

        Args:
            connection (str): The database file path or database URL to connect to.
        """
        # Establish a connection to the SQLite database
        self.connection = sqlite3.connect(connection)
        # Create a cursor object to execute SQL commands
        self.cursor = self.connection.cursor()
