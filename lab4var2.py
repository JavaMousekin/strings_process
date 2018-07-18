import additional


def empty_as(beginfile: str, file: str):
    begin = open(beginfile, 'rt')
    finish = open(file, 'wt')
    count = 0
    while True:
        line = begin.readline()
        if not line:
            break
        if line.startswith('As'):
            line = "\n"
            count += 1
        finish.write(line)
    finish.close()
    begin.close()
    return count


add = additional

poem = "O, speak again, bright angel, for thou art\
       \nAs glorious to this night, being oer my head,\
       \nAs is a winged messenger of heaven\
       \nUnto the white-upturned wondering eyes\
       \nOf mortals that fall back to gaze on him\
       \nWhen he bestrides the lazy-puffing clouds\
       \nAnd sails upon the bosom of the air."

input_file = 'txt\lab4var2in.txt'
output_file = 'txt\lab4var2out.txt'
additional.writer(poem, input_file)
empty = empty_as(input_file, output_file)

additional.user_input_num(input_file, output_file)
print(empty)
