import re


def rotate(string, steps, direction):
    steps %= len(string)
    if direction == 'right':
        string = string[-steps:] + string[:-steps]
    else:
        string = string[steps:] + string[:steps]
    return string


def apply_rule(password, rule, reverse=False):
    if rule.startswith('swap letter'):
        chars = ''.join(re.findall('letter ([a-z]{1})', rule))
        trans = str.maketrans(chars, ''.join(reversed(chars)))
        return password.translate(trans)
    if rule.startswith('swap position'):
        a, b = map(int, re.findall('position ([0-9]+)', rule))
        mn, mx = min(a, b), max(a, b)
        return password[:mn] + password[mx] + password[mn + 1:mx] + password[mn] + password[mx + 1:]
    if rule.startswith('move position'):
        frm, to = map(int, re.findall('([0-9]+)', rule))
        c = password[frm]
        password = password[:frm] + password[frm + 1:]
        return password[:to] + c + password[to:]
    if rule.startswith('reverse positions'):
        frm, to = map(int, re.findall('([0-9]+)', rule))
        return password[:frm] + ''.join(reversed(password[frm:to + 1])) + password[to + 1:]
    if rule.startswith('rotate based on position'):
        char = re.findall('letter ([a-z])', rule)[0]
        idx = password.index(char)
        steps = idx + 1 + (idx >= 4)
        return rotate(password, steps, 'right')
    if rule.startswith('rotate left'):
        steps = int(re.findall('([0-9]+) step', rule)[0])
        return rotate(password, steps, 'left')
    if rule.startswith('rotate right'):
        steps = int(re.findall('([0-9]+) step', rule)[0])
        return rotate(password, steps, 'right')


with open('input.txt', 'r') as fh:
    rules = [line.strip() for line in fh]

password = 'abcdefgh'
for rule in rules:
    password = apply_rule(password, rule.strip())
    assert len(password) == 8, rule + " " + password
    for char in 'abcdefgh':
        assert char in password, rule + " " + password

print('part 1:', password)


scrambled = 'fbgdceah'
for rule in reversed(rules):
    scrambled = apply_rule(scrambled, reverse=True)

