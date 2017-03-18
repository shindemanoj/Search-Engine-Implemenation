from bs4 import BeautifulSoup
import re
import os
from pathlib import Path

try:
    corpus_dir = 'corpus'
    os.mkdir(corpus_dir)
except OSError as err:
    print(err)

try:
    rawtext_dir = 'rawtext'
    os.mkdir(rawtext_dir)
except OSError as err:
    print(err)

doc_count = 0


def write_contents_to_file(dirname,text,name):
    name = name.replace(".html", ".txt")
    f = open(dirname + "/"+ name, "w",  encoding='utf-8')
    f.write(text)
    f.flush()
    f.close()

def write_html_contents_to_rawtext(dirname,text,name):
    name = name.replace(".html",".txt")
    f = open(dirname+ "/"+ name, "w",  encoding='utf-8')
    f.write(text)
    f.flush()
    f.close()



def remove_punctuation(bodytext):
    bodytext = bodytext.lower()
    bodytext = re.sub('[\{!@#$\[%^&*\]()\}+=:,;<>\"`~\|\\\?\/_—]'," ", bodytext)
    bodytext = re.sub('\'', "", bodytext)
    bodytext = re.sub('[-.][ ]|[ ][-.]'," ", bodytext)
    return bodytext


def parser():
    global doc_count
    filelist = os.listdir(r"cacm")
    print("Processing...")
    for doc in filelist:
        if doc.endswith(".html"):
            with open("cacm/"+doc,"r") as f:
                text = f.read()
                soup = BeautifulSoup(text,'html.parser')
                bodytext = soup.find("pre").get_text()
                useful_text = re.split("(CA[0-9]{6})",bodytext)[0]
                write_contents_to_file(rawtext_dir,useful_text, doc)
                useful_text = remove_punctuation(useful_text)
                write_contents_to_file(corpus_dir,useful_text, doc)
                doc_count += 1




