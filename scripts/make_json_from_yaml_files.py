import glob
import json
import os

import yaml

yaml_file_paths = sorted(glob.glob("collections/A1/**/*.yaml", recursive=True))

rows_to_write = []
base = ["name", "name_accent", "wordclass", "comment", "usage", "etymology"]
keys = ["base", "translation", "meta", "props"]

for i, yaml_file in enumerate(yaml_file_paths):
    print(
        "Processing file {} of {} file name: {}".format(
            i + 1, len(yaml_file_paths), yaml_file
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

        values = dict()

        base_dict = {}
        props_dict = {}
        meta_dict = {}
        translation_list = []

        for instance in data:
            key = instance
            value = data[instance]
            values["meta"] = meta_dict
            if value:
                if instance == "translation":
                    values["translation"] = value
                elif instance not in base:
                    props_dict.update({key: value})
                    values["props"] = props_dict
                else:
                    base_dict.update({key: value})
                    values["base"] = base_dict
            meta_dict.update({"level": course_name})
            meta_dict.update({"topic": deck_name})

        rows_to_write.append(values)


with open("courses.json", "w") as json_file:
    json.dump(rows_to_write, json_file, ensure_ascii=False)
