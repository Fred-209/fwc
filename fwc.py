# wc clone

# First step, takes a command line option -c and a filename as an argument, then
# outputs the number of bytes in a file

import sys


def count_bytes(filename):
    with open(filename, "rb") as file:
        file_bytes = file.read()
        byte_count = len(file_bytes)
        print(byte_count)


def display_manual():
    print(
        """
    **********fwc**********
    A command line tool to get the byte count of a file
    """
    )


def main():
    cmd_args = sys.argv[1:]
    arg_count = len(cmd_args)

    if arg_count < 2:
        display_manual()
        return

    option_flag = cmd_args[0]
    filename = cmd_args[1]

    if option_flag == "-c":
        count_bytes(filename)
    else:
        print("No valid option given")


main()
