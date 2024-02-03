"""
A script demonstrating the usage of the HssSqlDatabase class.

This script creates an instance of HssSqlDatabase, sets attributes, generates SQL commands,
displays attributes using PrettyTable, converts the instance to a dictionary, and
creates a new instance from the dictionary.

Make sure to have the HssSqlDatabase class implemented and imported before running this script.

Author: devinci-it
"""

from prettytable import PrettyTable
from HssSqlDatabase import HssSqlDatabase
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


def display_attributes_cli(database_instance):
    """
    Display the attributes of the HssSqlDatabase instance in a visually appealing CLI output.

    Args:
        database_instance (HssSqlDatabase): An instance of the HssSqlDatabase class.
    """
    table = PrettyTable(min_table_width=100)
    table.field_names = ["Attribute", "Value"]

    table.add_row(["Database Name", database_instance.database_name])
    table.add_row(["Schema", database_instance.schema])
    table.add_row(["Charset", database_instance.charset])
    table.add_row(["Collation", database_instance.collation])
    table.add_row(["Tables", ", ".join(database_instance.tables)])
    table.add_row(["Options", str(database_instance.options)])

    print(table)


def main():
    """
    Main function demonstrating the usage of the HssSqlDatabase class.

    Creates an instance of HssSqlDatabase, sets attributes, generates SQL commands,
    displays attributes using PrettyTable, converts the instance to a dictionary, and
    creates a new instance from the dictionary.
    """
    display_message_table("Creating instance of `HssSqlDatabase` Object")

    database_instance = HssSqlDatabase("my_database")
    database_instance.set_schema("custom_schema")
    database_instance.set_charset("utf8mb4")
    database_instance.set_collation("utf8mb4_unicode_ci")
    database_instance.add_table("table1")
    database_instance.add_table("table2")

    # Display attributes using PrettyTable
    display_message_table("HssSqlDatabase object instantiated successfully")
    display_attributes_cli(database_instance)

    display_message_table("Testing instance methods for HssSqlDatabase object")
    # Generate SQL commands
    create_command = database_instance.generate_create_database()
    alter_command = database_instance.generate_alter_database()
    drop_command = database_instance.generate_drop_database()
    show_tables_command = database_instance.generate_show_tables()
    show_info_command = database_instance.generate_show_database_info()

    display_message_table("SCRIPT GENERATED SUCCESSFULLY")
    # Display the generated script using PrettyTable
    script_table = PrettyTable(min_table_width=100,align='l')
    script_table.field_names = ["Generated Script"]

    generated_script = database_instance.script
    formatted_script = "\n".join(line.strip() + ';' for line in generated_script.split(';'))

    for line in formatted_script.split(';'):
        script_table.add_row([line.strip() + ';'])
    print(script_table)

    display_message_table("Testing class methods for serializing and deserializing `HssSqlDatabase` object")
    # Convert the database instance to a dictionary
    try:
        display_message_table("Serializing data...")
        database_dict = database_instance.to_dict()
        display_message_table("Serialized data:")
        print(json.dumps(database_dict,indent=4))
    except Exception as e:
        display_message_table(f"ERROR in data serialization: {str(e)}")

    # Create a new instance from the dictionary
    try:
        display_message_table("Deserializing data...")
        new_instance = HssSqlDatabase.from_dict(database_dict)
        display_message_table("Deserialized HssSqlDatabase instance:")
        display_attributes_cli(new_instance)
    except Exception as e:
        display_message_table(f"ERROR in data deserialization: {str(e)}")


if __name__ == "__main__":
    main()
