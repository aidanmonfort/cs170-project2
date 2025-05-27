import random

seed = None

def random_eval():
    if seed is not None:
        random.seed(seed)

    random_percent = random.uniform(0, 100)

    return random_percent


def forward_selection(feature_count):
    feature_set = []
    possible_features = set(range(1, feature_count + 1))
    current_accuracy = random_eval()

    print("Using no features and “random” evaluation, I get an accuracy of:", f"{current_accuracy: .3f}%")

    print("Beginning search.")
    while True:
        if not possible_features:#if we have taken all possible features
            break

        next_take = [(random_eval(), [pf] + feature_set) for pf in possible_features]
        
        for accuracy, subset in next_take:
            print(f"\tUsing feature(s) {{ {','.join(str(f) for f in subset)} }}, accuracy is {accuracy: .3f}")

        best_accuracy, best_subset = max(next_take)#will grab the best new feature subset using tuple comparison
        if best_accuracy < current_accuracy:
            print("(Warning: Decreased accuracy! )")
            break
        else:
            print(f"Feature set {{ {','.join(str(f) for f in best_subset)} }} was best,",
                  f"accuracy is {best_accuracy: .3f}%")
            current_accuracy = best_accuracy
            feature_set = best_subset
            remove_feature = best_subset[0]
            possible_features.remove(remove_feature)

    print(f"Search finished! The best subset of features is {{ {','.join(str(f) for f in feature_set)} }},",
          f"which has an accuracy of {current_accuracy: .3f}%")



def backward_elimination():
    pass

def main():
    print("Welcome to Aidan Monfort and Shaun Mansoor", 
          "Feature Selection Algorithm.")
    
    print("Please enter total number of features:", end='')
    feature_count = int(input())

    print("Type the number of the algorithm you want to run.")

    print("[1] Forward Selection\n", 
          "[2] Backward Elimination\n", sep='')

    algo_choice = int(input())

    if algo_choice == 1:
        forward_selection(feature_count)
    else:
        backward_elimination(feature_count)

main()
