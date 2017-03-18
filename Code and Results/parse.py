import operator

from bs4 import BeautifulSoup
import re
from collections import defaultdict
import nltk

data = []
doc_length_map = {}
# Code to generate clean data from 1000 raw data files
for i in range(1000):
    fr = open("URL" + str(i) + ".txt", "r")
    plain_text = fr.readline()
    url = plain_text.split('/')
    urlName = url[-1]
    urlName = urlName.replace("-", "")
    urlName = urlName.replace("_", "")
    print(urlName)
    plain_text = fr.readline()
    soup = BeautifulSoup(plain_text, 'html.parser')

    pageName = soup.find("h1", {"id": "firstHeading"}).get_text()
    pageName = pageName.lower()
    print(pageName + str(i))
    soup = soup.find("div", {"id": "mw-content-text"})
    # Decomposing all unimportant data to get clean data
    if soup.find("ol", {"class": "references"}) is not None:
        soup.find("ol", {"class": "references"}).decompose()

    if soup.find("math") is not None:
        soup.find("math").decompose()

    if soup.find("span", {"id": "See_also"}) is not None:
        soup.find("span", {"id": "See_also"}).decompose()
    if soup.find("span", {"id": "References"}) is not None:
        soup.find("span", {"id": "References"}).decompose()
    if soup.find("span", {"id": "Related_journals"}) is not None:
        soup.find("span", {"id": "Related_journals"}).decompose()

    for a in soup.find_all("a", {"class": "external autonumber"}):
        a.decompose()

    if soup.find("div", {"class": "toc"}) is not None:
        soup.find("div", {"class": "toc"}).decompose()

    for sup in soup.find_all("sup", {"class": "reference"}):
        sup.decompose()

    for span in soup.find_all("span", {"class": "mw-editsection"}):
        span.decompose()

    # Get only relevant data from the soup object
    soup = soup.find_all(["p", "b", "h1", "h2", "h3", "h4", "h5", "h6"], recursive=True)

    text = ""
    tagText = ""
    for tag in soup:
        all_tags = tag.find_all('a')
        for a_tag in all_tags:
            tagText = tagText + " " + a_tag.get_text()
        text = text + " " + tag.get_text()

    text = pageName + tagText + text
    text = text.lower()

    # Remove punctuations
    pattern = re.compile("[x][0-9a-f][0-9a-f]+")
    text = pattern.sub(' ', text)
    text = text.replace(". ", " ")
    text = text.replace(" - ", " ")
    text = text.replace(", ", " ")
    text = text.replace("\\", " ")
    text = text.replace("'", "")
    text = text.replace("'s", "")
    text = re.sub(' +', ' ', text)

    text = (re.sub('[%s]' % '!"#$%&()*+/\:;<=>?@[\\]^_`{|}~', ' ', text))
    # text.decode(encoding='UTF-8', errors='strict')
    #print(text)
    data.append(text)
    urlName = urlName.strip()
    text_array = text.split()
    print(len(text_array))
    doc_length_map[i] = len(text_array)


fw = open('DocumentLength.txt', 'w')
for index in doc_length_map:
    # print(key, value)
    fw.write(str(index) + "   " + str(doc_length_map[index]) + "\n")
fw.close()


