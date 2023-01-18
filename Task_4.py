

def decompress(string): 
    result = "" 
    # итерация по циклу с шагом 2 (первое - количество повторений символа, второй - сам символ)
    for i in range(0, len(string), 2): 
        result += string[i+1] * int(string[i]) 
    return result

with open('input2.txt', 'r') as file:
  input_str=file.read()

out_str=decompress(input_str)

with open('out2.txt', 'w') as file:
  file.write(out_str)
