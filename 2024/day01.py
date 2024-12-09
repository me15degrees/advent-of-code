def part_one(seq1, seq2):

    diff = sum(abs(a - b) for a, b in zip(seq1, seq2))

    return diff

def part_two(seq1, seq2):

    result = 0

    for item in seq1:
        multiplier = seq2.count(item)
        result += multiplier*item
        
    return result


def main():
    with open('input.in', 'r') as arquivo:
        seq1, seq2 = zip(*(map(int, linha.strip().split()) for linha in arquivo))

    seq1 = sorted(seq1)
    seq2 = sorted(seq2)

    res_part_one = part_one(seq1, seq2)
    res_part_two = part_two(seq1, seq2)

    print(res_part_one, res_part_two)

main()