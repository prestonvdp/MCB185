#!/usr/bin/env python3

import argparse
#import biotools

parser = argparse.ArgumentParser(
	description='PWM Finder.')
parser.add_argument('--dna', required=True, type=str,
	metavar='<str>', help='FASTA file')
parser.add_argument('--pwm', required=True, type=str,
	metavar='<str>', help='transfac file')
parser.add_argument('--threshold', required=True, type=float,
	metavar='<float>', help='probability threshold for finding motif')
arg = parser.parse_args()


