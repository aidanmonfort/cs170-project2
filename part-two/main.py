from validator import validate
from classifier import Classifier

def main():
    accuracy = validate("../small-test-dataset.txt", {3, 5, 7})
    print(accuracy)


main()
