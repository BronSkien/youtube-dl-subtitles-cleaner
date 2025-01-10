import sys

def get_input_file_name(default="input.txt"):
    """Retrieve the input file name from the command line arguments or use the default."""
    return sys.argv[1] if len(sys.argv) > 1 else default

def get_output_file_name(default="output.txt"):
    """Retrieve the output file name from the command line arguments or use the default."""
    return sys.argv[2] if len(sys.argv) > 2 else default

def read_file(file_name):
    """Read the content of a file and return it as a list of lines."""
    with open(file_name, "r", encoding="utf-8") as file:
        return file.readlines()

def write_to_file(lines, file_name):
    """Write a list of lines to a file."""
    with open(file_name, "w", encoding="utf-8") as file:
        file.writelines(lines)
