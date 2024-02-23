import json

def write_queries_to_txt(json_file, txt_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    with open(txt_file, 'w') as f:
        for entry in data:
            query = entry['query']
            database_name = entry['db_id']
            f.write(f"{query}\t{database_name}\n")

# Example usage
write_queries_to_txt(r'E:\Few-shot-NL2SQL-with-prompting-main\data\dev.json', r'E:\Few-shot-NL2SQL-with-prompting-main\data\gold_10.txt')
