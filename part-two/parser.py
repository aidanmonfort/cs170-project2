class Parser:
    def __init__(self, file=None):
        self.file = file

    def translate(self, line, selected_features=None):
        features = []

        label = int(float(line[0]))

        if selected_features is None:
            selected_features = list(range(1, len(line)))

        for f in selected_features:
            features.append(float(line[f]))
        return label, features

    def get_all(self, features=None):
        if self.file is None:
            print("No file data to parse")
            return []

        instances = []
        with open(self.file, "r") as data:
            lines = data.readlines()

            for line in lines:
                line = line.strip().split()

                instances.append(self.translate(line, features))

        return instances

    def get_subset(self, subset, features):
        if self.file is None:
            print("No file data to parse")
            return []

        instances = []
        with open(self.file, "r") as data:
            lines = data.readlines()

            for id in subset:
                line = lines[id].strip().split()

                instances.append(self.translate(line, features))

        return instances

    def get_by_id(self, id, features=None):
        if self.file is None:
            print("No file data to parse")
            return None, []

        lines = []
        with open(self.file, "r") as data:
            lines = data.readlines()

        return self.translate(lines[id].strip().split(), features)

    def get_size(self):
        if self.file is None:
            print("No file data to parse")
            return 0

        lines = []
        with open(self.file, "r") as data:
            lines = data.readlines()

        return len(lines) if lines else 0







