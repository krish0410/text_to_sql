import json

def copy_first_n_objects(source_file, destination_file):
    with open(source_file, 'r') as f:
        data = json.load(f)

    # Take the first n objects
    first_n_objects = data[:10]

    with open(destination_file, 'w') as f:
        json.dump(first_n_objects, f, indent=4)

# Example usage
copy_first_n_objects(r'E:\Few-shot-NL2SQL-with-prompting-main\data\dev_original.json', r'E:\Few-shot-NL2SQL-with-prompting-main\data\dev_50.json')
