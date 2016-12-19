import re


with open('input.txt', 'r') as fh:
    addresses = [l.strip() for l in fh]


def abbas(s):
    # the ?= allows overlapping matches via lookahead assertion
    for match in re.findall(r'(?=((.)(?!\2)(.)\3\2))', s):
        yield match[0]


def supports_TLS(address):
    hypernet_seqs = re.findall('\[.*?\]', address)
    for seq in hypernet_seqs:
        if any(abbas(seq)):
            return False

    for seq in re.split('\[.*?\]', address):
        if any(abbas(seq)):
            return True


print('part 1:', len(list(filter(None, map(supports_TLS, addresses)))))


def abas(s):
    # the ?= allows overlapping matches via lookahead assertion
    for match in re.findall(r'(?=((.)(?!\2)(.)\2))', s):
        yield match[0]


def supports_SSL(address):
    hypernet_seqs = re.findall('\[.*?\]', address)
    supernet_seqs = re.split('\[.*?\]', address)

    for s1 in hypernet_seqs:
        for aba in abas(s1):
            bab = '{b}{a}{b}'.format(a=aba[0], b=aba[1])
            for s2 in supernet_seqs:
                if bab in s2:
                    return True


print('part 2:', len(list(filter(None, map(supports_SSL, addresses)))))
