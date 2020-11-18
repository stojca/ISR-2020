import sys
import os
import math
import numpy as np
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


print("d) calculate the term frequency tf using different formulas for the word 'information'\n")


def unique_words():

    unique_list = list(set(d1_sorted + d2_sorted + d3_sorted + d4_sorted + d5_sorted))

    print(sorted(unique_list))
    print("Length " + str(len(unique_list)))
    # check number of unique words
    return len(unique_list), sorted(unique_list)


def raw_tf(word, document):
    count_occurence = 0
    for doc_it in document:
        if word in doc_it:
            count_occurence += 1

    return count_occurence

print("-------------------------a---------------------\n")
#d.2
for i, doc in enumerate([d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]):
    print("d2) document " + str(i) + " --> raw tf: " + str(raw_tf("information",  doc)))
print("\n")

print("--------------------------------------------------\n")
print("-------------------------b---------------------\n")

number_of_unique_words, unique_words = unique_words()

m_matrix = np.zeros((number_of_unique_words, 5))

for i, doc in enumerate([d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]):
    for j in range(0, number_of_unique_words):
        word = unique_words[j]
        m_matrix[j, i] = raw_tf(word, doc)

print("matrix: ")
print(m_matrix)

print("transposed matrix mT: ")
print(np.transpose(m_matrix))
print("--------------------------------------------------\n")


print("-------------------------c---------------------\n")

#(20,9), (19,20), (14,22)

print("matrix Cl: ")
matrix_cl = np.dot(m_matrix, np.transpose(m_matrix))
print(matrix_cl)

print(matrix_cl[20, 9])
print(matrix_cl[19, 20])
print(matrix_cl[14, 22])


print("--------------------------------------------------\n")