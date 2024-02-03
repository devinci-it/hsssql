# HssSqlDatabase Subpackage

## Overview

The `HssSqlDatabase` class is a component of the `hsssql` package, designed to facilitate the interactive generation of MySQL schema scripts. This class represents a SQL database and provides methods for various database operations.

## Class Structure

### Attributes

- `database_name` (str): The name of the database.
- `tables` (list): List of tables in the database.
- `schema` (str): The database schema.
- `charset` (str): The character set for the database.
- `collation` (str): The collation for the database.
- `options` (dict): Additional options for the database.
- `script` (str): The accumulated SQL script.

### Methods

- `set_database_name(name: str) -> None`: Set the name of the database.
- `set_schema(schema: str) -> None`: Set the schema for the database.
- `set_charset(charset: str) -> None`: Set the character set for the database.
- `set_collation(collation: str) -> None`: Set the collation for the database.
- `add_table(table) -> None`: Add a table to the database.
- `remove_table(table_name: str) -> None`: Remove a table from the database.
- `generate_create_database() -> str`: Generate SQL command for creating the database.
- `generate_alter_database() -> str`: Generate SQL command for altering the database.
- `generate_drop_database() -> str`: Generate SQL command for dropping the database.
- `generate_show_tables() -> str`: Generate SQL command for showing tables in the database.
- `generate_show_database_info() -> str`: Generate SQL command for showing database information.
- `to_dict() -> dict`: Convert the database object to a dictionary.
- `from_dict(data: dict) -> 'HssSqlDatabase'`: Create a database object from a dictionary.

## Usage Example

For a comprehensive usage example, please refer to the [DemoScript.py](./DemoScript.py) file.
The demo script demonstrates the creation of a `HssSqlDatabase` instance, manipulation of its attributes, generation of SQL commands, and conversion to/from a dictionary. Adjust the use case based on your specific requirements and data model.

```python
from hsssql.HssSqlDatabase import HssSqlDatabase

# Create an instance of HssSqlDatabase
database_instance = HssSqlDatabase("my_database")

# Set attributes using setter methods
database_instance.set_schema("custom_schema")
database_instance.set_charset("utf8mb4")
database_instance.set_collation("utf8mb4_unicode_ci")

# Add tables to the database
database_instance.add_table("table1")
database_instance.add_table("table2")

# Generate SQL commands
create_command = database_instance.generate_create_database()
alter_command = database_instance.generate_alter_database()
drop_command = database_instance.generate_drop_database()
show_tables_command = database_instance.generate_show_tables()
show_info_command = database_instance.generate_show_database_info()

# Display the generated script
print(f"Generated Script:\n{database_instance.script}")

# Convert the database instance to a dictionary
database_dict = database_instance.to_dict()

# Create a new instance from the dictionary
new_database_instance = HssSqlDatabase.from_dict(database_dict)

# Display the attributes of the new instance
print("\nAttributes of the new instance:")
print(f"Database Name: {new_database_instance.database_name}")
print(f"Schema: {new_database_instance.schema}")
print(f"Charset: {new_database_instance.charset}")
print(f"Collation: {new_database_instance.collation}")
print(f"Tables: {new_database_instance.tables}")
print(f"Options: {new_database_instance.options}")
```

