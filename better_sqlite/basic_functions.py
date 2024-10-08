from better_sqlite.config import Config
from typing import List, Tuple, Optional, Any


class BasicFunctions:
    def __init__(self, config: Config):
        """
        Initialize the BasicFunctions class with a database configuration.

        Args:
            config (Config): An instance of Config containing the database connection and cursor.
        """
        self.config = config

    def __repr__(self):
        return f"BasicFunctions(\n    config={self.config}\n)"

    def new_table(self, name: str, columns: List[Tuple[str, str]]):
        """
        Create a new table in the database.

        Args:
            name (str): The name of the table to be created.
            columns (List[Tuple[str, str]]): A list of tuples, where each tuple contains the column name
                                               and the column type (e.g., [("id", "INTEGER"), ("name", "TEXT")]).
        """
        # Dynamically construct the SQL query for table creation
        columns_query = ", ".join([f"{col_name} {col_type}" for col_name, col_type in columns])
        query = f"CREATE TABLE IF NOT EXISTS {name} ({columns_query})"
        # Execute the query to create the table
        self.config.cursor.execute(query)
        self.config.connection.commit()  # Commit the changes to the database

    def clear_table(self, name: str):
        """
        Clear all rows from the specified table.

        Args:
            name (str): The name of the table to be cleared.
        """
        # Construct the SQL query to delete all rows from the specified table
        query = f"DELETE FROM {name}"
        # Execute the query to clear the table
        self.config.cursor.execute(query)
        self.config.connection.commit()  # Commit the changes to the database

    def return_contents(self, name: str) -> List[Tuple]:
        """
        Retrieve all rows from the specified table.

        Args:
            name (str): The name of the table to retrieve rows from.

        Returns:
            List[Tuple]: A list of tuples representing the rows in the table.
        """
        # Construct the SQL query to retrieve all rows from the specified table
        query = f"SELECT * FROM {name}"
        self.config.cursor.execute(query)  # Execute the query
        # Fetch all rows and return them as a list of tuples
        return self.config.cursor.fetchall()

    def add_row(self, table_name: str, values: List):
        """
        Add a new row to the specified table.

        Args:
            table_name (str): The name of the table to add a row to.
            values (List): A list of values to be inserted into the new row.
        """
        # Construct the SQL query for inserting a new row
        placeholders = ", ".join(["?"] * len(values))  # Create placeholders for values
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        # Execute the query to insert the new row
        self.config.cursor.execute(query, values)
        self.config.connection.commit()  # Commit the changes to the database

    def delete_row(self, table_name: str, identifier_column: str = None, identifier_value: Optional[str] = None,
                   index: Optional[int] = None):
        """
        Delete a row from the specified table based on a condition or index.

        Args:
            table_name (str): The name of the table to delete a row from.
            identifier_column (str, optional): The name of the column used to identify the row for deletion.
            identifier_value (Optional[str], optional): The value of the identifier column for the row to delete.
            index (Optional[int], optional): The index of the row to delete (if identifier_column is not provided).

        Raises:
            IndexError: If the provided index is out of range.
            ValueError: If neither identifier_column and identifier_value nor index is provided.
        """
        # Check if an index is provided to find the identifier
        if index is not None:
            contents = self.return_contents(table_name)  # Retrieve current table contents
            if 0 <= index < len(contents):
                # Assuming the first column is the unique identifier
                identifier_value = contents[index][0]
            else:
                raise IndexError("Index out of range.")  # Raise error if index is out of range

        if identifier_column and identifier_value is not None:
            # Construct the SQL query to delete a row based on a specific condition
            query = f"DELETE FROM {table_name} WHERE {identifier_column} = ?"
            self.config.cursor.execute(query, (identifier_value,))  # Execute the query
            self.config.connection.commit()  # Commit the changes to the database
        else:
            raise ValueError("Either identifier_column and identifier_value or index must be provided.")

    def update_column(self, table_name: str, column_name: str, new_value: Any, where_column: Optional[str] = None,
                      where_value: Optional[Any] = None):
        """
        Update a column in the specified table.

        Args:
            table_name (str): The name of the table to update.
            column_name (str): The name of the column to be updated.
            new_value (Any): The new value to set in the specified column.
            where_column (Optional[str], optional): The name of the column used to identify which rows to update.
            where_value (Optional[Any], optional): The value of the identifier column for the rows to update.
        """
        if where_column and where_value is not None:
            # Update the specified column where the condition matches
            query = f"UPDATE {table_name} SET {column_name} = ? WHERE {where_column} = ?"
            self.config.cursor.execute(query, (new_value, where_value))  # Execute the query
        else:
            # Update the specified column for all rows if no condition is provided
            query = f"UPDATE {table_name} SET {column_name} = ?"
            self.config.cursor.execute(query, (new_value,))  # Execute the query

        self.config.connection.commit()  # Commit the changes to the database
