from math import sqrt

import numpy as np
#Let L(p) be the number of outgoing links of page p
#Let p1. . . pn be the pages that point to page a

outgoing = {1: [7], 2: [7], 3: [7], 4: [8, 9, 10], 5: [8,9,10], 6: [8,9], 7: [11], 8:[], 9:[12], 10:[], 11:[], 12:[]}
ingoing = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [1,2,3], 8:[4,5,6], 9:[4,5,6], 10:[4,5], 11: [7], 12:[9]}

auths = [1] * 12
hubs = [1] * 12


q=0.15
T=12

sum_pr_array_normalized = []
for iteration in range(3):
    print("###########################################################################################")
    print("iteration " + str(iteration + 1))

    initial_value = 1 / T
    print("initial value: " + str(initial_value))


    sum_pr = 0
    sum_pr_array = []

    for outgoing_element in outgoing:
        sum = 0
        if len(ingoing[outgoing_element]) != 0:
            for ingoing_element in ingoing[outgoing_element]:
                if(iteration >= 1):
                    #print("index: " + str(outgoing_element - 1))
                    sum += sum_pr_array_normalized[ingoing_element - 1] / len(outgoing[ingoing_element])
                else:
                    sum += initial_value / len(outgoing[ingoing_element])

        PR_a_normalized = q / T + (1 - q) * sum
        print("document " + str(outgoing_element))
        print("not normalized value " + str(PR_a_normalized))
        sum_pr += PR_a_normalized
        sum_pr_array.append(PR_a_normalized)

    #normalized
    c = 1.0 / sum_pr
    sum_normalized = 0

    sum_pr_array_normalized.clear()
    for index, pr_a in enumerate(sum_pr_array):
        PR_a_normalized = pr_a * float(c)
        sum_pr_array_normalized.append(PR_a_normalized)
        print("document " + str(index + 1))
        print("normalized: ")
        print(PR_a_normalized)
        sum_normalized += PR_a_normalized

    print(sum_pr_array_normalized)
    print("sum of all normalized after " + str(iteration + 1)  +  " iteration " + str(sum_normalized))


