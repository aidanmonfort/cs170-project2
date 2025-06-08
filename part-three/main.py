from validator import validate
from graphing import graph_subset, plot_class_distribution
import time

def get_stats(dataset):
    instance_count = 0
    feature_count = 0
    with open(dataset, "r") as data:
        instances = data.readlines()
        instance_count = len(instances)

        feature_count = len(instances[0].strip().split()) - 1

    return instance_count, feature_count

def eval(dataset, feature_set, k):
    return validate(dataset, feature_set, k)

def forward_selection(dataset, feature_count, k, verbose=True):
    feature_set = []
    possible_features = set(range(1, feature_count + 1))
    current_accuracy = eval(dataset, feature_set, k)

    if verbose:
        print("Using no features and majority class evaluation, I get an accuracy of:", f"{current_accuracy: .3f}%")
        print("Beginning search.")

    while True:
        if not possible_features:#if we have taken all possible features
            break

        #creates a tuple list of all subsets with one feature added, and scores the accuracy randomly
        next_take = []
        for pf in possible_features:
            new_subset = feature_set + [pf]  # don't mutate in place
            accuracy = validate(dataset, new_subset, k)
            next_take.append((accuracy, new_subset))

        
        if verbose:
            for accuracy, subset in next_take:
                print(f"\tUsing feature(s) {{ {','.join(str(f) for f in subset)} }}, accuracy is {accuracy: .3f}")

        best_accuracy, best_subset = max(next_take)#will grab the best new feature subset using tuple comparison
        if best_accuracy < current_accuracy:
            if verbose:
                print("(Warning: Decreased accuracy! )")
            break
        else:
            if verbose:
                print(f"Feature set {{ {','.join(str(f) for f in best_subset)} }} was best,",
                      f"accuracy is {best_accuracy: .3f}%")
            
            new_feature = next(f for f in best_subset if f not in feature_set)
            possible_features.remove(new_feature)

            current_accuracy = best_accuracy
            feature_set = best_subset#update to best feature set found

    if verbose:
        print(f"Search finished! The best subset of features is {{ {','.join(str(f) for f in feature_set)} }},",
              f"which has an accuracy of {current_accuracy: .3f}%")
    
    return feature_set, current_accuracy



def backward_elimination(dataset, feature_count, k, verbose=True):
    start_features = set(range(1, feature_count + 1))
    current_accuracy = validate(dataset, start_features, k)

    if verbose:
        print("Using all features and leave one-out evaluation, I get an accuracy of:", f"{current_accuracy: .3f}%")

    while True:
        if not start_features:
            break

        #creates a tuple list of all subsets with one feature removed, and scores the accuracy randomly
        possible_removes = []
        for feature in start_features:
            new_subset = start_features - {feature}
            accuracy = validate(dataset, new_subset, k)
            possible_removes.append((accuracy, new_subset))

        if verbose:
            for accuracy, subset in possible_removes:
                print(f"\tUsing feature(s) {{ {','.join(str(f) for f in subset)} }}, accuracy is {accuracy: .3f}")

        #will grab the best new feature subset using tuple comparison
        best_accuracy, best_subset = max(possible_removes)

        if best_accuracy < current_accuracy:
            if verbose:
                print("(Warning: Decreased accuracy! )")
            break
        else:
            if verbose:
                print(f"Feature set {{ {','.join(str(f) for f in best_subset)} }} was best,",
                  f"accuracy is {best_accuracy: .3f}%")
            current_accuracy = best_accuracy
            start_features = best_subset#update to new best set

    if verbose:
        print(f"Search finished! The best subset of features is {{ {','.join(str(f) for f in start_features)} }},",
              f"which has an accuracy of {current_accuracy: .3f}%")
    
    return start_features, current_accuracy

def main():
    print("Welcome to Aidan Monfort and Shaun Mansoor", 
          "Feature Selection Algorithm.")

    dataset_set = ["../titanic-dataset.txt"]
    k_values = [1, 3, 5, 7]


    for dataset in dataset_set:
        instances_c, feature_count = get_stats(dataset)
        print(f"Testing for dataset {dataset[3::]}, with {instances_c} instances and {feature_count} features")
        for k in k_values:
            time_start = time.time()
            print(f"\nTesting for k = {k}")
            selected_features = None

            selected_features, accuracy = forward_selection(dataset, feature_count, k, False)
            print(f"\nForward Selection gave feature set {selected_features} with accuracy {accuracy:.3f}")

            # graph_subset(dataset, selected_features)

            selected_features, accuracy = backward_elimination(dataset,feature_count, k, False)
            print(f"Backward Elimination gave feature set {list(selected_features)} with accuracy {accuracy:.3f}")

            time_end = time.time()
            print(f"Time taken: {time_end - time_start:.2f} seconds")

    plot_class_distribution(dataset)




main()
