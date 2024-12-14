import re

def part_one():
    total = 0
    with open('input.in', 'r') as file:
        for line in file:
            matches = re.findall(r"mul\((\d+),(\d+)\)", line)
            for match in matches:
                itens = tuple(map(int, match))
                total += itens[0] * itens[1]
    return total

def part_two():

    initial_state = 1 
    total = 0
    state = initial_state  
    
    with open('input.in', 'r') as file:
        for line in file:
            donts = list(re.finditer(r"don't", line))  
            dos = list(re.finditer(r"do\(\)", line))  
            multiplies = list(re.finditer(r"mul\((\d+),(\d+)\)", line))  
            
            indices_donts = [dont.start() for dont in donts]
            indices_dos = [do.start() for do in dos]
            indices_multiplies = [multiply.start() for multiply in multiplies]

            for i, multiply_index in enumerate(indices_multiplies):
            
                if indices_donts and multiply_index > indices_donts[0]:
                    state = 0  
                    indices_donts.pop(0)  
        
                if indices_dos and multiply_index > indices_dos[0]:
                    state = 1  
                    indices_dos.pop(0)  
                
                if state == 1:
                    itens = tuple(map(int, multiplies[i].groups()))
                    total += itens[0] * itens[1]
                
    return total

def main():
    res_part_one = part_one()
    res_part_two = part_two()
    print(res_part_one)
    print(res_part_two)
    
main()


