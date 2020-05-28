#!/usr/bin/env python3

import argparse
import biotools
import re
import math

parser = argparse.ArgumentParser(
	description='Horiztonal gene transfer detector.')
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='FASTA file')
parser.add_argument('--pseudo', required=False, type=float, default=1.0,
	metavar='<float>', help='pseudocount [%(default)f]')
arg = parser.parse_args()

for name, seq in biotools.read_fasta(arg.file):

	# we didn't go over regular expressions
	# but this is how you get the locus name
	match = re.search('locus_tag=(\w+)', name)
	locus = match[1]
	print(locus)

	