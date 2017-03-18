import ast
from collections import defaultdict
import operator
import math


# Main Function which takes input as query and gives output as map of document scores
def findCosineSim(query):
    # query1 = "global warming potential"
    # query2 = "green power renewable energy"
    # query3 = "solar energy california"
    # query4 = "light bulb bulbs alternative alternatives"

    # Read Unigram Index file
    fr = open("UnigramIndex.txt", "r")
    pageLine = fr.readline()
    while pageLine != "":
        text = pageLine.split("   ")
        uni_gram_index[text[0]] = text[1].strip()
        pageLine = fr.readline()

    # Make array of query terms
    query_array_wid_dup = query.split()
    query_set = set()
    query_array = []
    for value in query_array_wid_dup:
        if value not in query_set:
            query_array.append(value)
            query_set.add(value)

    print("Query terms Array:  " + str(query_array))

    # Find query term frequency
    for term in query_array_wid_dup:
        query_term_freq[term] = (query_array_wid_dup.count(term))
    print("Query terms Frequency:  " + str(query_term_freq))

    # Create doc tf*idf list based on the each term in query
    doc_set = set()
    for index in query_array:
        doc_tf_idf = {}
        if uni_gram_index[index]:
            uni_gram_index[index] = ast.literal_eval(uni_gram_index[index])
        for x in uni_gram_index[index]:
            # Find tf*idf value for document
            doc_tf_idf[x[0]] = (1.0 + math.log(float(x[1]), 10)) * (
                math.log(float(1000) / len(uni_gram_index[index]), 10))
            doc_set.add(x[0])
        doc_tf_idf_list.append(doc_tf_idf)

    print("Document tf*idf List based on term:  " + str(doc_tf_idf_list))
    print("Document Set:  " + str(doc_set))

    # Create document vector list
    doc_vector_list = []
    for doc_id in doc_set:
        doc_vector = []
        for doc_map in doc_tf_idf_list:
            if doc_id in doc_map:
                doc_vector.append(doc_map[doc_id])
            else:
                doc_vector.append(0.0)
        doc_vector.append(doc_id)
        doc_vector_list.append(doc_vector)

    print("Document Vector List:  " + str(doc_vector_list))

    # Create Query Vector
    for term in query_array:
        if uni_gram_index[term]:
            # Find tf*idf value for query terms
            query_vector.append((1.0 + math.log(float(query_term_freq[term]), 10)) * (
                math.log(float(1000) / len(uni_gram_index[term]), 10)))
        else:
            query_vector.append(0.0)

    print("Query Vector:  " + str(query_vector))

    result = {}

    # Function which calculates Cosine similarity between given two vectors
    def get_cosine(vector1, vector2):
        # Find Numerator value of Cosine formula
        numerator = sum([term * vector2[idx] for idx, term in enumerate(vector1)])

        # Find denominator value of Cosine formula
        sum1 = sum([x ** 2 for x in vector1])
        sum2 = sum([x ** 2 for x in vector2])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator

    # Get Vector of each document and call get_cosine function with query vector
    for doc_vector in doc_vector_list:
        doc_id = doc_vector.pop()
        result[doc_id] = get_cosine(doc_vector, query_vector)

    return result


query = ""
q = 0
while query != "q":

    # Initialize all the variables
    idf_map_query = {}
    query_term_freq = {}
    query_vector = []
    doc_tf_idf_list = []
    uni_gram_index = defaultdict(set)

    # Get query input from user
    query = input("Enter Query (q = quit): ")
    q += 1
    if query != "q":
        # Get results calling findCosineSim Function
        result = findCosineSim(query)
        count = 0
        # Write results to file in descending order based on document score
        fw = open("CosineQ" + str(q) + ".txt", 'w')
        for key, value in sorted(result.items(), key=operator.itemgetter(1), reverse=True):
            count += 1
            print(key, value)
            fw.write("query_" + str(q) + "   " + "Q0   " + str(key) + "   " + str(count) + "   " + str(
                value) + "   " + "system_NEU" + "\n")
            if count == 100:
                break
        fw.close()

k1 = 1.2
k2 = 100
b = 0.75
R = 0.0


def score_BM25(n, f, qf, r, N, dl, avdl):
    K = compute_K(dl, avdl)
    first = math.log(((r + 0.5) / (R - r + 0.5)) / ((n - r + 0.5) / (N - n - R + r + 0.5)))
    second = ((k1 + 1) * f) / (K + f)
    third = ((k2 + 1) * qf) / (k2 + qf)
    return first * second * third


def compute_K(dl, avdl):
    return k1 * ((1 - b) + b * (float(dl) / float(avdl)))

score = score_BM25(n=len(doc_dict), f=freq, qf=1, r=0, N=len(self.dlt),
									   dl=self.dlt.get_length(docid), avdl=self.dlt.get_average_length()) # calculate score