'''

# Create unigram list
uni_gram_list = []
for terms in data:
    uni_gram_list.append(nltk.word_tokenize(terms))

fw = open('Unigram.txt', 'w')
for uni in uni_gram_list:
    # print(key, value)
    fw.write(str(uni) + "\n")
fw.close()
print("Done Unigram")

# Create bigram list
bigram_list = []
for terms in data:
    tokens = nltk.word_tokenize(terms)
    list = []
    for i in range(len(tokens) - 1):
        list.append((tokens[i], tokens[i + 1]))
    bigram_list.append(list)

fw = open('Bigram.txt', 'w')
for bi in bigram_list:
    # print(key, value)
    fw.write(str(bi) + "\n")
fw.close()
print("Done Biigram")

# Create Trigram list
trigram_list = []
for terms in data:
    tokens = nltk.word_tokenize(terms)
    list = []
    for i in range(len(tokens) - 2):
        list.append((tokens[i], tokens[i + 1], tokens[i + 2]))
    trigram_list.append(list)

fw = open('Trigram.txt', 'w')
for tri in trigram_list:
    # print(key, value)
    fw.write(str(tri) + "\n")
fw.close()
print("Done Triigram")

uni_gram_index = defaultdict(set)
no_tokens = []

# Create Unigram index
for idx, terms in enumerate(uni_gram_list):
    no_tokens.append(str(idx + 1) + "   " + str(len(terms)))
    for term in terms:
        uni_gram_index[term].add(((idx + 1), (terms.count(term) / len(terms))))

print("Done Unigram Index")

fw = open('NormalisedIndex.txt', 'w')
for index in uni_gram_index:
    # print(key, value)
    fw.write(str(index) + "   " + str(uni_gram_index[index]) + "\n")
fw.close()


bi_gram_index = defaultdict(set)
tri_gram_index = defaultdict(set)
# Create Bigram index
for idx, terms in enumerate(bigram_list):
    for term in terms:
        bi_gram_index[term].add(((idx + 1), terms.count(term)))

print("Done Biigram Index")

# Create Trigram index
for idx, terms in enumerate(trigram_list):
    for term in terms:
        tri_gram_index[term].add(((idx + 1), terms.count(term)))

print("Done Triigram Index")

# Create Term frequency table for Unigram
term_frequency_table_uni = {}
for index in uni_gram_index:
    term_frequency_table_uni[index] = sum([x[1] for x in uni_gram_index[index]])

print("Done term freq Uni")

# Create Term frequency table for Bigram
term_frequency_table_bi = {}
for index in bi_gram_index:
    term_frequency_table_bi[index] = sum([x[1] for x in bi_gram_index[index]])

print("Done term freq Bi")

# Create Term frequency table for Trigram
term_frequency_table_tri = {}
for index in tri_gram_index:
    term_frequency_table_tri[index] = sum([x[1] for x in tri_gram_index[index]])

print("Done term freq Tri")

# Create Doc frequency table for Unigram
doc_frequency_table_uni = {}
for index in uni_gram_index:
    doc_id_list = [x[0] for x in uni_gram_index[index]]
    doc_frequency_table_uni[index] = (doc_id_list, len(doc_id_list))

print("Done Doc freq Uni")

# Create Doc frequency table for Bigram
doc_frequency_table_bi = {}
for index in bi_gram_index:
    doc_id_list = [x[0] for x in bi_gram_index[index]]
    doc_frequency_table_bi[index] = (doc_id_list, len(doc_id_list))
print("Done Doc freq Bi")

# Create Doc frequency table for Trigram
doc_frequency_table_tri = {}
for index in tri_gram_index:
    doc_id_list = [x[0] for x in tri_gram_index[index]]
    doc_frequency_table_tri[index] = (doc_id_list, len(doc_id_list))

print("Done Doc freq Tri")

# Create files for all tables
fw = open('TermFrequencyUni.txt', 'w')
for key, value in sorted(term_frequency_table_uni.items(), key=operator.itemgetter(1), reverse=True):
    # print(key, value)
    fw.write(str(key) + "   " + str(value) + "\n")
fw.close()

fw = open('TermFrequencyBi.txt', 'w')
for key, value in sorted(term_frequency_table_bi.items(), key=operator.itemgetter(1), reverse=True):
    # print(key, value)
    fw.write(str(key) + "   " + str(value) + "\n")
fw.close()


fw = open('TermFrequencyTri.txt', 'w')
for key, value in sorted(term_frequency_table_tri.items(), key=operator.itemgetter(1), reverse=True):
    # print(key, value)
    fw.write(str(key) + "   " + str(value) + "\n")
fw.close()

fw = open('DocFrequencyUni.txt', 'w')
for key, value in sorted(doc_frequency_table_uni.items(), key=operator.itemgetter(0)):
    # print(key, value)
    fw.write(str(key) + "   " + str(value) + "\n")
fw.close()
fw = open('DocFrequencyBi.txt', 'w')
for key, value in sorted(doc_frequency_table_bi.items(), key=operator.itemgetter(0)):
    # print(key, value)
    fw.write(str(key) + "   " + str(value) + "\n")
fw.close()


fw = open('DocFrequencyTri.txt', 'w')
for key, value in sorted(doc_frequency_table_tri.items(), key=operator.itemgetter(0)):
    # print(key, value)
    fw.write(str(key) + "   " + str(value) + "\n")
fw.close()
'''
