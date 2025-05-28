from classifier import Classifier
from parser import Parser
import time

def validate(dataset, feature_subset=None, verbose=False):
    model = Classifier(dataset)
    parser = Parser(dataset)
    size_i = model.get_size()

    assert size_i is not None
    all = set(range(size_i))
    correct = 0

    if verbose:
        print(f"\nStarting validation on dataset: {dataset}")
        print(f"Using features: {feature_subset if feature_subset else 'ALL'}")
        print(f"Total instances: {size_i}\n")

    for current_test in all:
        loop_start = time.time()

        train_set = all - {current_test}
        model.train(train_set, feature_subset)

        result, _ = model.test_by_id(current_test)
        true_class, _ = parser.get_by_id(current_test, feature_subset)

        if result == true_class:
            correct += 1

        loop_end = time.time()
        if verbose:
            print(f"Instance {current_test+1}: Predicted = {result}, Actual = {true_class}, "
                  f"{'✓' if result == true_class else '✗'}, "
                  f"Time: {loop_end - loop_start:.4f}s")

    accuracy = float(correct) / float(size_i)

    if verbose:
        print(f"\nCorrect predictions: {correct}/{size_i}")
        print(f"Accuracy: {accuracy:.3f}")

    return accuracy
