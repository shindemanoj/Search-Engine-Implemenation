from bs4 import BeautifulSoup
from IRparser import remove_punctuation
fr = open("cacm.query.txt", "r")
text = fr.read()
soup = BeautifulSoup(text, 'html.parser')
for docno in soup.find_all("docno"):
    docno.decompose()
soup = soup.find_all(["doc"], recursive=True)


count = 0
query_map = {}
for tag in soup:
    count += 1
    query_string = tag.get_text()
    query_string = query_string.replace("\n", " ")
    query_map[count] = remove_punctuation(query_string.strip())
print(query_map)

fw = open('Queries_CACM.txt', 'w')
for index in query_map:
    # print(key, value)
    fw.write(remove_punctuation(str(query_map[index])) + "\n")
fw.close()