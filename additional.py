def writer(content: str, file: str):
    filew = open(file, 'wt+')
    filew.write(content)
    filew.close()


def show(finish_file: str):
    finish = open(finish_file, 'rt')
    text = ""
    count = 0
    while True:
        line = finish.readline()
        if not line:
            break
        count += 1
        if line == '\n':
            continue
        text += line
    return text + " "


def user_input_num(input_file, output_file):
    print('You should choose file for showing:\n Press:\n 1 - for choose input file\n 2 - for choose output file')
    while True:
        a = int(input('Your answer is '))
        if a == 1:
            print('\n' + show(input_file))
            break
        elif a == 2:
            print('\n' + show(output_file))
            break
        else:
            print("Try again, I don't understand")


def user_input_name():
    while True:
        print('You should type file name for showing: ')
        input_file = 'txt/' + input()
        try:
            print('\n' + show(input_file))
            break
        except FileNotFoundError:
            print("Try again, I don't understand")

