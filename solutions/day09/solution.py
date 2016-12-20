import re


with open('input.txt', 'r') as fh:
    puzzle = fh.read().strip()


def expand(s, recursive=False):
    length = 0
    while s:
        match = re.search(r'\(([0-9]+)x([0-9]+)\)', s)
        if match:
            length += match.start()
            chars_to_repeat, n_repeats = map(int, match.groups())
            seq = s[match.end():match.end() + chars_to_repeat]
            if recursive:
                length += expand(seq, recursive=True) * n_repeats
            else:
                length += len(seq) * n_repeats

            s = s[match.end() + chars_to_repeat:]
        else:
            return length + len(s)

    return length


print('part 1:', expand(puzzle))
print('part 2:', expand(puzzle, recursive=True))
