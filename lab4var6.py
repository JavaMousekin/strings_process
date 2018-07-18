import additional
import re


def change_str(beginfile: str, file: str):
    begin = open(beginfile, 'rt')
    finish = open(file, 'wt')
    while True:
        line = begin.readline()
        if not line:
            break
        if re.search('(@\w+(\.\w+)+)', line):
            continue
        else:
            finish.write(line)
    finish.close()
    begin.close()


line = "Hello it my e-mail forte@mail.my\
\nYou can write me any time if you need.\
\npiano@mail.com\
\nFortissimo12@mail.su.io\
\nPerfect day is day with friends\
\nMajor_mario12@mailo"

input_file = 'txt\lab4var6in.txt'
output_file = 'txt\lab4var6out.txt'
additional.writer(line, input_file)
change_str(input_file, output_file)

additional.user_input_num(input_file, output_file)
