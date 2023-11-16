import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f:
        large_list_of_dicts = [row for row in csv.DictReader(f)]

    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(large_list_of_dicts, f, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
