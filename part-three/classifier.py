import math
import numpy as np
from parser import Parser


#class to handle training/testing stuff
class Classifier:
    def __init__(self, dataset):
        self.training_instances = None
        self.dataset = dataset
        self.loader = Parser(dataset)
        self.count = self.loader.get_size()
        self.feature_means = None
        self.feature_std = None

    #returns the size of dataset, probably shouldn't be in this class
    def get_size(self):
        return self.count

    def meanstd(self):
        #had to switch everything to numpy to make this exponentially easier
        feature_means = self.feature_vectors.mean(axis=0)
        feature_std = self.feature_vectors.std(axis=0)

        return feature_means, feature_std


    #trains by just storing important instances in memory, uses the parser class to do this
    def train(self, ids, feature_list=None):
        self.feature_list = feature_list
        self.labels, self.feature_vectors = self.loader.get_subset(ids, feature_list)

        self.feature_means, self.feature_std = self.meanstd() 
        self.feature_vectors = self.feature_vectors - self.feature_means 
        self.feature_vectors = self.feature_vectors/self.feature_std

    #tests a specific instance id
    def test_by_id(self, id):

        def euclid_dist(first, second):
            #super clean python one liner
            return math.sqrt(sum((d1 - d2)**2 for d1, d2 in zip(first, second)))

        
        _, test_features = self.loader.get_by_id(id, self.feature_list)
        # Use stored training statistics for normalization
        test_features = test_features - self.feature_means 
        test_features = test_features/self.feature_std

        _, nn_class, nn_id = min((euclid_dist(test_features, 
                                            feature_vec), self.labels[id], id) 
                               for id, feature_vec in enumerate(self.feature_vectors))

        return nn_class, nn_id

    #tests a specific instance id
    def test_by_data(self, features):

        def euclid_dist(first, second):
            #super clean python one liner
            return math.sqrt(sum((d1 - d2)**2 for d1, d2 in zip(first, second)))

        
        # Use stored training statistics for normalization
        features = features - self.feature_means
        features = features/self.feature_std
        
        #another super nice one liner
        #creates tuple list of distance, label, and ids and then uses min function to 
        #return the one with the shortest distance
        _, nn_class, nn_id = min((euclid_dist(features, 
                                            feature_vec), self.labels[id], id) 
                               for id, feature_vec in enumerate(self.feature_vectors))

        return nn_class, nn_id
