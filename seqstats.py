#!/usr/bin/env python3

import fileinput

# Write a program that computes typical sequence stats
# No, you cannot import any other modules!
# Use rand_seq to generate the sequences
# Expected output is shown below


# cut -------------------------------------------------------------------------

seqs = 0
nts = 0
count = [0] * 4
lengths = []

for line in fileinput.input():
	if line.startswith('>'): continue
	seq = line.rstrip()
	seqs += 1
	nts += len(seq)
	for c in seq:
		if   c == 'A': count[0] += 1
		elif c == 'C': count[1] += 1
		elif c == 'G': count[2] += 1
		elif c == 'T': count[3] += 1
	lengths.append(len(seq))

lengths.sort()
sum = 0
n50 = None
for i in range(len(lengths)):
	sum += lengths[i]
	if sum >= nts/2:
		n50 = lengths[i]
		break

prob = []
for i in range(len(count)):
	prob.append(count[i]/nts)


print(f'Number of sequences: {seqs}')
print(f'Number of letters: {nts}')
print(f'Minimum length: {lengths[0]}')
print(f'Maximum length: {lengths[-1]}')
print(f'N50: {n50}')
print(f'Composition: A={prob[0]:.3f} C={prob[1]:.3f} G={prob[2]:.3f} T={prob[3]:.3f}')

# cut -------------------------------------------------------------------------

"""
python3 rand_seq.py 100 100 100000 0.35 | python3 seqstats.py
Number of sequences: 100
Number of letters: 4957689
Minimum length: 219
Maximum length: 99853
N50: 67081
Composition: A=0.325 C=0.175 G=0.175 T=0.325
"""
