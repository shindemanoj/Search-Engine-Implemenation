from bs4 import BeautifulSoup
import re

i = 0
data = []
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
print(pageName)
soup = soup.find("div", {"id": "mw-content-text"})
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

soup.find("div", {"class": "toc"}).decompose()

for sup in soup.find_all("sup", {"class": "reference"}):
    sup.decompose()

for span in soup.find_all("span", {"class": "mw-editsection"}):
    span.decompose()


soup = soup.find_all(["p", "b", "h1", "h2", "h3", "h4", "h5", "h6"], recursive=True)

text = ""
tagText = ""
for tag in soup:
    allAtags = tag.find_all('a')
    for tag in allAtags:
        tagText = tagText + " " + tag.get_text()
    text = text + " " + tag.get_text()

#print(tagText)
text = pageName + tagText + text
text = text.lower()

'''def test(args):
    return ''.join([i if ord(i) < 128 else ' ' for i in text])


text = test(text)'''

# text = text.replace("\\", " \\")
# pattern = re.compile("['\\'x[0-9|a-f][0-9|a-f]]+")

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
print(text)
data.append(text)

#print(data)
