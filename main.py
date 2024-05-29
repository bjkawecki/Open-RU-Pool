import yaml
import csv
import glob


yaml_file_names = glob.glob("./a1/*.yaml")

rows_to_write = []
header = ["id"]

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
        values.update({"id": i})
        for instance in data:
            for field in header:
                if instance == field:
                    values.update({field: data[instance]})
        rows_to_write.append(values)

with open("a1.csv", "w", newline="") as outcsv:
    writer = csv.DictWriter(outcsv, fieldnames=header)
    writer.writeheader()
    writer.writerows(rows_to_write)
    print("Output file nodes.csv created")
