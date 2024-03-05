# wc clone

# First step, takes a command line option -c and a filename as an argument, then
# outputs the number of bytes in a file

import sys


def count_bytes(filename):
    """Returns the number of bytes in a file"""
    with open(filename, "rb") as file:
        file_bytes = file.read()
        byte_count = len(file_bytes)
        return byte_count


def count_lines(filename):
    """Returns the number of lines in a file"""
    with open(filename) as file:
        return len(file.readlines())


def display_manual():
    print(
        """
    **********fwc**********
    A command line tool to output byte count, line count, word count, and character count
    of a file
    
    Usage: fwc [OPTION][FILENAME]
    
    If no OPTION is given then byte count, line count, and word count will be output for a
    given filename
    
    Options:
        -c : Outputs the number of bytes in a given filename
        -l : Outputs the number of lines in a given filename
        -w : Outputs the number of words in a given filename
        -m : Outputs the number of characters in a given filename
        
    """
    )


def main():
    cmd_args = sys.argv[1:]
    arg_count = len(cmd_args)

    if arg_count < 2:
        display_manual()
        return
    try:
        option_flag = cmd_args[0]
        filename = cmd_args[1]
        match option_flag:
            case "-c":
                print(f"{count_bytes(filename)} {filename}")
            case "-l":
                print(f"{count_lines(filename)} {filename}")
            case _:
                print("No valid option given")
    except FileNotFoundError:
        print("That file doesn't exist")


main()
