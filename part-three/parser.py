import numpy as np


class Parser:
    #parser class to handle grabbing data from a file and returning instances
    def __init__(self, file=None):
        self.file = file

    #takes a line a makes an instance
    def translate(self, line, selected_features=None):
        features = []

        #grabs label from first column
        label = int(float(line[0]))

        #defaults to all features
        if selected_features is None:
            selected_features = range(1, len(line))

        #grabs columns from selected features and converts to floats
        for f in selected_features:
            features.append(float(line[f]))
        return label, np.array(features)

    #grabs all instances from a file, for a feature subset(if wanted)
    def get_all(self, features=None):
        if self.file is None:
            print("No file data to parse")
            return []

        label_array = []
        feature_array = []
        with open(self.file, "r") as data:
            lines = data.readlines()

            for line in lines:
                line = line.strip().split()#take newline off and split by spaces
                
                label, feature_vec = self.translate(line, features)
                label_array.append(label)
                feature_array.append(feature_vec)

        return np.array(label_array), np.array(feature_array)

    #grabs a subset of instances by ids and by feature subset, if wanted
    def get_subset(self, subset, features=None):
        if self.file is None:
            print("No file data to parse")
            return []

        label_array = []
        feature_array = []
        with open(self.file, "r") as data:
            lines = data.readlines()

            for id in subset:
                line = lines[id].strip().split()

                label, feature_vec = self.translate(line, features)
                label_array.append(label)
                feature_array.append(feature_vec)

        return np.array(label_array), np.array(feature_array)

    #grabs one instance with a specific id, returns a tuple of the label and features
    def get_by_id(self, id, features=None):
        if self.file is None:
            print("No file data to parse")
            return None, []

        lines = []
        with open(self.file, "r") as data:
            lines = data.readlines()

        return self.translate(lines[id].strip().split(), features)

    #returns the number of instances in the dataset
    def get_size(self):
        if self.file is None:
            print("No file data to parse")
            return 0

        lines = []
        with open(self.file, "r") as data:
            lines = data.readlines()

        return len(lines) if lines else 0
    
    def get_norms(self, feature_list=None):
        if self.file is None:
            print("No file data to parse")
            return []
        
        _, features = self.get_all(feature_list)
        # get mean and std along columns
        return features.mean(axis=0), features.std(axis=0)







