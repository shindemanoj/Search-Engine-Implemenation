from collections import defaultdict
query_results = {}
relevance_map = defaultdict(set)
fr = open("cacm.rel.txt", "r")
pageLine = fr.readline()
while pageLine != "":
    text = pageLine.split()
    relevance_map[int(text[0])].add(text[2])
    pageLine = fr.readline()
match_count = 0
count = 0
for query_no in relevance_map:
    count += count

    if key in relevance_map[1]:
        match_count += match_count

print(relevance_map)