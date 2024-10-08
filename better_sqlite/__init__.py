"""
better_sqlite package

This package provides a simple interface for interacting with SQLite databases.
It includes functionalities for database configuration, basic CRUD operations, 
and a test suite for testing database functionalities.
"""

from better_sqlite.config import Config  # Import the Config class for database connection configuration
from better_sqlite.basic_functions import BasicFunctions  # Import BasicFunctions for performing CRUD operations
from better_sqlite.db_suite import suite  # Import the test suite for validating database functionalities
