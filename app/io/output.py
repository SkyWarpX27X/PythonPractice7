def write_in_console(value):
    """ Prints value in console"""
    print(value)

def write_to_file(value, path:str, append:bool = False):
    """ Writes value in file

    Args:
         value: Value to write to file
         path: Full or relative path to file
         append: Append value to existing file or overwrite

    Raises:
        FileNotFoundError: If directory in path does not exist
    """
    with open(path, 'a' if append else 'w') as file:
        file.write(value)