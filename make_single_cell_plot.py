#! /usr/bin/env python2

import argparse
import os.path
import csv
import matplotlib.pyplot as pyplot

parser = argparse.ArgumentParser()
parser.add_argument('input_file', nargs='?', type=str, action='store')
parser.add_argument('--output', nargs='?', type=argparse.FileType('w'), dest='output', action='store', help='If specified, the location to save a picture of the plots to.')

args = parser.parse_args()

if input_file in args:
	f = open(input_file, 'r')
else:
	f = open('single_cell_select.csv', 'r')
reader = csv.reader(f)

data = []

#colors = ['#000000'] * 6
colors = ['#22AA22', '#66FF66', '#AAAAFF', '#000077', '#CCCC00', '#FF0000']
names = ['needsaname']*6
cluster_sizes = [1,2,4,8]

for row in reader:
	if len(row) == 0:
		continue
	data.append([ float(x) for x in row])


fig = pyplot.figure()
axes = fig.add_subplot(1, 1, 1)
#axes.set_title("Single cell select")
axes.set_xlabel("Size of cluster")
axes.set_ylabel("Time (s)")

for idx in range(len(data)):
	axes.plot(cluster_sizes, data[idx], '-o', color=colors[idx], linewidth=2)

axes.set_ylim(bottom=0)

if args.output != None:
	pyplot.savefig(args.output)
else:
	pyplot.show()

