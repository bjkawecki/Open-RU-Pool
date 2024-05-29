import yaml
import csv
import glob


yaml_file_names = sorted(glob.glob("./output/**/*.yaml", recursive=True))

rows_to_write = []
header = ["count"]

for i, each_yaml_file in enumerate(yaml_file_names):
    print(
        "Processing file {} of {} file name: {}".format(
            i + 1, len(yaml_file_names), each_yaml_file
        )
    )

    with open(each_yaml_file) as file:
        data = yaml.safe_load(file)
        for instance in data:
            header.append(instance) if instance not in header else header

        values = dict()
        values.update({"count": i + 1})
        for instance in data:
            for field in header:
                if instance == field:
                    values.update({field: data[instance]})
        rows_to_write.append(values)

with open("output.csv", "w", newline="") as outcsv:
    writer = csv.DictWriter(outcsv, fieldnames=header)
    writer.writeheader()
    writer.writerows(rows_to_write)
    print("Output file nodes.csv created")
