#PART ONE
"""with open("input_day1.txt", 'r') as certificate:
    soma = 0

    for line in certificate:
        digits = []

        for item in line:
            if item.isdigit():
                digits.append(int(item))

        if len(digits) == 1:
            num = str(digits[0])
            digit = num+num
            soma += int(digit)
        elif len(digits) > 1:
            first = str(digits[0])
            last = str(digits[-1])
            digit = first+last
            soma += int(digit)
        print(soma)
"""
#PART TWO
# numbers = ["one","two","three","four","five","six","seven","eight","nine"]
# with open("input_day1.txt", 'r') as certificate:

#     soma = 0
   
#     lista = []
#     for line in certificate:
#         digits_line = []    
#         line = ''.join(caracter for caracter in line if caracter.isalpha() or caracter.isspace())
        
#         line = line.replace("one","o1e")
#         line = line.replace("two","t2o")
#         line = line.replace("three","t3e")
#         line = line.replace("four","f4r")
#         line = line.replace("five","f5e")
#         line = line.replace("six","s6x")
#         line = line.replace("seven","s7n")
#         line = line.replace("eight","e8t")
#         line = line.replace("nine","n9e")
#         for digit in line:
#             if digit.isdigit():
#                 digits_line.append(digit)
#                 print(digits_line)
                
      


with open("input_day1.txt", 'r') as certificate:
    soma = 0

    for line in certificate:
        digits = []
        print(line)
        line = line.replace("one","o1e")
        line = line.replace("two","t2o")
        line = line.replace("three","t3e")
        line = line.replace("four","f4r")
        line = line.replace("five","f5e")
        line = line.replace("six","s6x")
        line = line.replace("seven","s7n")
        line = line.replace("eight","e8t")
        line = line.replace("nine","n9e")

        for item in line:
            if item.isdigit():
                digits.append(int(item))

        if len(digits) == 1:
            num = str(digits[0])
            digit = num+num
        elif len(digits) > 1:
            first = str(digits[0])
            last = str(digits[-1])
            digit = first+last
        print(line)
        print(digit)
        soma += int(digit)
    print(soma)