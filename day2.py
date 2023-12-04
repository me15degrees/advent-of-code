# PART ONE
total_index = 0 # sum of indexes start at zero

with open("input_day2.txt", 'r') as attempt:
    for line in attempt: # read the lines in the archive
        identification, content = line.replace(";", ",").split(":") # separete the lines in two variables
        
        content = content.split(" ") # separete content by empty spaces
        index = identification.split(" ")[1] # index will be the second part of identification, without the word game
        
        ispossible = True # create a pass indicator 
        
        for idx, item in enumerate(content):
            item = item.strip()
            if item == "green" or item == "green," or item == "green;":
                num = int(content[idx - 1]) # get the number before the appearance of color
                if num > 13: # if it exceeds the estimated value, it does not count
                    ispossible = False # so ispossible become False
            elif item == "blue" or item == "blue," or item =="blue;":
                num = int(content[idx - 1]) # get the number before the appearance of color
                if num > 14: # if it exceeds the estimated value, it does not count
                    ispossible = False # so ispossible become False
            elif item == "red" or item == "red," or item =="red;":
                num = int(content[idx - 1]) # get the number before the appearance of color
                if num > 12: # if it exceeds the estimated value, it does not count
                    ispossible = False # so ispossible become False

        if ispossible: # counts the times that the variable remained with the value True
            total_index += int(index)

    print("total index:", total_index) # show the result

# PART TWO
with open("input_day2.txt", 'r') as attempt:
    
    s = 0
    
    for line in attempt:  # read the lines in the archive
        identification, content = line.replace(";", ",").split(":") # separete the lines in two variables
        content = content.split(" ") # separete content by empty spaces
        index = identification.split(" ")[1] # index will be the second part of identification, without the word game
        # create empty lists for each color
        num_green = []
        num_red = []
        num_blue = []

        for idx, item in enumerate(content):
            item = item.strip(",").strip()

            if item == "green":
                num = int(content[idx-1]) # get the number before the appearance of color
                num_green.append(num) # add in the list
            elif item == "blue":
                num = int(content[idx-1]) # get the number before the appearance of color
                num_blue.append(num) # add in the list
            elif item == "red":
                num = int(content[idx-1]) # get the number before the appearance of color
                num_red.append(num) # add in the list
        # get the max number for each color
        max_green = max(num_green, default=1)
        max_blue = max(num_blue, default=1)
        max_red = max(num_red, default=1)
        
        product = max_red * max_green * max_blue # multiplicate them
        
        s += product # sum of all multiplications

    print(s) # show the result
