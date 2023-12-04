#PART ONE
with open("input_day1.txt", 'r') as certificate:
    
    s = 0 # inicialize variable sum with zero value

    for line in certificate: # read every line in the archive
        digits = [] # inicialize an empty list

        for item in line: # read every item in the line
            if item.isdigit(): # verify if item is a number
                digits.append(int(item)) # add the int version of the item in the list

        if len(digits) == 1: # if the size is one, it's necessary to duplicate the num - to concatenate!
            num = str(digits[0])
            digit = num+num
            s += int(digit) # add them in the sum
        
        elif len(digits) > 1: # if the size is more than one, just concatenate the first and last digits
            first = str(digits[0])
            last = str(digits[-1])
            digit = first+last
            s += int(digit) # add them in the sum
        print(s) # the result will appear here

# PART TWO
with open("input_day1.txt", 'r') as certificate:
    s = 0 # inicialize variable sum with zero value

    for line in certificate:
        digits = [] # inicialize an empty list
        
        # preparete lines to avoid the bad results of overlapping
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
            if item.isdigit(): # verify if the item is a number
                digits.append(int(item)) # if so, add in the list!

        if len(digits) == 1: # concatenate if the size is one
            num = str(digits[0])
            digit = num+num
        
        elif len(digits) > 1: # concatenate the first and last digit if the size is more than one
            first = str(digits[0])
            last = str(digits[-1])
            digit = first+last
        
        s += int(digit) # sum them all together
    print(s) # show the result
