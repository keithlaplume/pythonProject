from pprint import pprint
from random import randrange


def blank_it(strings_to_blank, blank_char, code_file):
    with open(code_file, 'r', encoding="utf-8") as file:
        filedata = file.read()

    for string in strings_to_blank:
        length = len(string)
        blank_string = blank_char * length
        print("replacing {} with {}".format(string, blank_string))
        filedata = filedata.replace(string, blank_string)

    with open(code_file, 'w', encoding="utf-8") as file:
        file.write(filedata)


def blank_random_lines(spacing, length, random, blank_char, code_file):
    with open(code_file, 'r', encoding="utf-8") as file:
        lines = file.readlines()
    startpoint = 50
    endpoint = startpoint + length
    for count, line in enumerate(lines):
        if startpoint <= count <= endpoint:
            # replace
            line_length = len(line)
            blank_string = (blank_char * line_length) + '\n'
            lines[count] = blank_string
        if count > endpoint:
            startpoint = endpoint + (randrange(spacing - random, spacing + random))
            endpoint = startpoint + (randrange(length - random, length + random))
    pprint(lines)
    with open(code_file, 'w', encoding="utf-8") as file:
        file.writelines(lines)
