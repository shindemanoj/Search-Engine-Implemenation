import re

docid = 0

fr = open("cacm_stem.txt", "r")
page_text = ""
useful_text = ""
pageLine = fr.readline()
stem_corpus_map = {}
while pageLine != "":
    text = pageLine.split()
    if text[0] is "#":
        if page_text is not "":
            useful_text = re.split("(ca[0-9]{6})", page_text)[0]
            stem_corpus_map[docid] = useful_text
        docid += 1
        page_text = ""
    else:
        page_text += pageLine.replace("\n", "")
    pageLine = fr.readline()
print(stem_corpus_map)

for docid in stem_corpus_map:
    if len(str(docid)) == 1:
        fileName = "CACM-000" + str(docid) + ".txt"
    elif len(str(docid)) == 2:
        fileName = "CACM-00" + str(docid) + ".txt"
    elif len(str(docid)) == 2:
        fileName = "CACM-0" + str(docid) + ".txt"
    else:
        fileName = "CACM-" + str(docid) + ".txt"
    fw = open(fileName, 'w')
    fw.write(str(stem_corpus_map[docid]))
    fw.close()
