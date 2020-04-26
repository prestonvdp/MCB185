#!/usr/bin/env python3

import time

# Move the triple quotes downward to uncover each segment of code

""""

# Previously, we have used the 'in' keyword for iterating over sequences

for c in 'ACGT': print(c)                    # strings are sequences of letters
for i in range(5): print(i)                  # range() makes in sequences
for pet in ('cat', 'dog', 'bun'): print(pet) # tuples are sequences
for pet in ['cat', 'dog', 'bun']: print(pet) # lists are sequences

# The other use of 'in' is completely different!
# 'in' can also be used to search for values within sequences

if 1 in ('a', 'b', 'c', 1, 2, 3): print('yes')
if 'bun' in 'cats are cool but buns are cooler': print('true')

# You can also do searches with a loop

data = [0] * 1000
data[999] = 1
for v in data:
	if v == 1:
		print('found')
		break

# But this is much more intuitive using 'in'
if 1 in data: print('found')

# What about performance? Let's test using the performance timer

trials   = 100000

# test 1: iterating using range()
t0 = time.perf_counter()
for i in range(trials):
	found = False
	if 1 in data:
		found = True
t1 = time.perf_counter()
print(f'range: {t1-t0:.4f}')

# test 2: iterating over values
t0 = time.perf_counter()
for i in range(trials):
	found = False
	for v in data:
		if v == 1:
			found = True
			break
t1 = time.perf_counter()
print(f'values: {t1-t0:.4f}')

# test 3: using 'in'
t0 = time.perf_counter()
for i in range(trials):
	for j in range(len(data)):
		found = False
		if data[j] == 1:
			found = True
			break
t1 = time.perf_counter()
print(f'in: {t1-t0:.4f}')

# Not only does 'in' look better, it's also 4-10 times faster
# However, by changing the algorithm, we can go 100x faster (stay tuned)

""""