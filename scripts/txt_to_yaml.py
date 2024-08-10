import ruamel.yaml as ruyml
import os

b2 = open("files/new_b2.txt", "r")
b2_lines = b2.read()
b2_list = b2_lines.split("\n")
b2_list = list(filter(None, b2_list))
print(len(sorted(b2_list)))
PATH = "b2"
if not os.path.exists(PATH):
    os.makedirs(PATH)
for line in b2_list:
    line = line.rstrip(".!")
    with open(f"{PATH}/{line}.yaml", "w") as template:
        ruyaml = ruyml.YAML()
        ruyaml.indent(sequence=4, offset=3)
        ruyaml.dump({"name": line}, template)
