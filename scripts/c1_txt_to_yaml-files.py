import ruamel.yaml as ruyml
import os

c1 = open("files/only_new_in_c1.txt", "r")
c1_lines = c1.read()
c1_list = c1_lines.split("\n")
c1_list = list(filter(None, c1_list))
print(len(sorted(c1_list)))
PATH = "c1"
if not os.path.exists(PATH):
    os.makedirs(PATH)
for line in c1_list:
    line = line.rstrip(".!")
    with open(f"{PATH}/{line}.yaml", "w") as template:
        ruyaml = ruyml.YAML()
        ruyaml.indent(sequence=4, offset=3)
        ruyaml.dump({"name": line}, template)
