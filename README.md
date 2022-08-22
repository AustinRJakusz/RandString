# RandString
A random string generator

# Installation
1. Ensure you have Poetry installed by following this guide [Poetry Installation Guide](https://python-poetry.org/docs/#installation 'Poetry Installation Guide').
2. Download the code and extract to the directory of your choice.
3. Run `poetry install --no-dev` in the directory to install the venv with no dev dependencies
4. Run `poetry run python main.py -h` which should show you the help text.

# Usage
To use the random string generator, run `poetry run python main.py`. If you would like to customize it's behavior, you
can see available options by running `poetry run python main.py -h`.

# TODO
- Implement the ability to copy to clipboard from command line tool (secretly).
- Add multiprocessing for anything over 1000 generated strings
- Add CSV output support (custom delimiter)
- Ensure included characters and excluded chars are ascii/UTF-8