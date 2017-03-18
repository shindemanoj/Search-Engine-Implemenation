import re
from collections import defaultdict

import nltk
from bs4 import BeautifulSoup

data = []

# Code to generate clean data from 1000 raw data files
for i in range(1000):
    fr = open("URL" + str(i) + ".txt", "r")
    plain_text = fr.readline()

    # Clean URL Name
    url = plain_text.split('/')
    urlName = url[-1]
    urlName = urlName.replace("-", "")
    urlName = urlName.replace("_", "")
    print(urlName)
    plain_text = fr.readline()

    # Get Soup Object
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

    # Remove
    #
    #
    #
    #  punctuations
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
    # print(text)
    data.append(text)
    urlName = urlName.strip()
    # Create files with clean data in it
    fw = open("CleanData/" + str(urlName) + ".txt", 'w')
    fw.write(text)
    fw.close()

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

uni_gram_index = defaultdict(set)
no_tokens = []

# Create Unigram index
for idx, terms in enumerate(uni_gram_list):
    no_tokens.append(str(idx + 1) + "   " + str(len(terms)))
    for term in terms:
        uni_gram_index[term].add(((idx + 1), (terms.count(term) / len(terms))))

print("Done Unigram Index")

fw = open('UnigramIndex.txt', 'w')
for index in uni_gram_index:
    # print(key, value)
    fw.write(str(index) + "   " + str(uni_gram_index[index]) + "\n")
fw.close()
