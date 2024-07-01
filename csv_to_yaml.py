import os
import csv
import yaml
import ruamel.yaml as ruyml

from utils.unaccentify import unaccentify
from utils import enums
from utils.headers import headers, translations
from utils.parse_headers import parse_headers, parse_translations

if __name__ == "__main__":

    with open("data/course_a1.csv") as course:
        reader = list(csv.DictReader(course))

        for i, row in enumerate(reader):

            print(
                "Processing row {} of {} with word name: {}".format(
                    i + 1, len(reader), row["word_name"]
                )
            )

            theme = row["theme"]
            deck = row["deck_name"]
            name_ac = row["word_name"]
            word_counter = str(row["public_word_id"])[4:]
            name = unaccentify(row["word_name"])
            wordclass_id = int(row["word_class"])
            wordclass = str()
            for key in enums.wordclasses:
                if wordclass_id == key:
                    wordclass = enums.wordclasses[key]
            output = "output"
            level = "A1"
            PATH = f"./{output}/{level}/{theme}/{deck}"
            os.makedirs(PATH, exist_ok=True)
            dataMap = dict()
            wordclass_template = f"./templates/{wordclass}.yaml"

            with open(wordclass_template, "r") as template:
                dataMap = yaml.safe_load(template)
                dataMap["name"] = name
                dataMap["name_ac"] = name_ac
                dataMap["wordcls"] = wordclass
                dataMap["translation"] = []
                dataMap["publ_id"] = int(f"1{theme[:1]}{deck[:2]}{word_counter}")

                parse_headers(headers, dataMap=dataMap, row=row)
                parse_translations(translations, dataMap=dataMap, row=row)

            with open(f"{PATH}/{word_counter} {name}.yaml", "w") as template:

                ruyaml = ruyml.YAML()
                ruyaml.indent(sequence=4, offset=3)
                ruyaml.dump(dataMap, template)
