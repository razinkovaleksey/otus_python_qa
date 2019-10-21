def replace_num_to_sign(input_string):
    return input_string.replace('1', '+').replace('0', '-')


with open("data.csv", 'r', encoding='cp1251') as input_file, open('result.txt', 'w', encoding='utf-8') as output_file:
    lines = input_file.read().splitlines()
    res_lines = [line.split(',') for line in lines][1:]
    res_lines_f = [line[:2] + [replace_num_to_sign(num) for num in line[2:]] for line in res_lines]
    print(res_lines_f)
    for line in res_lines_f:
        output_file.write('	'.join(line) + '\n')
