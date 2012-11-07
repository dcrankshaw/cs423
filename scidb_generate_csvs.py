import random
import csv

num_cells = 32*(10**6)
#num_cells = 1000
#dimensions = [2, 3, 5]
dimensions = [5]
long_offset = 2**33
base_word_length = 20

for dim in dimensions:
    dim_file = '/home/scidb/' + str(dim) + '_dims.csv'
    #dim_file = '/tmp/' + str(dim) + '_dims.csv'
    myfile = open(dim_file, 'wb')
    writer = csv.writer(myfile)
    length = int(round((num_cells**(1.0 / dim))))
    cur_index = [0 for x in range(dim)]
    done = False
    row_num = 0
    while not done:
	if row_num % 10000 == 0:
	    print('row ' + str(row_num))
        entry = list(cur_index)
        num = long_offset + random.randint(0,999)
        string = ''
        word_length = base_word_length + random.randint(-5, 5)
        for letter in range(word_length):
            string += random.choice('abcdefghijklmnopqrstuvwxyz')
        entry.append(num)
        entry.append(string)
        writer.writerow(entry)
        keep_adding = True
        i = 0
        while keep_adding and i < len(cur_index):
            updated_index = cur_index[i] + 1
            if updated_index >= length:
                cur_index[i] = 0
                i = i + 1
            else:
                keep_adding = False
                cur_index[i] = updated_index
        if keep_adding:
            done = True
	row_num += 1
    myfile.close()
    print('finished dim ' + str(dim))

