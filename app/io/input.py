import pandas as pd

def read_from_console() -> str:
    """ Reads and returns string from console """
    return input()

def read_file(path:str) -> str:
    """ Reads and returns string from file

    Args:
        path: Full or relative path to file

    Returns:
        Content of file in string

    Raises:
        FileNotFoundError: If file does not exist
    """
    with open(path, 'r') as file:
        return file.read()

def read_file_with_pandas(path:str, separator=',') -> str:
    """ Reads table structured file

    Args:
        path: Full or relative path to file
        separator: Separator between values, by default in csv format

    Returns:
        DataFrame of file converted to string

    Raises:
        FileNotFoundError: If file does not exist
        pandas.errors.ParserError: If file is not in table format
    """
    return pd.read_csv(path,header=None, sep=separator).to_string()