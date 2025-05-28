from validator import validate

def main():
    accuracy = validate("../large-test-dataset.txt", {1, 15, 27})
    print(accuracy)

main()
