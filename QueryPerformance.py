import sys
import os
import matplotlib.pyplot as plt


#--------------------------------------------------------------#
#made list of rankings
#init

dict_ranking_q1 = {}
dict_ranking_q2 = {}

keys = range(30)
values_q1 = ["d123", "d4711", "d1", "d6", "d11", "d777", "d888", "d878", "d1966", "d909", "d999", "d1504", "d13", "d222", "d19998", "d333",
             "d444", "D8", "d166", "d167", "d212", "d213", "d334", "d55", "d2001", "d2010", "d23", "d3001", "d3002", "d3005"]

values_q2 = ["d4", "d35", "d266", "d255", "d677", "d1", "d1400", "d5001", "d11", "d7555", "d6100", "d133", "d7888", "d2001", "d913", "d3000",
             "d1705", "d555", "d799", "d18877", "d404", "d343", "d23", "d15010", "d2888", "d144", "d7", "d2002", "d9", "d13900"]

for i in (keys):
    dict_ranking_q1[i] = values_q1[i]
    dict_ranking_q2 [i] = values_q2[i]

#print(dict_ranking_q1)


print("Test Query 1--------------------------------------------------------------------------------------------------")

#Test query 1 (Q1):
#Relevant documents {d7, d23, d55, d123, d888, d1966, d4711, d19999}

relevant_documents_q1 = ["d7","d23","d55", "d123", "d888", "d1966", "d4711", "d19999"]
precisions = []
recalls = []

found = 1
for document in relevant_documents_q1:


    for document_ranking, document_name in dict_ranking_q1.items():
        #print("1 " + document)
        #print("2 " + str(document_ranking))
        precision_sum = 0

        if document == document_name:
            print("document: " + document)
            recall = found / len(relevant_documents_q1)
            precission = found / (document_ranking + 1)
            precisions.append(precission)
            recalls.append(recall)
            print("recall: ")
            print(recall)

            print("precission: ")
            print(precission)
            found += 1
if ((found - 1) != len(relevant_documents_q1)):
    print("precission: 0")
    precission = 0
    precisions.pop()
    precisions.append(0)
else:
    print("precission: ")
    print(precission)

print("Test Query 2--------------------------------------------------------------------------------------------------")
print("Precisions")
print(precisions)
print("Recalls")
print(recalls)

plt.plot(precisions, recalls)
plt.show()


#Test query 2 (Q2):
#Relevant documents {d1, d11, d133, d255, d555, d2001, d2002, d2888, d13900, d15010, d18877 }
relevant_documents_q2 = ["d1","d11","d133", "d255", "d555", "d2001", "d2002", "d2888", "d13900", "d15010", "d18877"]

precisions.clear()
recalls.clear()
found = 1
for document in relevant_documents_q2:


    for document_ranking, document_name in dict_ranking_q2.items():
        #print("1 " + document)
        #print("2 " + str(document_ranking))
        precision_sum = 0

        if document == document_name:
            print("document: " + document)
            recall = found / len(relevant_documents_q2)
            precission = found / (document_ranking + 1)
            precisions.append(precission)
            recalls.append(recall)
            print("recall: ")

            print(recall)
            print("precission: ")

            print(precission)
            found += 1


if ((found - 1) != len(relevant_documents_q2)):
    print("precission: 0")
    precisions.pop()
    precisions.append(0)
    #precission = 0
else:
    print("precission: ")
    print(precission)


plt.plot(precisions, recalls)
plt.show()


########################################### b)

standard_recall_levels = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]