class HssSqlDatabase:
    """
    A class representing a SQL database and providing methods for database operations.

    Attributes:
        database_name (str): The name of the database.
        tables (list): List of tables in the database.
        schema (str): The database schema.
        charset (str): The character set for the database.
        collation (str): The collation for the database.
        options (dict): Additional options for the database.
        script (str): The accumulated SQL script.

    Methods:
        set_database_name(name: str) -> None: Set the name of the database.
        set_schema(schema: str) -> None: Set the schema for the database.
        set_charset(charset: str) -> None: Set the character set for the database.
        set_collation(collation: str) -> None: Set the collation for the database.
        add_table(table) -> None: Add a table to the database.
        remove_table(table_name: str) -> None: Remove a table from the database.
        generate_create_database() -> str: Generate SQL command for creating the database.
        generate_alter_database() -> str: Generate SQL command for altering the database.
        generate_drop_database() -> str: Generate SQL command for dropping the database.
        generate_show_tables() -> str: Generate SQL command for showing tables in the database.
        generate_show_database_info() -> str: Generate SQL command for showing database information.
        to_dict() -> dict: Convert the database object to a dictionary.
        from_dict(data: dict) -> 'HssSqlDatabase': Create a database object from a dictionary.

    """

    def __init__(self, database_name):
        """
        Initialize a new instance of HssSqlDatabase.

        Args:
            database_name (str): The name of the database.

        """
        self.database_name = database_name
        self.tables = []
        self.schema = "public"
        self.charset = "utf8"
        self.collation = "utf8_general_ci"
        self.options = {}
        self.script = ""

    def set_database_name(self, name: str) -> None:
        """
        Set the name of the database.

        Args:
            name (str): The new name for the database.

        Returns:
            None

        """
        self.database_name = name

    def set_schema(self, schema: str) -> None:
        """
        Set the schema for the database.

        Args:
            schema (str): The new schema for the database.

        Returns:
            None

        """
        self.schema = schema

    def set_charset(self, charset: str) -> None:
        """
        Set the character set for the database.

        Args:
            charset (str): The new character set for the database.

        Returns:
            None

        """
        self.charset = charset

    def set_collation(self, collation: str) -> None:
        """
        Set the collation for the database.

        Args:
            collation (str): The new collation for the database.

        Returns:
            None

        """
        self.collation = collation

    def add_table(self, table) -> None:
        """
        Add a table to the database.

        Args:
            table: The table object to add.

        Returns:
            None

        """
        self.tables.append(table)

    def remove_table(self, table_name: str) -> None:
        """
        Remove a table from the database.

        Args:
            table_name (str): The name of the table to remove.

        Returns:
            None

        """
        self.tables = [table for table in self.tables if table.name != table_name]

    def generate_create_database(self) -> str:
        """
        Generate SQL command for creating the database.

        Returns:
            str: The SQL command.

        """
        create_command = f"CREATE DATABASE {self.database_name} "
        create_command += f"CHARACTER SET {self.charset} "
        create_command += f"COLLATE {self.collation};"
        self.script += create_command
        return create_command

    def generate_alter_database(self) -> str:
        """
        Generate SQL command for altering the database.

        Returns:
            str: The SQL command.

        """
        alter_command = f"ALTER DATABASE {self.database_name} "
        alter_command += f"CHARACTER SET {self.charset} "
        alter_command += f"COLLATE {self.collation};"
        self.script += alter_command
        return alter_command

    def generate_drop_database(self) -> str:
        """
        Generate SQL command for dropping the database.

        Returns:
            str: The SQL command.

        """
        drop_command = f"DROP DATABASE IF EXISTS {self.database_name};"
        self.script += drop_command
        return drop_command

    def generate_show_tables(self) -> str:
        """
        Generate SQL command for showing tables in the database.

        Returns:
            str: The SQL command.

        """
        show_tables_command = f"SHOW TABLES;"
        self.script += show_tables_command
        return show_tables_command

    def generate_show_database_info(self) -> str:
        """
        Generate SQL command for showing database information.

        Returns:
            str: The SQL command.

        """
        show_info_command = f"SHOW DATABASE {self.database_name};"
        self.script += show_info_command
        return show_info_command

    def to_dict(self) -> dict:
        """
        Convert the database object to a dictionary.

        Returns:
            dict: The dictionary representation of the database.

        """
        return {
            "database_name": self.database_name,
            "tables": self.tables,
            "schema": self.schema,
            "charset": self.charset,
            "collation": self.collation,
            "options": self.options
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'HssSqlDatabase':
        """
        Create a database object from a dictionary.

        Args:
            data (dict): The dictionary containing database information.

        Returns:
            HssSqlDatabase: The database object.

        """

        instance = cls(data["database_name"])
        instance.tables = data.get("tables", [])
        instance.schema = data.get("schema", "public")
        instance.charset = data.get("charset", "utf8")
        instance.collation = data.get("collation", "utf8_general_ci")
        instance.options = data.get("options", {})

        return instance
