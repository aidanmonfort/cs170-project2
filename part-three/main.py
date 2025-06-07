from validator import validate
from graphing import graph_subset

def get_stats(dataset):
    instance_count = 0
    feature_count = 0
    with open(dataset, "r") as data:
        instances = data.readlines()
        instance_count = len(instances)

        feature_count = len(instances[0].strip().split()) - 1

    return instance_count, feature_count

def eval(dataset, feature_set):
    return validate(dataset, feature_set)

def forward_selection(dataset, feature_count):
    feature_set = []
    possible_features = set(range(1, feature_count + 1))
    current_accuracy = eval(dataset, feature_set)

    print("Using no features and “random” evaluation, I get an accuracy of:", f"{current_accuracy: .3f}%")

    print("Beginning search.")
    while True:
        if not possible_features:#if we have taken all possible features
            break

        #creates a tuple list of all subsets with one feature added, and scores the accuracy randomly
        next_take = []
        for pf in possible_features:
            new_subset = feature_set + [pf]  # don't mutate in place
            accuracy = validate(dataset, new_subset)
            next_take.append((accuracy, new_subset))

        
        for accuracy, subset in next_take:
            print(f"\tUsing feature(s) {{ {','.join(str(f) for f in subset)} }}, accuracy is {accuracy: .3f}")

        best_accuracy, best_subset = max(next_take)#will grab the best new feature subset using tuple comparison
        if best_accuracy < current_accuracy:
            print("(Warning: Decreased accuracy! )")
            break
        else:
            print(f"Feature set {{ {','.join(str(f) for f in best_subset)} }} was best,",
                  f"accuracy is {best_accuracy: .3f}%")
            
            new_feature = next(f for f in best_subset if f not in feature_set)
            possible_features.remove(new_feature)

            current_accuracy = best_accuracy
            feature_set = best_subset#update to best feature set found

    print(f"Search finished! The best subset of features is {{ {','.join(str(f) for f in feature_set)} }},",
          f"which has an accuracy of {current_accuracy: .3f}%")
    
    return feature_set



def backward_elimination(dataset, feature_count):
    start_features = set(range(1, feature_count + 1))
    current_accuracy = validate(dataset, start_features)

    print("Using all features and “random” evaluation, I get an accuracy of:", f"{current_accuracy: .3f}%")

    while True:
        if not start_features:
            break

        #creates a tuple list of all subsets with one feature removed, and scores the accuracy randomly
        possible_removes = []
        for feature in start_features:
            new_subset = start_features - {feature}
            accuracy = validate(dataset, new_subset)
            possible_removes.append((accuracy, new_subset))

        for accuracy, subset in possible_removes:
            print(f"\tUsing feature(s) {{ {','.join(str(f) for f in subset)} }}, accuracy is {accuracy: .3f}")

        #will grab the best new feature subset using tuple comparison
        best_accuracy, best_subset = max(possible_removes)

        if best_accuracy < current_accuracy:
            print("(Warning: Decreased accuracy! )")
            break
        else:
            print(f"Feature set {{ {','.join(str(f) for f in best_subset)} }} was best,",
                  f"accuracy is {best_accuracy: .3f}%")
            current_accuracy = best_accuracy
            start_features = best_subset#update to new best set

    print(f"Search finished! The best subset of features is {{ {','.join(str(f) for f in start_features)} }},",
          f"which has an accuracy of {current_accuracy: .3f}%")
    
    return start_features

def main():
    print("Welcome to Aidan Monfort and Shaun Mansoor", 
          "Feature Selection Algorithm.")

    print("Type the number of the algorithm you want to run.")

    print("[1] Forward Selection\n", 
          "[2] Backward Elimination\n", sep='')

    algo_choice = int(input())
    dataset = "../small-test-dataset.txt"
    instances_c, feature_count = get_stats(dataset)

    print(f"Dataset has {instances_c} instances and {feature_count} features")

    selected_features = [3, 5, 7]

    # if algo_choice == 1:
    #     selected_features = forward_selection(dataset, feature_count)
    # else:
    #     selected_features = backward_elimination(dataset,feature_count)

    graph_subset(dataset, selected_features)




main()
