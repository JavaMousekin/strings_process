import additional
import re


def pass_s_words(beginfile: str, file: str):
    begin = open(beginfile, 'rt')
    finish = open(file, 'wt')
    new_line = ""
    while True:
        line = begin.readline()
        if not line:
            break
        password = re.search(":[1-9]+", line)
        myset = line.split(' ')
        for p in myset:
            if ":" in p:
                continue
            else:
                new_line += p.title()+" "
        finish.write(new_line)
    finish.close()
    begin.close()
    return str(password[0]).lstrip(':')

string = "d:/ФайлыPython/files/file1.txt Log:Admin1 Password:12345 send message saturday january 2018 Stephen"
input_file = 'txt\lab4var8in.txt'
output_file = 'txt\lab4var8out.txt'
additional.writer(string, input_file)
pas = pass_s_words(input_file, output_file)

additional.user_input_num(input_file, output_file)
print(pas)
