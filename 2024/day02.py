def part_one(numbers):

    direction = None

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]

        if abs(diff) > 3 or diff == 0:
            return False

        if diff > 0: 
            if direction is None:
                direction = "increasing"
            elif direction != "increasing":
                return False

        elif diff < 0: 
            if direction is None:
                direction = "decreasing"
            elif direction != "decreasing":
                return False

    return True


def part_two(numbers):
   
    for i in range(len(numbers)):
        sublist = numbers[:i] + numbers[i+1:]
        if part_one(sublist):
            return True

    return False 


def main():
    counter_safe_part_one = 0
    counter_safe_part_two = 0

    with open('input.in', 'r') as file:
        for line in file:
            numbers = list(map(int, line.split()))
            if part_one(numbers):
                counter_safe_part_one += 1

            if part_two(numbers):
                counter_safe_part_two += 1

    print(f"Safe sequences (part one): {counter_safe_part_one}")
    print(f"Safe sequences (part two): {counter_safe_part_two}")

main()