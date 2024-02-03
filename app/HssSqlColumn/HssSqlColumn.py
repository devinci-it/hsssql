class HssSqlColumn:
    """
    A class representing a SQL column.

    Attributes:
        name (str): The name of the column.
        data_type (str): The data type of the column.
        constraints (list): List of constraints on the column.

    Class Attributes:
        VALID_DATA_TYPES (list): List of commonly used data types.
        DATA_TYPES_WITH_PARAMETERS (list): List of data types that can accept parameters.
        VALID_CONSTRAINTS (list): List of valid column constraints.

    Methods:
        set_column_name(name: str) -> None: Set the name of the column.
        set_data_type(data_type: str, parameter: str = None) -> None: Set the data type of the column.
        add_constraint(constraint: str) -> None: Add a constraint to the column.
        remove_constraint(constraint: str) -> None: Remove a constraint from the column.
        to_dict() -> dict: Convert the column object to a dictionary.
        from_dict(data: dict) -> 'HssSqlColumn': Create a column object from a dictionary.
        __repr__() -> str: Return a string representation of the object.
        __str__() -> str: Return a human-readable string representation of the object.
        is_valid_data_type(data_type: str) -> bool: Check if a data type is valid.

    """

    VALID_DATA_TYPES = [
        "BIT", "TINYINT", "BOOL", "BOOLEAN", "SMALLINT", "MEDIUMINT",
        "INT", "INTEGER", "BIGINT", "FLOAT", "DOUBLE", "DECIMAL",
        "CHAR", "VARCHAR", "BINARY", "VARBINARY",
        "TINYBLOB", "TINYTEXT", "BLOB", "TEXT", "MEDIUMBLOB",
        "MEDIUMTEXT", "LONGBLOB", "LONGTEXT", "ENUM", "SET",
        "DATE", "DATETIME", "TIMESTAMP", "TIME", "YEAR"
    ]

    DATA_TYPES_WITH_PARAMETERS = ["CHAR", "VARCHAR", "BINARY", "VARBINARY", "ENUM", "SET", "FLOAT", "DOUBLE", "DECIMAL"]

    VALID_CONSTRAINTS = ["PRIMARY KEY", "UNIQUE", "NOT NULL", "CHECK", "DEFAULT"]

    def __init__(self, name=None, data_type=None):
        """
        Initialize a new instance of HssSqlColumn.

        Args:
            name (str): The name of the column.
            data_type (str): The data type of the column.

        """
        if name is None:
            self.name = ''
        else:
            self.name = name

        if data_type is None:
            self.data_type = ''
        else:
            self.data_type = data_type

        self.constraints = []

    def set_column_name(self, name: str) -> None:
        """
        Set the name of the column.

        Args:
            name (str): The new name for the column.

        Returns:
            None

        """
        self.name = name

    def set_data_type(self, data_type: str, parameter: str = None) -> None:
        """
        Set the data type of the column.

        Args:
            data_type (str): The new data type for the column.
            parameter (str, optional): Optional parameter for data types that accept it.

        Returns:
            None

        """

        if parameter is not None:
            data_type_with_param = f"{data_type}({parameter})"
            if not self.is_valid_data_type(data_type_with_param):
                raise ValueError(f"Invalid data type with parameter: {data_type_with_param}")
            self.data_type = data_type_with_param
        else:
            if not self.is_valid_data_type(data_type):
                raise ValueError(f"Invalid data type: {data_type}")
            self.data_type = data_type

    def add_constraint(self, constraint: str) -> None:
        """
        Add a constraint to the column.

        Args:
            constraint (str): The constraint to add.

        Returns:
            None

        """
        if not self.is_valid_constraint(constraint):
            raise ValueError(f"Invalid constraint: {constraint}")
        self.constraints.append(constraint)

    def remove_constraint(self, constraint: str) -> None:
        """
        Remove a constraint from the column.

        Args:
            constraint (str): The constraint to remove.

        Returns:
            None

        """
        self.constraints = [c for c in self.constraints if c != constraint]

    @staticmethod
    def is_valid_data_type(data_type: str, parameter: str = None) -> bool:
        """
        Check if a data type is valid.

        Args:
            data_type (str): The data type to check.
            parameter (str, optional): Optional parameter for data types that accept it.

        Returns:
            bool: True if the data type is valid, False otherwise.

        """
        if parameter and data_type.upper() not in HssSqlColumn.DATA_TYPES_WITH_PARAMETERS:
            return False  # Parameter provided for a data type that does not accept it

        if parameter and not parameter.isdigit():
            return False  # Parameter must be a valid integer

        return data_type.upper() in HssSqlColumn.VALID_DATA_TYPES

    @staticmethod
    def is_valid_constraint(constraint: str) -> bool:
        """
        Check if a column constraint is valid.

        Args:
            constraint (str): The constraint to check.

        Returns:
            bool: True if the constraint is valid, False otherwise.

        """
        return constraint.upper() in HssSqlColumn.VALID_CONSTRAINTS

    def to_dict(self) -> dict:
        """
        Convert the column object to a dictionary.

        Returns:
            dict: The dictionary representation of the column.

        """
        return {
            "name": self.name,
            "data_type": self.data_type,
            "constraints": self.constraints
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'HssSqlColumn':
        """
        Create a column object from a dictionary.

        Args:
            data (dict): The dictionary containing column information.

        Returns:
            HssSqlColumn: The column object.

        """
        instance = cls(data["name"], data["data_type"])
        instance.constraints = data.get("constraints", [])
        return instance

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: The string representation.

        """
        return f"HssSqlColumn(name='{self.name}', data_type='{self.data_type}', constraints={self.constraints})"

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the object.

        Returns:
            str: The human-readable string representation.

        """
        constraints_str = ', '.join(self.constraints) if self.constraints else 'None'
        return f"Column: {self.name}, Data Type: {self.data_type}, Constraints: {constraints_str}"

