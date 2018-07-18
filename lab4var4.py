import additional


def change_str(beginfile: str, file: str):
    begin = open(beginfile, 'rt')
    finish = open(file, 'wt')
    count = 0
    while True:
        line = begin.readline()
        if not line:
            break
        line = line.strip('\n')
        if line.endswith(('s', 'w', 'r', 't', 'q', 'd', 'z', 'x', 'c', 'v', 'f', 't', 'h', 'g', 'j', 'k', 'l', 'm', 'n', 'b', 'y')):
            line += line[-1] + 'ay\n'
        elif line.endswith(('a', 'e', 'u', 'i', 'o')):
            line += ' way\n'
        finish.write(line)
    finish.close()
    begin.close()
    return count


poem = "Thou blind fool, Love, what dost thou to mine eyes\
\nThat they behold, and see not what they see\
\nThey know what beauty is, see where it lies\
\nYet what the best is take the worst to be"

input_file = 'txt\lab4var4in.txt'
output_file = 'txt\lab4var4out.txt'
additional.writer(poem, input_file)
found = change_str(input_file, output_file)

additional.user_input_name()