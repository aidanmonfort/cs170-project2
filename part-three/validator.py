from tqdm import tqdm
from classifier import Classifier
from parser import Parser


def validate(dataset, feature_subset=None):
    model = Classifier(dataset)
    parser = Parser(dataset)
    size_i = model.get_size()

    assert size_i is not None
    all = set(range(size_i))
    correct = 0
    for current_test in all:
        train_set = all - {current_test}
        print(train_set)
        model.train(train_set, feature_subset)


        true_class, features = parser.get_by_id(current_test, feature_subset)

        result, _ = model.test_by_data(features)

        if result == true_class:
            correct += 1

    return float(correct)/float(size_i)
