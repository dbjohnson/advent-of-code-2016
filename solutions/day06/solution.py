from collections import defaultdict


letter_counts = defaultdict(lambda: defaultdict(int))


with open('input.txt', 'r') as fh:
    for line in fh:
        for i, char in enumerate(line.strip()):
            letter_counts[i][char] += 1

code = [
    sorted(letter_counts[i], key=lambda c: letter_counts[i][c], reverse=True)[0]
    for i in sorted(letter_counts)
]

print('part 1:', ''.join(code))


code = [
    sorted(letter_counts[i], key=lambda c: letter_counts[i][c], reverse=True)[-1]
    for i in sorted(letter_counts)
]

print('part 2:', ''.join(code))
