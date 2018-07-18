import additional
import re


def change_str(beginfile: str, file: str):
    begin = open(beginfile, 'rt')
    finish = open(file, 'wt')
    while True:
        c_line = begin.readline()
        if not c_line:
            break
        line1 = re.search("(@\w+(\.\w+)+)", c_line)
        finish.write(str(line1[0]).lstrip('@'))
    finish.close()
    begin.close()


line = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2018 "

input_file = 'txt\lab4var5in.txt'
output_file = 'txt\lab4var5out.txt'
additional.writer(line, input_file)
change_str(input_file, output_file)

additional.user_input_num(input_file, output_file)

