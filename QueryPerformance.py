import sys
import os
import matplotlib.pyplot as plt


# --------------------------------------------------------------#
# made list of rankings
# init

dict_ranking_q1 = {}
dict_ranking_q2 = {}

keys = range(30)
values_q1 = ["d123", "d4711", "d1", "d6", "d11", "d777", "d888", "d878", "d1966", "d909", "d999", "d1504", "d13", "d222", "d19998", "d333",
             "d444", "D8", "d166", "d167", "d212", "d213", "d334", "d55", "d2001", "d2010", "d23", "d3001", "d3002", "d3005"]

values_q2 = ["d4", "d35", "d266", "d255", "d677", "d1", "d1400", "d5001", "d11", "d7555", "d6100", "d133", "d7888", "d2001", "d913", "d3000",
             "d1705", "d555", "d799", "d18877", "d404", "d343", "d23", "d15010", "d2888", "d144", "d7", "d2002", "d9", "d13900"]

for i in (keys):
    dict_ranking_q1[i] = values_q1[i]
    dict_ranking_q2[i] = values_q2[i]


# print(dict_ranking_q1)


def getRecPrec(relevant, value_to_check, debug=False):
    found = 0

    prec = [100]
    rec = [0]
    for idx, val in enumerate(value_to_check):

        if val in relevant:
            found += 1
            p = found / (idx + 1)
            r = found / len(relevant)
            prec.append(p * 100.0)
            rec.append(r * 100.0)

            if debug:
                print("%d -- p %f  r %f" % (len(prec), p, r))

    while len(prec) <= len(relevant):
        prec.append(0)
        rec.append(len(rec) * 100 / len(relevant))

    return rec, prec


def calc_standard_recall(prec, rec):
    import math
    import numpy as np

    # init new array with value from previous
    # use rec values as index, store precision values
    norm_rec = np.zeros(101)

    for i in range(0, len(rec)):
      if i < len(prec):
          print(math.floor(rec[i]))
          norm_rec[math.floor(rec[i])] = prec[i]
    plt.plot(norm_rec, marker='o')
    plt.show()

    for i in range(0, len(norm_rec)):
      norm_rec[i] = max(norm_rec[i:])

    print("standard recall lvl of 40% (list 100) = ", norm_rec[40])
    norm_rec = norm_rec[0:101:10]
    plt.plot(norm_rec, marker='o')
    plt.show()
    print("standard recall lvl of 40%  (list 10) = ", norm_rec[4])
    return norm_rec

print("Test Query 1--------------------------------------------------------------------------------------------------")
relevant_documents_q1 = ["d7", "d23", "d55", "d123", "d888", "d1966", "d4711", "d19999"]

rec_1, prec_1 = getRecPrec(relevant_documents_q1, values_q1, debug=True)

plt.plot(rec_1, prec_1, marker='o')
plt.show()

norm_rec_1 = calc_standard_recall(prec_1, rec_1)


print("Test Query 2--------------------------------------------------------------------------------------------------")
relevant_documents_q2 = ["d1", "d11", "d133", "d255", "d555", "d2001", "d2002", "d2888", "d13900", "d15010", "d18877"]

rec_2, prec_2 = getRecPrec(relevant_documents_q2, values_q2, debug=True)

plt.plot(rec_2, prec_2, marker='o')
plt.show()

norm_rec_2 = calc_standard_recall(prec_2, rec_2)

avg_prec_recall_40 = (norm_rec_1[4] + norm_rec_2[4]) / 2
print("average precision at 40% = ", avg_prec_recall_40)
