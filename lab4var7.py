import additional
#Coding utf-8


def zero(beginfile: str, file: str):
    begin = open(beginfile, 'rt')
    finish = open(file, 'wt')
    count = 0
    while True:
        line = begin.readline()
        line = line.strip('\n')
        if not line:
            break
        if line.endswith("0"):
            finish.write(line + '\n')
            count += 1
    finish.close()
    begin.close()
    return count


shopping_list = "Бананы   12.23\
\nАнанасы   3.40 \
\nКокосы  124.23\
\nЯблоки  233.40\
\nЛимоны  789.23\
\nГранат   55.71\
\nВиноград  5.20\
\nСливы   233.40"

input_file = 'txt\lab4var7in.txt'
output_file = 'txt\lab4var7out.txt'
additional.writer(shopping_list, input_file)
empty = zero(input_file, output_file)

additional.user_input_num(input_file, output_file)
