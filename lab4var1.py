import additional
#Coding utf-8


def empty_as(beginfile: str, file: str):
    begin = open(beginfile, 'rt')
    finish = open(file, 'wt')
    count = 0
    while True:
        line = begin.readline()
        if not line:
            break
        if line.startswith('И'):
            finish.write(line)
            count += 1
    finish.close()
    begin.close()
    return count


poem = "У лукоморья дуб зелёный;\
\nЗлатая цепь на дубе том:\
\nИ днём и ночью кот учёный\
\nВсё ходит по цепи кругом;\
\nИдёт направо - песнь заводит,"

input_file = 'txt\lab4var1in.txt'
output_file = 'txt\lab4var1out.txt'
additional.writer(poem, input_file)
empty = empty_as(input_file, output_file)

additional.user_input_num(input_file, output_file)
print(empty)
