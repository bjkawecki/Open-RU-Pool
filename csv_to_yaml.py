import os
import csv
import yaml
import ruamel.yaml as ruyml

from utils.unaccentify import unaccentify
from utils.enum import wordclasses


if __name__ == "__main__":

    with open("data/course_a1.csv") as course:
        reader = csv.DictReader(course)

        for row in reader:
            theme = row["theme"]
            deck = row["deck_name"]
            name_ac = row["word_name"]
            name = unaccentify(row["word_name"])
            wordclass_id = int(row["word_class"])
            wordclass = str()
            for key in wordclasses:
                if wordclass_id == key:
                    wordclass = wordclasses[key]

            PATH = f"./a1/{theme}/{deck}"
            os.makedirs(PATH, exist_ok=True)
            dataMap = dict()
            wordclass_template = f"./templates/{wordclass}.yaml"

            with open(wordclass_template, "r") as template:
                dataMap = yaml.safe_load(template)
                dataMap["name"] = name
                dataMap["name_ac"] = name_ac
                dataMap["wordcls"] = wordclass

            with open(f"{PATH}/{name}.yaml", "w") as template:

                ruyaml = ruyml.YAML()
                ruyaml.indent(sequence=4, offset=3)
                ruyaml.dump(dataMap, template)
