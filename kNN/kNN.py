from numpy import *
import operator


def create_data_set():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def distances(in_x, data_set):
    """
    :param in_x: Input vector
    :param data_set: Training samples
    :return:
    """
    data_set_size = data_set.shape[0]
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    return sq_distances ** 0.5


def classify0(in_x, data_set, labels, k):
    """
    :param in_x: Input vector
    :param data_set: Training samples
    :param labels: Label vector
    :param k: Number of the nearest neighbors
    :return:
    """
    dist = distances(in_x, data_set)
    sorted_dist_indices = dist.argsort()

    class_count = {}

    for i in range(k):
        vote_label_i = labels[sorted_dist_indices[i]]
        class_count[vote_label_i] = class_count.get(vote_label_i, 0) + 1

    sorted_class_count = sorted(class_count.iteritems(),
                                key=operator.itemgetter(1),  # sort by 2nd item (count)
                                reverse=True)
    return sorted_class_count[0][0]
