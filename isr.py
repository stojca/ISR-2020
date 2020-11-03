import sys
import os
import math

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



def count_word_all_doc(word):
    cnt = 0
    for arr in [d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]:
        cnt += count_freq(arr, word)

    print("Word " + ">>"+ word +"<<" + " in all documents " + str(cnt))
    return cnt


def count_word_in_doc(word):
    words_in_doc = 0
    for doc in [d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]:
        if word in doc:
            words_in_doc += 1
    print("Word " + ">>"+ word+ "<<" + "repeated in " + str(words_in_doc) + " documents")
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
    print(len(unique_list))
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

# a
print(d1_sorted)
print(d2_sorted)
print(d3_sorted)
print(d4_sorted)
print(d5_sorted)

# b Fi
print(count_freq(d1_sorted, "information"))
print(count_freq(d3_sorted, "data"))
print(count_freq(d5_sorted, "search"))


count_word_all_doc("information")
count_word_all_doc("hypertext")


count_word_in_doc("information")
count_word_in_doc("hypertext")


print("information" in d1_sorted)
print("information" in d2_sorted)
print("information" in d3_sorted)
print("information" in d4_sorted)
print("information" in d5_sorted)

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

#d.3
for i, doc in enumerate([d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]):
    normalization = float(float(raw_tf("information",  doc)) / float(max_word_in_document("information") ))
    print(str(i) + " document --> normalization tf: " + str(normalization))

#d.4
for i, doc in enumerate([d1_sorted, d2_sorted, d3_sorted, d4_sorted, d5_sorted]):
    print(str(i) + " document --> log normalization tf: " + str(math.log(1 + raw_tf("information",  doc), 2)))



unique_words()