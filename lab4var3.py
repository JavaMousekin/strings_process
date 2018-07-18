import additional


def name_(beginfile: str, file: str):
    begin = open(beginfile, 'rt')
    finish = open(file, 'wt')
    count = 0
    while True:
        line = begin.readline()
        if not line:
            break
        if 'name' in line:
            line = line.replace('name', 'Surname')
            count += 1
        finish.write(line)
    finish.close()
    begin.close()
    return count


add = additional

poem = "What's Montague? It is nor hand, nor foot, \
\nNor arm, nor face, nor any other part \
\nBelonging to a man. O, be some other name.\
\nWhat's in a name? That which we call a rose\
\nBy any other name would smell as sweet"

input_file = 'txt\lab4var3in.txt'
output_file = 'txt\lab4var3out.txt'
additional.writer(poem, input_file)
found = name_(input_file, output_file)

additional.user_input_num(input_file, output_file)
print(found)