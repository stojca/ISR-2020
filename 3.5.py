import sys
import os
import math
from collections import Counter

import matplotlib.pyplot as plt
 
from matplotlib_venn import venn2


d1 = "information retrieval introduction information retrieval model searching browsing search brows"

d2 = "information retrieval data retrieval retrieval mechanism information science user interface ranking relevance"

d3 = "data information knowledge information retrieval information science relevance feedback information retrieval history"

d4 = "search service hypertext data retrieval model information need"

d5 = "search service search engine meta search catalogue search service portal"

d1_sorted = sorted(d1.split(" "))
d2_sorted = sorted(d2.split(" "))
d3_sorted = sorted(d3.split(" "))
d4_sorted = sorted(d4.split(" "))
d5_sorted = sorted(d5.split(" "))

ka = information
kb = retrieval
kc = science
kd = data

v = venn3(subsets=(1,1,0,1,0,0,0))
v.get_label_by_id('100').set_text('First')
v.get_label_by_id('010').set_text('Second')
v.get_label_by_id('001').set_text('Third')
plt.title("Not a Venn diagram")
plt.show()

#(DNF): q= ka ^ (kb v kc v !kd)