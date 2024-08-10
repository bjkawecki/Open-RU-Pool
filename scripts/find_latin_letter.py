import string

latin_letters = string.ascii_letters

b2 = open("b2.txt", "r")
b2_lines = b2.read()
b2_list = b2_lines.split("\n")
b2_list = list(filter(None, b2_list))

for line in b2_list:
    chars = list(line)
    for c in chars:
        if c in latin_letters:
            print(c, line)
