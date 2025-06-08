import matplotlib.pyplot as plt
import numpy as np
from parser import Parser
from matplotlib.widgets import CheckButtons

def graph_subset(dataset, feature_subset):
    if len(feature_subset) < 2:
        print("Need at least 2 features to create a 2D visualization")
        return
        
    parser = Parser(dataset)
    features_to_plot = list(feature_subset)
    
    labels, features = parser.get_all()
    x_coords = []
    y_coords = []
    z_coords = []
    
    for label, features in zip(labels, features):
        x_coords.append(features[0])
        y_coords.append(features[1])
        if len(feature_subset) >= 3:
            z_coords.append(features[2])
    
    x_coords = np.array(x_coords)
    y_coords = np.array(y_coords)
    z_coords = np.array(z_coords)
    
    if len(feature_subset) >= 3:
        # use 3d instead of 2d
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        unique_labels = np.unique(labels)
        scatter_plots = {}
        for label in unique_labels:
            mask = labels == label
            scatter_plots[label] = ax.scatter(x_coords[mask], y_coords[mask], z_coords[mask], label=f'Class {label}')
        ax.set_xlabel(f'Feature {features_to_plot[0]}')
        ax.set_ylabel(f'Feature {features_to_plot[1]}')
        ax.set_zlabel(f'Feature {features_to_plot[2]}')
        ax.set_title('3D Data Visualization')
        ax.legend()
    else:
        # use 2d instead of 3d
        fig, ax = plt.subplots()
        unique_labels = np.unique(labels)
        scatter_plots = {}
        for label in unique_labels:
            mask = labels == label
            scatter_plots[label] = ax.scatter(x_coords[mask], y_coords[mask], label=f'Class {label}')
        ax.set_xlabel(f'Feature {features_to_plot[0]}')
        ax.set_ylabel(f'Feature {features_to_plot[1]}')
        ax.set_title('Data Visualization')
        ax.legend()
    
    # add checkbuttons for toggling classes
    plt.subplots_adjust(left=0.2)
    rax = plt.axes([0.05, 0.4, 0.1, 0.15])
    check = CheckButtons(rax, [f'Class {label}' for label in unique_labels], [True] * len(unique_labels))
    
    def func(label):
        index = int(label.split()[-1])
        scatter_plots[index].set_visible(not scatter_plots[index].get_visible())
        plt.draw()
    
    check.on_clicked(func)
    plt.ioff()  # Turn off interactive mode to make plt.show() blocking
    plt.show()

def plot_class_distribution(dataset): 
    parser = Parser(dataset)
    labels, _ = parser.get_all()
    
    plt.figure()
    unique, counts = np.unique(labels, return_counts=True)
    plt.bar([f'Class {label}' for label in unique], counts)
    plt.title(dataset[3:])
    plt.xlabel('Class')
    plt.ylabel('Count')
    for i, count in enumerate(counts):
        plt.text(i, count, str(count), ha='center', va='bottom')
    plt.show()

plot_class_distribution("../small-test-dataset.txt")
plot_class_distribution("../large-test-dataset.txt")
plot_class_distribution("../titanic-dataset.txt")
# graph_subset("../small-test-dataset.txt", [3, 5, 7])
# graph_subset("../small-test-dataset.txt", [1, 2, 4])
