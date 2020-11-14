import sys
import os
import math
from collections import Counter

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

words_combined = d1_sorted + d2_sorted + d3_sorted + d4_sorted + d5_sorted
words_combined = list(dict.fromkeys(words_combined))
print('Words ->', words_combined)

def count_word_in_doc(word):
    words_in_doc = 0
    for doc in [d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]:
        if word in doc:
            words_in_doc += 1
    #print("Word " + ">>"+ word+ "<<" + "repeated in " + str(words_in_doc) + " documents")
    return words_in_doc

def raw_tf(word, document):
    count_occurence = 0
    for doc_it in document:
        if word in doc_it:
            count_occurence += 1

    return count_occurence

def e1(word, doc, N=5.0):
    raw = raw_tf(word, doc)
    ni = float(count_word_in_doc(word))
    lg = math.log(N/ni,2)

    return raw * lg


print("--------------------------------------------------\n")

print("a) Reuse the weights wi,j applying the following formulas and list them (for all 25 words)\n")
print("a1) weights according to a1")

for i, doc in enumerate([d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]):
    sum_of_weights = 0
    for word in words_combined:
        weight = e1(word, doc)
        #sum_of_weights += weight
        #print("doc %s, word %s ----> %f" % (i+1,word ,weight))
    #print('Quadratic sum of weights for a1 -> %f', sum_of_weights*sum_of_weights) 
       


print("--------------------------------------------------\n")
################################################################## a2
def max_word_in_document_real(word, document):
    cnt = Counter(document)

    return max(cnt.values())



def e2(word, doc, N=5):
    raw = raw_tf(word, doc)
    ni = float(count_word_in_doc(word))
    lg = math.log(N/ni,2)

    maxf = float(max_word_in_document_real(word, doc))

    if raw == 0:
        return 0
    return (raw/maxf) * lg


print("\n")
print("a2) weights according to a2")

for i, doc in enumerate([d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]):
    #sum_of_weights = 0
    quadratic_sum = 0
    for word in words_combined:
        weight = e2(word, doc)

        #sum_of_weights += weight
        quadratic_sum += weight*weight
        #print("doc %s, word %s ----> %f" % (i+1,word ,weight))
    print('Quadratic sum of weights for a2 -> %f',quadratic_sum)
########################################################### b1
########################sum(wi,j) / sqrt(sum(wi,j*wi,j))



################################################################# a3
print("\n")
print("a3) weights according to a3")
def e3(word, doc, N=5):
    raw = raw_tf(word, doc)
    ni = float(count_word_in_doc(word))
    lg = math.log(N/ni,2)

    if raw == 0:
        return 0
    return (math.log(raw,2) + 1) * lg


for i, doc in enumerate([d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]):
    sum_of_weights = 0
    quadratic_sum = 0
    for word in words_combined:
        weight = e3(word, doc)

        sum_of_weights += weight
        quadratic_sum += weight*weight
        #print("doc %s, word %s ----> %f" % (i+1,word ,weight))
    #print('Quadratic sum of weights for a3 -> %f',math.sqrt(quadratic_sum))
########################################################### b1
########################sum(wi,j) / sqrt(sum(wi,j*wi,j))




