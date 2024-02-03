from app.HssSqlColumn.HssSqlColumn import HssSqlColumn
class HssSqlTable:
    """
    A class representing a SQL table.

    Attributes:
        name (str): The name of the table.
        columns (list): List of columns in the table.
        constraints (list): List of constraints on the table.

    Methods:
        set_table_name(name: str) -> None: Set the name of the table.
        add_column(column) -> None: Add a column to the table.
        remove_column(column_name: str) -> None: Remove a column from the table.
        add_constraint(constraint: str) -> None: Add a constraint to the table.
        remove_constraint(constraint: str) -> None: Remove a constraint from the table.
        generate_create_table() -> str: Generate SQL command for creating the table.
        to_dict() -> dict: Convert the table object to a dictionary.
        from_dict(data: dict) -> 'HssSqlTable': Create a table object from a dictionary.

    """
    def __init__(self, name):
        """
        Initialize a new instance of HssSqlTable.

        Args:
            name (str): The name of the table.

        """
        self.name = name
        self.columns = []
        self.constraints = []

    def set_table_name(self, name: str) -> None:
        """
        Set the name of the table.

        Args:
            name (str): The new name for the table.

        Returns:
            None

        """
        self.name = name

    def add_column(self, column) -> None:
        """
        Add a column to the table.

        Args:
            column: The column object to add.

        Returns:
            None

        """
        self.columns.append(column)

    def remove_column(self, column_name: str) -> None:
        """
        Remove a column from the table.

        Args:
            column_name (str): The name of the column to remove.

        Returns:
            None

        """
        self.columns = [col for col in self.columns if col.name != column_name]

    def add_constraint(self, constraint: str) -> None:
        """
        Add a constraint to the table.

        Args:
            constraint (str): The constraint to add.

        Returns:
            None

        """
        self.constraints.append(constraint)

    def remove_constraint(self, constraint: str) -> None:
        """
        Remove a constraint from the table.

        Args:
            constraint (str): The constraint to remove.

        Returns:
            None

        """
        self.constraints.remove(constraint)

    def generate_create_table(self) -> str:
        """
        Generate SQL command for creating the table.

        Returns:
            str: The SQL command.

        """
        create_command = f"CREATE TABLE {self.name} (\n"
        column_commands = [f"    {col.generate_column_definition}" for col in self.columns]
        constraint_commands = [f"    {constraint}" for constraint in self.constraints]
        create_command += ",\n".join(column_commands + constraint_commands)
        create_command += "\n);"
        return create_command

    def to_dict(self) -> dict:
        """
        Convert the table object to a dictionary.

        Returns:
            dict: The dictionary representation of the table.

        """
        return {
            "name": self.name,
            "columns": [col.to_dict() for col in self.columns],
            "constraints": self.constraints
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'HssSqlTable':
        """
        Create a table object from a dictionary.

        Args:
            data (dict): The dictionary containing table information.

        Returns:
            HssSqlTable: The table object.

        """
        instance = cls(data["name"])
        instance.columns = [HssSqlColumn.from_dict(col_data) for col_data in data.get("columns", [])]
        instance.constraints = data.get("constraints", [])
        return instance


