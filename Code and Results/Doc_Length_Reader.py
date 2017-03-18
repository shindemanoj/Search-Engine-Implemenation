doc_len_map = {}
fr = open("doc_len_map.txt", "r")
pageLine = fr.readline()
while pageLine != "":
    text = pageLine.split(":")
    doc_len_map[text[0].strip()] = text[1].strip()
    pageLine = fr.readline()

print(doc_len_map)