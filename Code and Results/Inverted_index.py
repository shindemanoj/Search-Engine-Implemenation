from collections import defaultdict
import nltk
import matplotlib.pyplot as plt
import operator
text = "test test test4 test1 test2 test3 test1"
text1 = "test test4 test5 test6 test test4 test a"

# data contains all data of files in the form of list
data = [text, text1]
uni_gram_list = []

for terms in data:
    uni_gram_list.append(nltk.word_tokenize(terms))

bigram_list = []


for terms in data:
    tokens = nltk.word_tokenize(terms)
    list = []
    for i in range(len(tokens) - 1):
        list.append((tokens[i], tokens[i + 1]))
    bigram_list.append(list)

trigram_list = []


for terms in data:
    tokens = nltk.word_tokenize(terms)
    list = []
    for i in range(len(tokens) - 2):
        list.append((tokens[i], tokens[i + 1], tokens[i + 2]))
    trigram_list.append(list)

print(uni_gram_list)
print(bigram_list)
print(trigram_list)

uni_gram_index = defaultdict(set)
bi_gram_index = defaultdict(set)
tri_gram_index = defaultdict(set)

for idx, terms in enumerate(uni_gram_list):
    for term in terms:
        uni_gram_index[term].add(((idx + 1), terms.count(term)))

for idx, terms in enumerate(bigram_list):
    for term in terms:
        bi_gram_index[term].add(((idx + 1), terms.count(term)))

for idx, terms in enumerate(trigram_list):
    for term in terms:
        tri_gram_index[term].add(((idx + 1), terms.count(term)))

print(uni_gram_index)
print(bi_gram_index)
print(tri_gram_index)

term_frequency_table_uni = {}
for index in uni_gram_index:
    term_frequency_table_uni[index] = sum([x[1] for x in uni_gram_index[index]])

term_frequency_table_bi = {}
for index in bi_gram_index:
    term_frequency_table_bi[index] = sum([x[1] for x in bi_gram_index[index]])

term_frequency_table_tri = {}
for index in tri_gram_index:
    term_frequency_table_tri[index] = sum([x[1] for x in tri_gram_index[index]])

print(term_frequency_table_uni)
print(term_frequency_table_bi)
print(term_frequency_table_tri)

doc_frequency_table_uni = {}
for index in uni_gram_index:
    doc_id_list = [x[0] for x in uni_gram_index[index]]
    doc_frequency_table_uni[index] = (doc_id_list, len(doc_id_list))

doc_frequency_table_bi = {}
for index in bi_gram_index:
    doc_id_list = [x[0] for x in bi_gram_index[index]]
    doc_frequency_table_bi[index] = (doc_id_list, len(doc_id_list))

doc_frequency_table_tri = {}
for index in tri_gram_index:
    doc_id_list = [x[0] for x in tri_gram_index[index]]
    doc_frequency_table_tri[index] = (doc_id_list, len(doc_id_list))

print(doc_frequency_table_uni)
print(doc_frequency_table_bi)
print(doc_frequency_table_tri)
list = []
for term in term_frequency_table_bi:
    list.append(term_frequency_table_bi[term])

#fw = open('TermFrequency.txt', 'w')
for key, value in sorted(term_frequency_table_uni.items(), key=operator.itemgetter(0), reverse=True):
    print(key, value)
    #fw.write(str(key) + "   " + str(value) + "\n")
#fw.close()

plt.plot(sorted(term_frequency_table_bi.values(), reverse=True))
plt.ylabel('some numbers')
plt.show()