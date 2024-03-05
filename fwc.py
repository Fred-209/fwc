# wc clone

import sys


def count_bytes(byte_data):
    """
    Calculate the number of bytes in the given byte_data.

    Parameters:
        byte_data (bytes): The byte data to be counted
    Returns:
        int: The number of bytes in the byte data
    """

    return len(byte_data)


def count_lines(byte_data):
    """
    Count the number of lines in the given byte data after decoding it from utf-8.

    Parameters:
        byte_data (bytes): The byte data to be decoded and counted.

    Returns:
        int: The number of lines in the decoded byte data.
    """

    return len(byte_data.decode("utf-8").splitlines())


def count_words(byte_data):
    """
    Count the number of words in the given byte data after decoding it from utf-8.

    Parameters:
    byte_data (bytes): The byte data to be decoded and counted.

    Returns:
    int: The number of words in the decoded byte data.
    """

    return len(byte_data.decode("utf-8").split())


def count_chars(byte_data):
    """
    Count the number of characters in the given byte data after decoding it from utf-8.

    Parameters:
    byte_data (bytes): The byte data to be decoded and counted.

    Returns:
    int: The number of characters in the decoded byte data.
    """

    return len(byte_data.decode("utf-8"))


def count_lines_words_bytes(byte_data):
    """
    Count the number of lines, words, and bytes in the given byte data.

    Parameters:
        byte_data (bytes): The byte data to be counted.

    Returns:
        tuple: A 3-tuple containing the line count, word count, and byte count of the input byte data.
    """
    return (count_lines(byte_data), count_words(byte_data), count_bytes(byte_data))


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

    # Check to see if stdin was piped in from another program
    if not sys.stdin.isatty():
        file_path = "stdin"

        try:
            byte_data = sys.stdin.buffer.read()
            option_flag = cmd_args[0]
        except IndexError:
            option_flag = None

    # if stdin is not piped in from another source, need to open file
    # and read it in
    else:
        try:
            if arg_count == 0:
                display_manual()
                return
            elif arg_count == 1:
                if cmd_args[0] == "-h":
                    option_flag = "-h"
                    file_path = None
                else:
                    file_path = cmd_args[0]
                    option_flag = None
            elif arg_count == 2:
                option_flag = cmd_args[0]
                file_path = cmd_args[1]
            else:
                print("Too many arguments given. Read manual with -h option")
                display_manual()
                return

            if file_path:
                with open(file_path, "rb") as file:
                    byte_data = file.read()

        except FileNotFoundError:
            print(f"No file at path {file_path} is found.")
            return
    if not option_flag:
        line_count, word_count, byte_count = count_lines_words_bytes(byte_data)
        print(line_count, word_count, byte_count, file_path)
    else:
        match option_flag:
            case "-h":
                display_manual()
            case "-c":
                print(f"{count_bytes(byte_data)} {file_path}")
            case "-l":
                print(f"{count_lines(byte_data)} {file_path}")
            case "-w":
                print(f"{count_words(byte_data)} {file_path}")
            case "-m":
                print(f"{count_chars(byte_data)} {file_path}")
            case _:
                print("No valid option given")


main()
