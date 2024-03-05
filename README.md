# fwc - Word Counter

`fwc` is a Python-based clone of the Linux `wc` tool.
It's is a command-line tool designed to output the byte count, line count, word count, and character count of a file.
Wrapped in a bash script for easy usage

## Features

- Count bytes, lines, words, and characters in a file.
- Support for reading from both files and standard input.
- Simple command-line interface.

## Installation

To use `fwc`, clone this repository to your local machine:

```
git clone https://github.com/Fred-209/fwc.git
cd fwc
```

Ensure that you have Python installed on your system. This script has been tested with Python 3.8 and above.

## Usage

You can use `fwc` by specifying the filename as an argument or piping data into it. Here are some usage examples:

- Display the byte count, line count, and word count of a file:

```
  ./fwc filename.txt
```

- Display the number of bytes in a file:

```
  ./fwc -c filename.txt
```

- Display the number of lines in a file:

```
  ./fwc -l filename.txt
```

- Display the number of words in a file:

```
  ./fwc -w filename.txt
```

- Display the number of characters in a file:

```
  ./fwc -m filename.txt
```

- Display help/usage instructions:

```
  ./fwc -h
```

- Use `fwc` with standard input:

```
  cat filename.txt | ./fwc
```

## License

`fwc` is released under the MIT License. See the LICENSE file for more details.
