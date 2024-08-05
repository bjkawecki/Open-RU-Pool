import yaml
import glob


yaml_file_names = sorted(glob.glob("./collections/**/*.yaml", recursive=True))

rows_to_write = []
header = ["course", "deck"]

for i, yaml_file in enumerate(yaml_file_names):
    print(
        "Processing file {} of {} file name: {}".format(
            i + 1, len(yaml_file_names), yaml_file
        )
    )

    with open(yaml_file) as file:
        data = yaml.safe_load(file)

    if data and "publ_id" in data:
        data.pop("publ_id")

    with open(yaml_file, "w") as file:
        yaml.safe_dump(data, file, allow_unicode=True, sort_keys=False)
