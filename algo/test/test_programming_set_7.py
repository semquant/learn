# -*- coding: utf-8 -*-

""" In this programming problem and the next you'll code up the greedy
algorithms from lecture for minimizing the weighted sum of completion times..
Use file [./Jobs.txt]. This file describes a set of jobs with positive and
integral weights and lengths. It has the format

[job_1_weight] [job_1_length]
[job_2_weight] [job_2_length]
...

For example, the third line of the file is "74 59", indicating that the second
job has weight 74 and length 59. You should NOT assume that edge weights or
lengths are distinct.

Your task in this problem is to run the greedy algorithm that schedules jobs in
decreasing order of the difference (weight - length). Recall from lecture that
this algorithm is not always optimal. IMPORTANT: if two jobs have equal
difference (weight - length), you should schedule the job with higher weight
first. Beware: if you break ties in a different way, you are likely to get the
wrong answer. You should report the sum of weighted completion times of the
resulting schedule --- a positive integer --- in the box below.

ADVICE: If you get the wrong answer, try out some small test cases to debug
your algorithm (and post your test cases to the discussion forum)!
"""

import os

#from src.job_scheduling import schedule
#
#
#jobs1 = []
#jobs2 = []
#with open('{base}/test/Jobs.txt'.format(base=os.getcwd()), 'r') as f:
#    key = 1
#    for line in f:
#        [weight, length] = map(int, line.split())
#        jobs1.append([key, weight, length])
#        jobs2.append([key, weight, length])
#        key += 1
#
#output1 = schedule(jobs1, score='diff')
#print '>>>>  diff: ', output1['sum_completion_time']
#
#output2 = schedule(jobs2, score='ratio')
#print '>>>> ratio: ', output2['sum_completion_time']


""" In this programming problem you'll code up Prim's minimum spanning tree
algorithm. Use the text file [./Edges.txt]. This file describes an undirected
graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]
[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
...
For example, the third line of the file is "2 3 -8874", indicating that there
is an edge connecting vertex #2 and vertex #3 that has cost -8874. You should
NOT assume that edge costs are positive, nor should you assume that they are
distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You
should report the overall cost of a minimum spanning tree --- an integer, which
may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn)
time implementation of Prim's algorithm should work fine. OPTIONAL: For those
of you seeking an additional challenge, try implementing a heap-based version.
The simpler approach, which should already give you a healthy speed-up, is to
maintain relevant edges in a heap (with keys = edge costs). The superior
approach stores the unprocessed vertices in the heap, as described in lecture.
Note this requires a heap that supports deletions, and you'll probably need to
maintain some kind of mapping between vertices and their positions in the heap.
"""

#from src.graph import Graph
#from src.minimum_spanning_tree import prims_suboptimal_mst, prims_heap_mst, \
#                              kruskal_suboptimal_mst, kruskal_union_find_mst
#
#
#g = Graph(directed=False)
#
#with open('{base}/test/Edges.txt'.format(base=os.getcwd()), 'r') as f:
#    for line in f:
#        [tail, head, cost] = line.split()
#        g.add_edge((int(tail), int(head), int(cost)))
#
##mst = prims_suboptimal_mst(g)   # -3612829
##mst = prims_heap_mst(g)         # -3611276
##mst = kruskal_suboptimal_mst(g) # -3362091
##mst = kruskal_union_find_mst(g)  # -3362091
#
#cost = 0
#for edge in mst.get_edges():
#    cost += edge[2]
#
#print '>>> cost: ', cost
