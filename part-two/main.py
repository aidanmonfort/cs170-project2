import time
from validator import validate

def main():
    dataset_path = r"C:\Users\User\cs170-project2\large-test-dataset.txt"
    features_to_test = [1, 15, 27]

    print("Welcome to Aidan Monfort and Shaun Mansoor",
          "leave one out validation")

    print(f"Dataset: {dataset_path}")
    print(f"Selected features: {features_to_test}")
    
    total_start = time.time()
    
    accuracy = validate(dataset_path, features_to_test, verbose=True)
    
    total_end = time.time()
    total_time = total_end - total_start
    
    print(f"\nTotal runtime for validation: {total_time:.3f} seconds")

if __name__ == "__main__":
    main()