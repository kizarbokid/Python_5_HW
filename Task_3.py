with open('input.txt', 'r') as file:
  input_str=file.read()


def compress(string):
    compr_str = ""
    current_i = 0
    # пока номер текущего элемента меньше длины входной строки
    while current_i < len(string):
        count = 1
        next_j = current_i+1
        # пока текущий элемент = следующему и номер следующего элемента меньше длины входной строки
        while next_j < len(string) and string[next_j] == string[current_i]:
            next_j += 1
            count += 1
        compr_str += str(count) + string[current_i]
        # как только одинаковые элементы закончились, рассмотрим следующий
        current_i = next_j
    return compr_str

out_str=compress(input_str)

with open('out.txt', 'w') as file:
  file.write(out_str)