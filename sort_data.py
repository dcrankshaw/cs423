#! /usr/bin/env python2

import argparse
import os.path
import csv

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str)
parser.add_argument('--output', nargs='?', type=str, action='store', default='')

args = parser.parse_args()

#TODO look at the files in the directory and use that to get the cluster size
filenames = dict([(x, os.path.join(args.input, str(x)+'.txt')) for x in [1,2,4,8]])
# read in the files for each of the cluster sizes
# data[line number][cluster size] = value
data = {}
for (size, filename) in filenames.iteritems():
	f = open(filename)
	for (num, line) in enumerate(f):
		line = line.strip()
		if len(line) > 0:
			if num not in data:
				data[num] = {}
			data[num][size] = float(line.strip())


# Write out the select a single cell times
f = open(os.path.join(args.output, 'single_cell_select.csv'), 'wb')
csvout = csv.writer(f)
for i in range(6):
	csvout.writerow([ data[i][1], data[i][2], data[i][4], data[i][8] ] )

f = open(os.path.join(args.output, 'cube_range_query.csv'), 'wb')
csvout = csv.writer(f)
for i in range(6, 12):
	csvout.writerow([ data[i][1], data[i][2], data[i][4], data[i][8] ] )

f = open(os.path.join(args.output, 'slice_range_query.csv'), 'wb')
csvout = csv.writer(f)
for i in range(12, 18):
	csvout.writerow([ data[i][1], data[i][2], data[i][4], data[i][8] ] )

f = open(os.path.join(args.output, 'equality.csv'), 'wb')
csvout = csv.writer(f)
for i in range(18, 24):
	csvout.writerow([ data[i][1], data[i][2], data[i][4], data[i][8] ] )

f = open(os.path.join(args.output, 'window_2d.csv'), 'wb')
csvout = csv.writer(f)
for i in range(24, 28):
	csvout.writerow([ data[i][1], data[i][2], data[i][4], data[i][8] ] )

f = open(os.path.join(args.output, 'window_3d.csv'), 'wb')
csvout = csv.writer(f)
for i in range(28, 32):
	csvout.writerow([ data[i][1], data[i][2], data[i][4], data[i][8] ] )

f = open(os.path.join(args.output, 'window_5d.csv'), 'wb')
csvout = csv.writer(f)
for i in range(32, 36):
	csvout.writerow([ data[i][1], data[i][2], data[i][4], data[i][8] ] )

f = open(os.path.join(args.output, 'group_by_separate.csv'), 'wb')
csvout = csv.writer(f)
for i in [36+2x for x in range(6)]:
	csvout.writerow([ data[i][1], data[i][2], data[i][4], data[i][8] ] )

f = open(os.path.join(args.output, 'group_by_overlap.csv'), 'wb')
csvout = csv.writer(f)
for i in [37+2x for x in range(6)]:
	csvout.writerow([ data[i][1], data[i][2], data[i][4], data[i][8] ] )

