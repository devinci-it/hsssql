"""
Demo script for HssSqlTable and HssSqlColumn classes.

Instantiate an HssSqlTable, create columns using HssSqlColumn objects, add columns to the table,
add constraints to the table, generate SQL commands, display SQL commands, remove a column from the table,
and display the updated SQL command.

Make sure to have the HssSqlTable and HssSqlColumn classes implemented and imported
before running this script.

Author: devinci-it
"""

from app.HssSqlColumn.HssSqlColumn import HssSqlColumn
from app.HssSqlTable.HssSqlTable import HssSqlTable


def display_sql_command(title, command):
    """
    Display a SQL command using PrettyTable.

    Args:
        title (str): The title for the section.
        command (str): The SQL command to be displayed.
    """
    print(f"\n{title}:\n{command}\n{'=' * (len(title) + 2)}\n")


# Instantiate an HssSqlTable
sample_table = HssSqlTable(name="employees")

# Create columns using HssSqlColumn objects
column1 = HssSqlColumn(name="id", data_type="INT", constraints=["PRIMARY KEY", "AUTO_INCREMENT"])
column2 = HssSqlColumn(name="name", data_type="VARCHAR(255)", constraints=["NOT NULL"])
column3 = HssSqlColumn(name="age", data_type="INT")
column4 = HssSqlColumn(name="salary", data_type="DECIMAL(10,2)")

# Add columns to the table
sample_table.add_column(column1)
sample_table.add_column(column2)
sample_table.add_column(column3)
sample_table.add_column(column4)

# Add a constraint to the table
sample_table.add_constraint("UNIQUE (name)")

# Generate the SQL command for creating the table
create_table_command = sample_table.generate_create_table()

# Display the SQL command
display_sql_command("Create Table Command", create_table_command)

# Remove a column from the table
sample_table.remove_column("age")

# Generate the updated SQL command for creating the table
updated_create_table_command = sample_table.generate_create_table()

# Display the updated SQL command
display_sql_command("Updated Create Table Command", updated_create_table_command)
