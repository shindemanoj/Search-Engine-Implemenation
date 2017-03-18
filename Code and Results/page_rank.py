import math
import operator

graph = {}
outlink_count_map = {}
sink_node_set = set()


# Get first column from each line of file
def getFirstColumn(page):
    page_array = page.split()
    return page_array[0]


# Build OutlinkMap which will contain page and its outlink count
# and SinkSet which will contain sink pages
def buildOutlinkMapAndSinkSet():
    for p in graph.keys():
        outlink_count_map[p] = 0

    for page in graph:
        for inlink in graph[page]:
            outlink_count_map[inlink] += 1

    for page in outlink_count_map:
        if outlink_count_map[page] == 0:
            sink_node_set.add(page)


# Get inlinks of inout page
def getInlinks(page):
    inlinks = page.split()
    inlinks.remove(getFirstColumn(page))
    return inlinks


# Read input file
def readFile():
    fr = open("G2.txt", "r")
    #fr = open("G1.txt", "r")
    # fr = open("Toy.txt", "r")
    pageLine = fr.readline()
    while pageLine != "":
        graph[getFirstColumn(pageLine)] = getInlinks(pageLine)
        pageLine = fr.readline()


fw = open('G2_Perplexity.txt', 'w')
#fw = open('G1_Perplexity.txt', 'w')


# fw = open('Toy_Perplexity.txt', 'w')

# Function for PageRank Algorithm
def findPageRank(graph, outlinks_count_map, sink, damping=0.85):
    N = len(graph.keys())
    ranks = {}
    new_ranks = {}
    entropy = 0
    perplexity = 0
    count = 0

    for node in graph.keys():
        ranks[node] = 1 / N  # initial value

    while count < 4:
        sinkPR = 0
        for page in sink:
            sinkPR += ranks[page]  # Calculate total sinkPR

        for page in graph:
            new_ranks[page] = (1 - damping) / N  # teleportation
            new_ranks[page] += damping * sinkPR / N  # spread remaining sinkPR evenly

            for inlink in graph[page]:  # pages pointing to p
                new_ranks[page] += damping * ranks[inlink] / outlinks_count_map[inlink]  # add share of PageRank from in-links

        for page in graph:
            ranks[page] = new_ranks[page]

        for page in graph:
            entropy += (ranks[page] * math.log(ranks[page], 2))

        entropy = - entropy
        new_perplexity = (2 ** entropy)
        entropy = 0
        fw.write(str(new_perplexity) + '\n')

        if (new_perplexity - perplexity) < 1:
            count += 1
        else:
            count = 0

        perplexity = new_perplexity

    return ranks


readFile()
buildOutlinkMapAndSinkSet()
# Call function to get doc_vector_list ranks
final_ranks = findPageRank(graph, outlink_count_map, sink_node_set)
fw.close()
#fw = open('G1_Top50_Ranks.txt', 'w')
fw = open('G2_Top50_Ranks.txt', 'w')
#fw = open('Toy_Ranks.txt', 'w')

# Create file to store pages with its rank in descending order
for key, value in sorted(final_ranks.items(), key=operator.itemgetter(1), reverse=True):
    # print(key, value)
    fw.write(str(key) + "   " + str(value) + "\n")

fw.close()

# fw = open('Sink_Nodes_Toy.txt', 'w')
#fw = open('G1_Sink_Nodes.txt', 'w')
fw = open('G2_Sink_Nodes.txt', 'w')

# Create file to store pages with its rank in descending order
for node in sorted(sink_node_set):
    fw.write(str(node) + "\n")
fw.write("\n \n" + str(len(sink_node_set)))
fw.close()

# Create file to store sources
# fw = open('Sources_Toy.txt', 'w')
#fw = open('G1_Sources.txt', 'w')
fw = open('G2_Sources.txt', 'w')
for page in graph:
    if not graph[page]:
        fw.write(str(page) + "\n")

fw.close()

# Create file to store page and its Inlinks count
#fw = open('G1_Inlinks_Count.txt', 'w')
fw = open('G2_Inlinks_Count.txt', 'w')
inlink_count_map = {}
for page in graph:
    inlink_count_map[page] = len(graph[page])

for key, value in sorted(inlink_count_map.items(), key=operator.itemgetter(1), reverse=True):
    # print(key, value)
    fw.write(str(key) + "   " + str(value) + "\n")
fw.close()
