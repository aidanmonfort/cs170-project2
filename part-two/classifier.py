import math
from parser import Parser


class Classifier:
    def __init__(self, dataset):
        self.training_instances = None
        self.dataset = dataset
        self.loader = Parser(dataset)

    def train(self, ids):
        self.training_instances = self.loader.get_subset(ids)

    def test(self, id):
        if self.training_instances is None:
            print("Error! No training data given")
            return

        def euclid_dist(first, second):
            #super clean python one liner
            return math.sqrt(sum((d1 - d2)**2 for d1, d2 in zip(first, second)))

        
        test_instance = self.loader.get_by_id(id)

        assert test_instance is not None
        _, nn_class, nn_id = min((euclid_dist(test_instance[1], 
                                            neighbor[1]), neighbor[0], id) 
                               for id, neighbor in enumerate(self.training_instances))

        return nn_class, nn_id
