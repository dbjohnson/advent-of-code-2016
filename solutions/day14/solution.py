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


def idx_of_next_key(start_idx=0, stretch=0):
    for idx in range(start_idx, 10 ** 999):
        m = re.search(r'(([a-z0-9])\2{2,})', hash_idx(idx, stretch))
        if m:
            five = m.group()[0] * 5
            for offset in range(1000):
                if five in hash_idx(idx + offset + 1, stretch):
                    return idx


def solve(n=64, stretch=0):
    start_idx = 0
    for i in range(n):
        idx = idx_of_next_key(start_idx, stretch)
        start_idx = idx + 1
    return idx


print('part 1:', solve())
print('part 2:', solve(stretch=2016))
