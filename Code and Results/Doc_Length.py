import glob
import os

path = 'corpus'
doc_length_map = {}

for filename in glob.glob(os.path.join(path, '*.txt')):
    fr = open(filename, "r")
    filename = filename.replace(".txt", "")
    text = fr.read()
    text = text.replace("\n", " ")
    text = text.strip()
    text_array = text.split()
    print(len(text_array))
    doc_length_map[filename] = len(text_array)

fw = open('DocumentLengthCACM.txt', 'w')
for index in doc_length_map:
    # print(key, value)
    fw.write(str(index) + "   " + str(doc_length_map[index]) + "\n")
fw.close()