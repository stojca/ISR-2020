import math
from textblob import TextBlob
from nltk.probability import FreqDist

# we use textblob for word extraction since one would also use existing tools
# when actually doing such tasks
# get textblob by following https://textblob.readthedocs.io/en/dev/

document = ""
with open("gutenberg_file.txt") as infile:
    document += infile.read()

print("5.6 Implementation of text analysis\n")


words = TextBlob(document).words
print("Number of Words", len(words))
distinct_words = set(words)
print("Number of distinct words", len(distinct_words))  # note that this also contains words like 'll, 's, 1, 1.A, 1.B etc
#print(sorted(distinct_words))

print("performing frequency analysis")
fdist = FreqDist(words)
print("displaying the 50 most common words")
fdist_most_common = fdist.most_common(50)
print(fdist_most_common)
fdist.plot(50, cumulative=False)

print("word occurrence distribution")
for i in range(0, 10):
    word_occ = fdist_most_common[i]
    print("word occurence rank", i+1, " of word '", word_occ[0], "' occurrences:", word_occ[1])
    # todo not sure how to calculated word occurrence distribution


word_num_last_10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # [0] = words that appear only once, [1] = words that appear twice ...

for key, value in fdist.items():
    #print(key, value)
    if value < 11:
        word_num_last_10[value-1] += 1

for i in range(0, len(word_num_last_10)):
    print("number of words occurring", i+1, "times:", word_num_last_10[i])



