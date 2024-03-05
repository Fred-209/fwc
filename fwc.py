# wc clone

import sys


def count_bytes(filename):
    """
    Returns the number of bytes in a file

    Parameters:
        filename (str): The name of the file to read from

    Returns:
        int: The number of bytes in the file
    """
    with open(filename, "rb") as file:
        file_bytes = file.read()
        byte_count = len(file_bytes)
        return byte_count


def count_lines(filename):
    """
    Returns the number of lines in a file

    Parameters:
        filename (str): The name of the file to read from

    Returns:
        int: The number of lines in the file
    """
    with open(filename, encoding="utf-8") as file:
        return len(file.readlines())


def count_words(filename):
    """
    Returns the number of words in a file

    Parameters:
        filename (str): The name of the file to read from

    Returns:
        int: The number of words in the file
    """
    with open(filename, encoding="utf-8") as file:
        return len(file.read().split())


def count_chars(filename):
    """
    Count the number of characters in the file specified by the filename parameter.

    Parameters:
    filename (str): The path to the file to be counted.

    Returns:
    int: The number of characters in the file.
    """

    with open(filename, "rb") as file:
        return len(file.read().decode())


def count_bytes_lines_words(filename):
    """
    Count the bytes, lines, and words in a file

    Parameters:
        filename (str): The text name of a file
    Returns:
        tuple: (cout of bytes, count of lines, count of words)
    """
    return (count_bytes(filename), count_lines(filename), count_words(filename))


def display_manual():
    """
    Displays the usage and options of a command line tool to output byte count, line count, word count,
    and character count of a file.
    """
    print(
        """
    **********fwc**********
    A command line tool to output byte count, line count, word count, and character count
    of a file
    
    Usage: fwc [OPTION][FILENAME]
    
    If no OPTION is given then byte count, line count, and word count will be output for a
    given filename
    
    Options:
        -h : Displays help/usage instructions
        -c : Outputs the number of bytes in a given filename
        -l : Outputs the number of lines in a given filename
        -w : Outputs the number of words in a given filename
        -m : Outputs the number of characters in a given filename
        
    """
    )


def main():
    cmd_args = sys.argv[1:]
    arg_count = len(cmd_args)

    if arg_count == 0:
        display_manual()
        return
    elif arg_count == 1:
        if cmd_args[0] == "-h":
            display_manual()
            return

        filename = cmd_args[0]
        byte_count, line_count, word_count = count_bytes_lines_words(filename)
        print(
            f"{line_count} lines, {byte_count} bytes, and {word_count} words in {filename}"
        )
    else:
        try:
            option_flag = cmd_args[0]
            filename = cmd_args[1]

            match option_flag:
                case "-h":
                    display_manual()
                case "-c":
                    print(f"{count_bytes(filename)} {filename}")
                case "-l":
                    print(f"{count_lines(filename)} {filename}")
                case "-w":
                    print(f"{count_words(filename)} {filename}")
                case "-m":
                    print(f"{count_chars(filename)} {filename}")
                case _:
                    print("No valid option given")
        except FileNotFoundError:
            print("That file doesn't exist")


main()
