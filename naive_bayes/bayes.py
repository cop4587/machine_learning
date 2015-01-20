def load_data_set():
    """
    :return: mock posts as list of lists, and classification vector
    """
    posting_list = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    class_vec = [0, 1, 0, 1, 0, 1]

    return posting_list, class_vec


def vocab_list_for(data_set):
    """
    Create vocabulary set for data set(posts, articles, emails, etc.)
    :param data_set: data set as list of lists
    :return: vocabulary as list
    """
    vocab_set = set([])

    for document in data_set:
        vocab_set = vocab_set | set(document)

    return list(vocab_set)


def occurance_vector(vocabulary, input_words):
    result = [0] * len(vocabulary)

    for word in input_words:
        if word in vocabulary:
            result[vocabulary.index(word)] = 1
        else:
            print("the word: %s is not in my vocabulary!" % word)

    return result

