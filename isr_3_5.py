#!/usr/bin/env python3


def check_if_query_satisfied(word_list):
    return (k_a in word_list and k_b in word_list) or \
           (k_a in word_list and k_c in word_list) or \
           (k_a in word_list and k_d not in word_list)

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

k_a = "information"
k_b = "retrieval"
k_c = "science"
k_d = "data"

print("---------- 3.5. CALCULATION: Boolean Model ----------\n\n")
print("document1: " + str(d1_sorted))
print("document2: " + str(d2_sorted))
print("document3: " + str(d3_sorted))
print("document4: " + str(d4_sorted))
print("document5: " + str(d5_sorted))

print("query term k_a: " + k_a + "       query term k_b: " + k_b)
print("query term k_c: " + k_c + "       query term k_d: " + k_d)
print("search query defined as (DNF): q= ka ^ (kb v kc v !kd)")
print("--------------------------------------------------\n")


print("b) Find out or calculate the disjunctive normal form and list all conjunctive components\n")
print("q_DNF = ")
print("ka ^ ( kb v  kc v  kd ) v   [comment: == qcc1]")
print("ka ^ ( kb v  kc v !kd ) v   [comment: == qcc2]")
print("ka ^ ( kb v !kc v  kd ) v   [comment: == qcc3]")
print("ka ^ ( kb v !kc v !kd ) v   [comment: == qcc4]")
print("ka ^ (!kb v  kc v  kd ) v   [comment: == qcc5]")
print("ka ^ (!kb v  kc v !kd ) v   [comment: == qcc6]")
print("ka ^ (!kb v !kc v !kd ) v   [comment: == qcc7]")
print("\n")
print("c(q)_1 = (1,1,1,1)")
print("c(q)_2 = (1,1,1,0)")
print("c(q)_3 = (1,1,0,1)")
print("c(q)_4 = (1,1,0,0)")
print("c(q)_5 = (1,0,1,1)")
print("c(q)_6 = (1,0,1,0)")
print("c(q)_7 = (1,0,0,0)")

print("--------------------------------------------------\n")


print("c) List the document representation for each of the documents applying binary weights.\n")
print("d1 =(1,1,0,0) => qcc4 -> '1'")
print("d1 =(1,1,1,1) => qcc1 -> '1'")
print("d1 =(1,1,1,1) => qcc1 -> '1'")
print("d1 =(1,1,0,1) => qcc3 -> '1'")
print("d1 =(0,0,0,0) => N/A  -> '0'")

print("--------------------------------------------------\n")

print("d) Find out which of the documents satisfy the search query (sim(dj, q))\n")
print("d1 satisfies query: " + str(check_if_query_satisfied(d1_sorted)))
print("d2 satisfies query: " + str(check_if_query_satisfied(d2_sorted)))
print("d3 satisfies query: " + str(check_if_query_satisfied(d3_sorted)))
print("d4 satisfies query: " + str(check_if_query_satisfied(d4_sorted)))
print("d5 satisfies query: " + str(check_if_query_satisfied(d5_sorted)))
print("\n")
