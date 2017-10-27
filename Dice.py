from __future__ import print_function
import itertools


probs = {}
for x, y in itertools.product(range(1, 7), range(1, 7)):

    total = x + y
    for k in range(1, 21):
        if k % total == 0:
            probs[k] = probs.get(k, 0) + 1.0/36
print(probs)
