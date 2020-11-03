import sys
import os
import math
from collections import Counter

input_file = sys.argv


# b
def count_freq(words_list, word):
    counter = 0
    for sec_w in words_list:
        if word == sec_w:
            counter += 1
    return counter


def max_word_in_document(word):
    cnt = 0
    for arr in [d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]:
        if cnt < count_freq(arr, word):
            cnt = count_freq(arr, word)

    #print("Max Word occuerence " + ">>"+ word +"<<" + " in all documents " + str(cnt))
    return cnt


def max_word_in_document_real(word, document):
    cnt = Counter(document)

    return max(cnt.values())


def count_word_all_doc(word):
    cnt = 0
    for arr in [d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]:
        cnt += count_freq(arr, word)

    return cnt


def count_word_in_doc(word):
    words_in_doc = 0
    for doc in [d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]:
        if word in doc:
            words_in_doc += 1
    #print("Word " + ">>"+ word+ "<<" + "repeated in " + str(words_in_doc) + " documents")
    return words_in_doc


def binary_tf(word, document):
    for doc_it in document:
        if word in doc_it:
            return 1

    return 0

def raw_tf(word, document):
    count_occurence = 0
    for doc_it in document:
        if word in doc_it:
            count_occurence += 1

    return count_occurence

def unique_words():
    #unique_words = set()

    unique_list = list(set(d1_sorted + d2_sorted + d3_sorted + d4_sorted + d5_sorted))

    print(sorted(unique_list))
    print("Length " + str(len(unique_list)))
    # check number of unique words


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

print("Sorted words")

print(unique_words())

print("------------------")

# b Fi
print("b) for information")
print(count_freq(d1_sorted, "information"))
print(count_word_all_doc("information"))
count_word_in_doc("information")
print("b) for hypertext")
print(count_freq(d1_sorted, "hypertext"))
print(count_word_all_doc("hypertext"))
count_word_in_doc("hypertext")

print("------------------")

N = count_word_all_doc("information")
N_hypertext = count_word_all_doc("hypertext")
n_i = count_word_in_doc("information")
n_i_hypertext = count_word_in_doc("hypertext")

id_fi = math.log(5.0/n_i, 2)
id_fi_hypertext = math.log(5.0/n_i_hypertext, 2)
print("information inverse frequency " + str(id_fi))
print("hypertext inverse frequency " + str(id_fi_hypertext))

print("information inverse frequency smooth " + str(math.log(1 + 5.0/n_i, 2)))
print("hypertext inverse frequency smooth " + str(math.log(1 + 5.0/n_i_hypertext, 2)))

max_word_information = max_word_in_document("information")
max_word_hypertext = max_word_in_document("hypertext")
print("information inverse frequency max " + str(math.log(1 + max_word_information/n_i, 2)))
print("hypertext inverse frequency max " + str(math.log(1 + max_word_hypertext/n_i_hypertext, 2)))


#d.1
for i, doc in enumerate([d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]):
    print(str(i) + " document --> binary tf: " + str(binary_tf("information",  doc)))

#d.2
for i, doc in enumerate([d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]):
    print(str(i) + " document --> raw tf: " + str(raw_tf("information",  doc)))

#d.1
normalization = float(float(raw_tf("information",  d1_sorted)) / float(max_word_in_document_real("information", d1_sorted)))
print("1 document --> normalization tf: " + str(normalization))

#d.2
normalization = float(float(raw_tf("information",  d2_sorted)) / float(max_word_in_document_real("information", d2_sorted)))
print("2 document --> normalization tf: " + str(normalization))

#d.5
normalization = float(float(raw_tf("information",  d5_sorted)) / float(max_word_in_document_real("information", d5_sorted)))
print("5 document --> normalization tf: " + str(normalization))

#d.4
normalization = float(float(raw_tf("information",  d5_sorted)) / float(max_word_in_document_real("information", d5_sorted)))
print("5 document --> normalization tf: " + str(normalization))

#d.1
normalization = math.log(raw_tf('information', d2_sorted), 2) + 1
print("1 document --> log normalization tf: " + str(normalization))


def e1(word, doc, N=5.0):
    raw = raw_tf(word, doc)
    ni = float(count_word_in_doc(word))
    lg = math.log(N/ni,2)

    return raw * lg

print("-----------------------")
print("Weights according to e1")

for i, doc in enumerate([d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]):
    weight = e1('information', doc)
    print("doc %s ----> %f" % (i+1, weight))


def e2(word, doc, N=5):
    raw = raw_tf(word, doc)
    ni = float(count_word_in_doc(word))
    lg = math.log(N/ni,2)

    maxf = float(max_word_in_document_real(word, doc))

    if raw == 0:
        return 0
    return (raw/maxf) * lg

print("-----------------------")
print("Weights according to e2")

l = [d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]
for i, doc in enumerate(l):
    weight = e2('information', doc)
    print("doc %s ----> %f" % (i+1, weight))

print("------------------------------")
print("Weights according to e3")

def e3(word, doc, N=5):
    raw = raw_tf(word, doc)
    ni = float(count_word_in_doc(word))
    lg = math.log(N/ni,2)

    if raw == 0:
        return 0
    return (math.log(raw,2) + 1) * lg


for i, doc in enumerate([d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]):
    weight = e3('information', doc)
    print("doc %s ----> %f" % (i+1, weight))


