import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    rows = []
    fields = []
    with open(INPUT_FILENAME, newline='') as file:
        temp = csv.reader(file)
        fields = next(temp)

        for i in temp:
            rows.append(i)

    large_list_of_dicts = []
    for i in range(0, len(rows)):
        tempdict = {}
        for j in range(0, len(fields)):
            tempdict[fields[j]] = rows[i][j]
        large_list_of_dicts.append(tempdict)

    jsonstring = json.dumps(large_list_of_dicts, indent=4)

    with open(OUTPUT_FILENAME, "w") as json_file:
        json_file.write(jsonstring)



if __name__ == '__main__':

    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
