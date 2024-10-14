import glob
import json
import os

import yaml

yaml_file_paths = sorted(glob.glob("collections/A2/**/*.yaml", recursive=True))
words_without_translation = []


for i, yaml_file in enumerate(yaml_file_paths):
    print(
        "Processing file {} of {} file name: {}".format(
            i + 1, len(yaml_file_paths), yaml_file
        )
    )

    with open(yaml_file) as file:
        data = yaml.safe_load(file)

        if "translation" not in data:
            words_without_translation.append(data["name"])
print(words_without_translation)
