#!/usr/bin/env python

from subprocess import Popen, PIPE
from time import time

no_overlap_arrays = ['twoxtwo', 'threexthree', 'fivexfive']
overlap_arrays = ['twoxtwooverlap', 'threexthreeoverlap', 'fivexfiveoverlap']


def do_query(query, aql):
    print query
    timestart = time()
    iquery_bin = 'iquery'
    if aql:
        proc = Popen([iquery_bin, "-q", query], stdout=PIPE)
    else:
        proc = Popen([iquery_bin, "-aq", query], stdout=PIPE)
    result = proc.communicate()[0]
    print result
    print 'Time: ' + str(time() - timestart) + '\n'

def run_tests():
    selectqueries = []
    selectqueries.append('"select * from twoxtwo where i=1 and j=1;"')
    selectqueries.append('"select * from twoxtwooverlap where i=1 and j=1;"')
    selectqueries.append('"select * from threexthree where i=1 and j=1 and k = 1;"')
    selectqueries.append('"select * from threexthreeoverlap where i=1 and j=1 and k = 1;"')
    selectqueries.append('"select * from fivexfive where i=1 and j=1 and k = 1 and l = 1 and m = 1;"')
    selectqueries.append('"select * from fivexfiveoverlap where i=1 and j=1 and k = 1 and l = 1 and m = 1;"')
    for q in selectqueries:
        do_query(q, true)

#cube range queries
    cubequeries = []
    cubequeries.append('"between(twoxtwo, 0, 0, 1000, 1000"')
    cubequeries.append('"between(twoxtwooverlap, 0, 0, 1000, 1000"')
    cubequeries.append('"between(threexthree, 0, 0, 0, 80, 80, 80"')
    cubequeries.append('"between(threexthreeoverlap, 0, 0, 0, 80, 80, 80"')
    cubequeries.append('"between(fivexfive, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8"')
    cubequeries.append('"between(fivexfiveoverlap, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8"')
    for q in cubequeries:
        do_query(q, false)

#slice range queries
    slicequeries = []
    slicequeries.append('"between(twoxtwo, 0, 0, 32, 32"')
    slicequeries.append('"between(twoxtwooverlap, 0, 0, 32, 32"')
    slicequeries.append('"between(threexthree, 0, 0, 0, 0, 32, 32"')
    slicequeries.append('"between(threexthreeoverlap, 0, 0, 0, 0, 32, 32"')
    slicequeries.append('"between(fivexfive, 0, 0, 0, 0, 0, 0, 0, 0, 32, 32"')
    slicequeries.append('"between(fivexfiveoverlap, 0, 0, 0, 0, 0, 0, 0, 0, 32, 32"')
    for q in cubequeries:
        do_query(q, false)

#attribute equality queries
    attrqueries = []
    attrqueries.append('"select * from twoxtwo where valnum = 8589934788;"')
    attrqueries.append('"select * from twoxtwooverlap where valnum = 8589934788;"')
    attrqueries.append('"select * from threexthree where valnum = 8589934788;"')
    attrqueries.append('"select * from threexthreeoverlap valnum = 8589934788;"')
    attrqueries.append('"select * from fivexfive where valnum = 8589934788;"')
    attrqueries.append('"select * from fivexfiveoverlap where valnum = 8589934788;"')
    for q in attrqueries:
        do_query(q, true)

#window aggregate queries
windowqueries = []
    windowqueries.append('"select avg(valnum) from twoxtwo fixed window as (partition by i 5 preceding and 5 following, j 5 preceding and 5 following);"');
    windowqueries.append('"select avg(valnum) from twoxtwo fixed window as (partition by i 5 preceding and 5 following, j 5 preceding and 5 following);"');
    windowqueries.append('"select avg(valnum) from twoxtwooverlap fixed window as (partition by i 0 preceding and 10 following, j 0 preceding and 10 following);"');
    windowqueries.append('"select avg(valnum) from twoxtwooverlap fixed window as (partition by i 0 preceding and 10 following, j 0 preceding and 10 following);"');

    windowqueries.append('"select avg(valnum) from threexthree fixed window as (partition by i 3 preceding and 3 following, j 3 preceding and 3 following, k 3 preceding and 3 following);"');
    windowqueries.append('"select avg(valnum) from threexthree fixed window as (partition by i 0 preceding and 6 following, j 0 preceding and 6 following, k 0 preceding and 6 following);"');
    windowqueries.append('"select avg(valnum) from threexthreeoverlap fixed window as (partition by i 3 preceding and 3 following, j 3 preceding and 3 following, k 3 preceding and 3 following);"');
    windowqueries.append('"select avg(valnum) from threexthreeoverlap fixed window as (partition by i 0 preceding and 6 following, j 0 preceding and 6 following, k 0 preceding and 6 following);"');

    windowqueries.append('"select avg(valnum) from fivexfive fixed window as (partition by i 1 preceding and 1 following, j 1 preceding and 1 following, k 1 preceding and 1 following, l 1 preceding and 1 following, m 1 preceding and 1 following);"');
    windowqueries.append('"select avg(valnum) from fivexfive fixed window as (partition by i 0 preceding and 2 following, j 0 preceding and 2 following, k 0 preceding and 2 following, l 0 preceding and 2 following, m 0 preceding and 2 following);"');
    windowqueries.append('"select avg(valnum) from fivexfiveoverlap fixed window as (partition by i 1 preceding and 1 following, j 1 preceding and 1 following, k 1 preceding and 1 following, l 1 preceding and 1 following, m 1 preceding and 1 following);"');
    windowqueries.append('"select avg(valnum) from fivexfiveoverlap fixed window as (partition by i 0 preceding and 2 following, j 0 preceding and 2 following, k 0 preceding and 2 following, l 0 preceding and 2 following, m 0 preceding and 2 following);"');
    for q in windowqueries:
        do_query(q, true)

#group by queries
    groupqueries = []
    groupqueries.append('"select max(valnum) from twoxtwo where j < 10 group by j;"');
    groupqueries.append('"select max(valnum) from twoxtwooverlap where j < 10 group by j;"');
    groupqueries.append('"select max(valnum) from twoxtwo where i < 10 group by i;"');
    groupqueries.append('"select max(valnum) from twoxtwooverlap where i < 10 group by i;"');

    groupqueries.append('"select max(valnum) from threexthree where k < 10 group by k;"');
    groupqueries.append('"select max(valnum) from threexthreeoverlap where k < 10 group by k;"');
    groupqueries.append('"select max(valnum) from threexthree where i < 10 group by i;"');
    groupqueries.append('"select max(valnum) from threexthreeoverlap where i < 10 group by i;"');

    groupqueries.append('"select max(valnum) from fivexfive where m < 10 group by m;"');
    groupqueries.append('"select max(valnum) from fivexfiveoverlap where m < 10 group by m;"');
    groupqueries.append('"select max(valnum) from fivexfive where i < 10 group by i;"');
    groupqueries.append('"select max(valnum) from fivexfiveoverlap where i < 10 group by i;"');
    for q in groupqueries:
        do_query(q, true)

if __name__=='__main__':
    run_tests()
