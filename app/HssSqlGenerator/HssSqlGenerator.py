import os

import click
from rich.console import Console


class HssSqlGenerator:
    """
    A class to interactively generate MySQL schema scripts.

    Attributes:
        CONSOLE_MIN_WIDTH (int): The minimum width of the console.
        SCRIPT_DIRECTORY (str): The directory containing the script.
        DEFAULT_PATH (str): The default path for session file.
        TABLES (dict): A dictionary to store tables.
        CHANGES (dict): A dictionary to store changes.
        BANNER (str): The banner read from the file.
        MENU_OPTIONS (dict): Placeholder for menu options.
        _SESSION_FILE_PATH (str): The path for the session file.
        CURRENT_SESSION: Placeholder for the current session.
        CONSOLE (Console): The console object.

    Methods:
        read_banner(cls): Read the banner from the file.
        __init__(session_file_path): Initialize the HssSqlGenerator object.
        clear_screen(): Clear the console screen.
        get_banner(): Get the banner with the script directory.
        display_banner(): Display the banner using rich console.
        set_session_file_path(path): Set the session file path.
        get_session_file_path(): Get the session file path.
    """

    CONSOLE_MIN_WIDTH = 100
    SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    DEFAULT_PATH = os.path.join(SCRIPT_DIRECTORY, "..", "..", "Generated_Scripts")
    MENU_OPTIONS = {
        1: 'Start',
        # Add more menu options as needed
        'Q': 'Quit'
    }

    @classmethod
    def read_banner(cls):
        """
        Read the banner from the file.

        Returns:
            str: The content of the banner file.
        Raises:
            FileNotFoundError: If the banner file is not found.
        """
        try:
            with open("assets/banner.txt", "r") as banner_file:
                banner = banner_file.read()
            return banner
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error reading banner file: {e}")

    def __init__(self, session_file_path=None):
        """
        Initialize the HssSqlGenerator object.

        Args:
            session_file_path (str): The path for the session file. Defaults to None.

        Raises:
            OSError: If an error occurs while creating the default directory.
        """
        self.TABLES = {}
        self.CHANGES = {}
        self.BANNER = self.get_banner()

        if session_file_path is None:
            try:
                os.makedirs(self.DEFAULT_PATH, exist_ok=True)
                self._SESSION_FILE_PATH = self.DEFAULT_PATH
            except OSError as e:
                raise OSError(f"Error creating directory: {e}")
        else:
            if not os.path.exists(session_file_path):
                print(f"Specified path {session_file_path} not found. Creating in default path.")
                self._SESSION_FILE_PATH = os.path.join(self.DEFAULT_PATH, session_file_path)
            else:
                self._SESSION_FILE_PATH = session_file_path

        self.CURRENT_SESSION = None
        self.CONSOLE = Console(width=self.CONSOLE_MIN_WIDTH)

    @staticmethod
    def clear_screen():
        """Clear the console screen."""
        click.clear()

    def get_banner(self):
        """
        Get the banner with the script directory.

        Returns:
            str: The banner with the script directory.
        """
        return self.read_banner().format(path_to_script=self.SCRIPT_DIRECTORY)

    def display_banner(self):
        """Display the banner using rich console."""
        print_to_console = self.get_banner()
        self.CONSOLE.print(print_to_console)

    def set_session_file_path(self, path):
        """
        Set the session file path.

        Args:
            path (str): The new session file path.
        """
        self._SESSION_FILE_PATH = path

    def get_session_file_path(self):
        """
        Get the session file path.

        Returns:
            str: The session file path.
        """
        return self._SESSION_FILE_PATH

    # Placeholder for additional methods related to menu and script generation

# Example usage:
# generator = HssSqlGenerator()
# generator.set_session_file_path("/new/path")
# print(generator.get_session_file_path())
# generator.display_banner()
# generator.clear_screen()
