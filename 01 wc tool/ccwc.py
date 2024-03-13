""" 
Created on : 13/03/24 11:09am
@author : ds  
"""
import sys

def file_exists(filename):
    try:
        with open(filename, 'r'):
            pass
        return True
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False

def count_bytes(filename):
    with open(filename, 'rb') as file:
        byte_count = len(file.read())
        return byte_count


def count_lines(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)
        return line_count

def count_words(filename):
    with open(filename, 'r') as file:
        word_count = 0
        for line in file:
            words = line.split()
            word_count += len(words)
        return word_count

def count_characters(filename):
    with open(filename, 'r') as file:
        character_count = 0
        for line in file:
            character_count += len(line)
        return character_count


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ['-c', '-l', '-w', '-m']:
        print(f"Usage: python {sys.argv[0]} [-c/-l/-w/-m] filename")
        return

    option = sys.argv[1]
    filename = sys.argv[2]

    if not file_exists(filename):
        return

    if option == "-c":
        byte_count = count_bytes(filename)
        if byte_count is not None:
            print(f"{byte_count} {filename}")
    elif option == '-l':
        line_count = count_lines(filename)
        if line_count is not None:
            print(f"{line_count} {filename}")
    elif option == '-w':
        word_count = count_words(filename)
        if word_count is not None:
            print(f"{word_count} {filename}")
    elif option == '-m':
        character_count = count_characters(filename)
        if character_count is not None:
            print(f"{character_count} {filename}")


if __name__ == "__main__":
    main()