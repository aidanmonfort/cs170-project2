import math
import numpy as np
from parser import Parser
from collections import Counter


#class to handle training/testing stuff
class Classifier:
    def __init__(self, dataset):
        self.training_instances = None
        self.dataset = dataset
        self.loader = Parser(dataset)
        self.count = self.loader.get_size()
        self.feature_means = None
        self.feature_std = None
        self.most_common_class = None

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
        
        # if no features selected, just store the most common class
        if not feature_list:
            #another nice one liner, counter object with all labels, gets the 1st most common class, 
            #then gets the 0th tuple that has the most common class and frequency, then grabs the class itself
            self.most_common_class = Counter(self.labels).most_common(1)[0][0]
            return
            
        #changed normalization to grab the means for features in the subset
        self.feature_means, self.feature_std = self.loader.get_norms(feature_list)
        self.feature_vectors = self.feature_vectors - self.feature_means 
        self.feature_vectors = self.feature_vectors/self.feature_std

    #tests a specific instance id
    def test_by_id(self, id, k=1):
        # if no features selected, return the most common class
        if not self.feature_list:
            return self.most_common_class
            
        def euclid_dist(first, second):
            #super clean python one liner
            return math.sqrt(sum((d1 - d2)**2 for d1, d2 in zip(first, second)))

        
        _, test_features = self.loader.get_by_id(id, self.feature_list)
        # use stored training statistics for normalization
        test_features = test_features - self.feature_means 
        test_features = test_features/self.feature_std

        #create a list of tuples, with the first entry being the distance, then find one with the smallest distance
        distances = [(euclid_dist(test_features, feature_vec), self.labels[idx], idx) for idx, feature_vec in enumerate(self.feature_vectors)]

        distances.sort()
        k_nearest = distances[:k]
        majority_class = Counter([label for _, label, _ in k_nearest]).most_common(1)[0][0]

        return majority_class

    #tests a specific feature vector
    def test_by_data(self, features, k=1):
        # if no features selected, return the most common class
        if not self.feature_list:
            return self.most_common_class
            
        def euclid_dist(first, second):
            #super clean python one liner
            return math.sqrt(sum((d1 - d2)**2 for d1, d2 in zip(first, second)))

        
        # use stored training statistics for normalization
        features = features - self.feature_means
        features = features/self.feature_std
        
        #another super nice one liner
        #creates tuple list of distance, label, and ids and then uses min function to 
        #return the one with the shortest distance
        distances = [(euclid_dist(features, feature_vec), self.labels[idx], idx) for idx, feature_vec in enumerate(self.feature_vectors)]
        
        distances.sort()
        #grab k nearest neighbors:
        k_nearest = distances[:k]
        majority_class = Counter([label for _, label, _ in k_nearest]).most_common(1)[0][0]

        return majority_class
