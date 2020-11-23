import numpy as np



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
        if word == doc_it:
            count_occurence += 1

    return count_occurence
print("-------------------------1-----------------------")
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
        #print("word: " + word)
        #print("document: " + str(i))

        m_matrix[j, i] = raw_tf(word, doc)
        #print("count: " + str(raw_tf(word, doc)))

#print("matrix: ")
#print(m_matrix)
#print(m_matrix.shape)

#print("transposed matrix mT: ")
#print(np.transpose(m_matrix))
print("--------------------------------------------------\n")


print("-------------------------c---------------------\n")

#(20,9), (19,20), (14,22)

print("matrix Cl: ")
matrix_cl = np.dot(m_matrix, np.transpose(m_matrix))
#print(matrix_cl)
#print(matrix_cl.shape)
print(matrix_cl[19, 8])
print(matrix_cl[18, 19])
print(matrix_cl[13, 21])

print("--------------------------------------------------\n")
print("-----------------------e-------------------------\n")


#[3,8]
data_index = unique_words.index('data')
information_index = unique_words.index('information')

#data
row_data = matrix_cl[data_index].argsort()
#print("matrix_cl at data index ")
#print(matrix_cl[data_index])
#print(row_data[-1])
#print(row_data[-2])

print("What are the 2 most frequent terms co-occurring with the search term “data”")
print(unique_words[row_data[-1]])
print(unique_words[row_data[-2]])


#information
#print("index " + str(information_index))
row_information = matrix_cl[information_index].argsort()
#print("matrix_cl at information index ")
#print(matrix_cl[information_index])
#print(row_information[-2])
#print(row_information[-3])

print("What are the 2 most frequent terms co-occurring with the search term “information”")
#ignore information as same as search term
print(unique_words[row_information[-2]])
print(unique_words[row_information[-3]])

print("--------------------------------------------------\n")

print("-----------------------2b-------------------------\n")

hyper_index = unique_words.index('hypertext')
similarity = np.dot(matrix_cl[hyper_index],matrix_cl[data_index]) /  (np.linalg.norm(matrix_cl[hyper_index]) * np.linalg.norm(matrix_cl[data_index]))
print("Scalar Clusters: What is the cosine similarity value for the co-occurring terms “data” and “hypertext”? ")
print(similarity)

similarity_2 = np.dot(matrix_cl[hyper_index],matrix_cl[information_index]) /  (np.linalg.norm(matrix_cl[hyper_index]) * np.linalg.norm(matrix_cl[information_index]))
print("Scalar Clusters: What is the cosine similarity value for the co-occurring terms “information” and “hypertext”? ")
print(similarity_2)

def cousine_similarity(word_index_1, word_index_2, matrix_cl):
    similarity = np.dot(matrix_cl[word_index_1],matrix_cl[word_index_2]) /  (np.linalg.norm(matrix_cl[word_index_1]) * np.linalg.norm(matrix_cl[word_index_2]))
    return similarity

temp_matrix = np.zeros((25,25))
for i in range(len(unique_words)):
    for j in range(len(unique_words)):
        temp_matrix[i,j] = cousine_similarity(i,j, matrix_cl)

print(" Scalar Clusters: What are the 2 most frequent terms co-occurring with the search term “data”? ")
temp_result = temp_matrix[data_index].argsort()
print(unique_words[temp_result[-2]])
print(unique_words[temp_result[-3]])


print("Scalar Clusters: What are the 2 most frequent terms co-occurring with the search term “information”? ")
temp_result = temp_matrix[information_index].argsort()
print(unique_words[temp_result[-2]])
print(unique_words[temp_result[-3]])

print("--------------------------------------------------\n")

print("--------------------isr6.11----------------------------\n")
print("--------------------a)----------------------------\n")

