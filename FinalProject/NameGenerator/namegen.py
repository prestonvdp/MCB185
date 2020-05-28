#!/usr/bin/env python3

import fileinput

puncs =  '.,1?!:;-*"_()[]{}<>/1234567890—“”’‘–' # you may need to add more
spaces = ' ' * len(puncs)

for rawline in fileinput.input():

	# convert to lowercase
	lower = rawline.lower()
	
	# convert punctuation to spaces
	table = lower.maketrans(puncs, spaces)
	line = lower.translate(table)
	
	# start work here
	for word in line.split():
		print(word)