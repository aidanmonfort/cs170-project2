def forward_selection():
    pass

def backward_elimination():
    pass

def main():
    print("Welcome to Aidan Monfort and Shaun Mansoor", 
          "Feature Selection Algorithm.")
    
    print("Please enter total number of features:", end='')
    feature_count = input()

    print("Type the number of the algorithm you want to run.")

    print("[1] Forward Selection\n", 
          "[2] Backward Elimination\n", sep='')

    algo_choice = input()

    if algo_choice == 1:
        forward_selection()
    else:
        backward_elimination()

main()
