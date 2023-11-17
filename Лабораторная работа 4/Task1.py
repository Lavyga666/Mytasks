import json

def task() -> float:
    with open('input.json') as file:
        parse_json_dict = json.load(file)
    sum = 0
    for temp in parse_json_dict:
        sum += temp['score'] * temp['weight']
    return round(sum, 3);

print(task())
