import numpy as np
import math
documents = []
with open('test1.txt') as f:
    content = ''
    for line in f:
        content = line.split()
        documents.append(content)

def normalize(input_matrix):
    """
    Normalizes the rows of a 2d input_matrix so they sum to 1
    """

    row_sums = input_matrix.sum(axis=1)
    try:
        assert (np.count_nonzero(row_sums)==np.shape(row_sums)[0]) # no row should sum to zero
    except Exception:
        raise Exception("Error while normalizing. Row(s) sum to zero")
    new_matrix = input_matrix / row_sums[:, np.newaxis]
    return new_matrix

unique = []
for doc in documents:
    for word in doc:
        unique.append(word)

docCount = 0
wordCount = 0
a = [ [0]*len(unique) for i in [0]*len(documents)]
for doc in documents:
    for word in unique:
        currCount = doc.count(word)
        a[docCount][wordCount] = doc.count(word)
        wordCount = wordCount + 1
    wordCount = 0
    docCount = docCount + 1

document_topic_prob = np.random.random_sample((len(documents), 5))
document_topic_prob = normalize(document_topic_prob)
print(document_topic_prob)