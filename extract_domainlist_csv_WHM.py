#!/usr/bin/python

import sys

def extract_domain(line):
	line = line.split(",")
	print(line[0])
	
if len(sys.argv) != 2:
	exit('Usage: extract.py root.csv\n')

file = open(sys.argv[1],'r')

lines = file.readlines()
del lines[0]

for x in lines:
	extract_domain(x)
