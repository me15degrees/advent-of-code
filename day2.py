# PART 1
"""total_index = 0

with open("input_day2.txt", 'r') as tentativas:
    for line in tentativas:
        identification, content = line.replace(";", ",").split(":")
        content = content.split(" ")
        index = identification.split(" ")[1]
        
        ispossible = True
        
        for idx, item in enumerate(content):
            item = item.strip()
            if item == "green" or item == "green," or item == "green;":
                num = int(content[idx - 1])
                if num > 13:
                    ispossible = False
            elif item == "blue" or item == "blue," or item =="blue;":
                num = int(content[idx - 1])
                if num > 14:
                    ispossible = False
            elif item == "red" or item == "red," or item =="red;":
                num = int(content[idx - 1])
                if num > 12:
                    ispossible = False

        if ispossible:
            total_index += int(index)

        print("Is possible:", ispossible)
    print("Total Index:", total_index)
"""
# PART 2
with open("input_day2.txt", 'r') as tentativas:
    soma = 0
    for line in tentativas:
        identification, content = line.replace(";", ",").split(":")
        content = content.split(" ")
        index = identification.split(" ")[1]
        
        num_green = []
        num_red = []
        num_blue = []

        for idx, item in enumerate(content):
            item = item.strip(",").strip()

            if item == "green":
                num = int(content[idx-1])
                num_green.append(num)
            elif item == "blue":
                num = int(content[idx-1])
                num_blue.append(num)
            elif item == "red":
                num = int(content[idx-1])
                num_red.append(num)

        menor_green = max(num_green, default=1)
        menor_blue = max(num_blue, default=1)
        menor_red = max(num_red, default=1)
        print(menor_green,menor_blue,menor_red)
        produto = menor_red * menor_green * menor_blue
        

        
        soma += produto

    print(soma)
