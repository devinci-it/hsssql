"""
A script demonstrating the usage of the HssSqlColumn class.

This script creates an instance of HssSqlColumn, sets attributes, adds constraints,
displays attributes using PrettyTable, converts the instance to a dictionary, and
creates a new instance from the dictionary.

Make sure to have the HssSqlColumn class implemented and imported before running this script.

Author: devinci-it
"""

from prettytable import PrettyTable
from HssSqlColumn import HssSqlColumn
import json


def display_message_table(message):
    """
    Display a single message using PrettyTable.

    Args:
        message (str): The message to be displayed.
    """
    table = PrettyTable(min_table_width=100)
    table.field_names = ["Message"]
    table.add_row([message])
    print(table)


def display_attributes_cli(column_instance):
    """
    Display the attributes of the HssSqlColumn instance in a visually appealing CLI output.

    Args:
        column_instance (HssSqlColumn): An instance of the HssSqlColumn class.
    """
    table = PrettyTable(min_table_width=100)
    table.field_names = ["Attribute", "Value"]

    table.add_row(["Column Name", column_instance.name])
    table.add_row(["Data Type", column_instance.data_type])
    table.add_row(["Constraints", ", ".join(column_instance.constraints)])

    print(table)


def main():
    """
    Main function demonstrating the usage of the HssSqlColumn class.

    Creates an instance of HssSqlColumn, sets attributes, adds constraints,
    displays attributes using PrettyTable, converts the instance to a dictionary, and
    creates a new instance from the dictionary.
    """
    display_message_table("Creating instance of `HssSqlColumn` Object")

    column_instance = HssSqlColumn()
    column_instance.set_column_name("column_name")
    column_instance.set_data_type("TIME",255)
    column_instance.add_constraint("NOT NULL")
    column_instance.add_constraint("UNIQUE")

    # Display attributes using PrettyTable
    display_message_table("HssSqlColumn object instantiated successfully")
    display_attributes_cli(column_instance)

    display_message_table("Testing instance methods for HssSqlColumn object")
    # Remove a constraint
    column_instance.remove_constraint("UNIQUE")

    # Display attributes after removing a constraint
    display_message_table("Constraint removed successfully")
    display_attributes_cli(column_instance)

    display_message_table("Testing class methods for serializing and deserializing `HssSqlColumn` object")
    # Convert the column instance to a dictionary
    try:
        display_message_table("Serializing data...")
        column_dict = column_instance.to_dict()
        display_message_table("Serialized data:")
        print(json.dumps(column_dict, indent=4))
    except Exception as e:
        display_message_table(f"ERROR in data serialization: {str(e)}")

    # Create a new instance from the dictionary
    try:
        display_message_table("Deserializing data...")
        new_column_instance = HssSqlColumn.from_dict(column_dict)
        display_message_table("Deserialized HssSqlColumn instance:")
        display_attributes_cli(new_column_instance)
    except Exception as e:
        display_message_table(f"ERROR in data deserialization: {str(e)}")


if __name__ == "__main__":
    main()
