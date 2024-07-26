import os
import yaml
import csv
import glob
import json


yaml_file_names = sorted(glob.glob("./output/**/*.yaml", recursive=True))

rows_to_write = []
header = ["course", "deck"]

for i, yaml_file in enumerate(yaml_file_names):
    print(
        "Processing file {} of {} file name: {}".format(
            i + 1, len(yaml_file_names), yaml_file
        )
    )
    directory = os.path.dirname(yaml_file)
    deck_name = os.path.basename(directory)

    deck_directory = os.path.dirname(directory)
    theme_name = os.path.basename(deck_directory)

    course_directory = os.path.dirname(deck_directory)
    course_name = os.path.basename(course_directory)

    with open(yaml_file) as file:
        data = yaml.safe_load(file)
        for instance in data:
            header.append(instance) if instance not in header else header

        values = dict()
        values.update({"course": f"{course_name}", "deck": f"{deck_name[3:]}"})
        for instance in data:
            for field in header:
                if instance == field:
                    values.update({field: data[instance]})
        rows_to_write.append(values)

with open("courses.json", "w") as json_file:
    json.dump(rows_to_write, json_file, ensure_ascii=False)


with open("output.csv", "w") as outcsv:
    writer = csv.DictWriter(
        outcsv, fieldnames=header, delimiter=";", quoting=csv.QUOTE_NONE, escapechar=" "
    )
    writer.writeheader()
    writer.writerows(rows_to_write)
    print("Output file output.csv created")
