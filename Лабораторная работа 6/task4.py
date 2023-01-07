import json

INPUT_FILE = "input_new.csv"


def csv_to_list_dict(file_in, a='\n', b=',') -> list[dict]:  # TODO реализовать конвертер из csv в json
    with open(file_in) as file:
        lines = file.read().split(a)
        row = [i.split(b) for i in lines]
        list_d = [dict(zip(row[0], row[i])) for i in range(1, len(lines))]
    return list_d


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
