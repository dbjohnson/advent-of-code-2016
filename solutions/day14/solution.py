import re
from functools import lru_cache
from hashlib import md5

salt = 'zpqevtbw'


def hash(val, stretch=0):
    for _ in range(stretch + 1):
        val = md5(val.encode()).hexdigest()
    return val


@lru_cache(1000)
def hash_idx(idx, stretch=0):
    return hash(salt + str(idx), stretch)


def valid_pad(idx, stretch=0):
        m = re.search(r'(([a-z0-9])\2{2,})', hash_idx(idx, stretch))
        if m:
            five = m.group()[0] * 5
            for offset in range(1000):
                if five in hash_idx(idx + offset + 1, stretch):
                    return idx


def nth_pad(n=64, stretch=0):
    found = 0
    for idx in range(10 ** 999):
        if valid_pad(idx, stretch):
            found += 1
            if found == n:
                return idx


print('part 1:', nth_pad())
print('part 2:', nth_pad(stretch=2016))
