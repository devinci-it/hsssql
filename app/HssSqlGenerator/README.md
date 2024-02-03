# HssSqlGenerator

The `HssSqlGenerator` is a Python class designed for interactively generating MySQL schema scripts. It provides
functionality for creating, modifying, and interacting with database tables through an interactive command-line
interface.

## Installation

You can install the `HssSqlGenerator` package using pip:

```bash
pip install HssSqlGenerator
```

## Usage

```python

from HssSqlGenerator import HssSqlGenerator

# Create an instance of HssSqlGenerator
generator = HssSqlGenerator()

# Set a custom session file path
generator.set_session_file_path("/new/path")

# Get the current session file path
print(generator.get_session_file_path())

# Display the banner
generator.display_banner()

# Clear the console screen
generator.clear_screen()
```

## Features

- **Interactive Menu**: The class includes a simple interactive menu to guide users through various functionalities.

- **Banner Display**: A banner is displayed to provide information about the script and the script directory.

- **Session File Path Management**: Easily set and retrieve the session file path.

- **Console Screen Clearing**: Clear the console screen for a cleaner user interface.


