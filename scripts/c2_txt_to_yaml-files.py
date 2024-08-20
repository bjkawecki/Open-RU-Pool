import ruamel.yaml as ruyml
import os

c2 = open("files/only_new_in_c2.txt", "r")
c2_lines = c2.read()
c2_list = c2_lines.split("\n")
c2_list = list(filter(None, c2_list))
print(len(sorted(c2_list)))
PATH = "c2"
if not os.path.exists(PATH):
    os.makedirs(PATH)
for line in c2_list:
    line = line.rstrip(".!")
    with open(f"{PATH}/{line}.yaml", "w") as template:
        ruyaml = ruyml.YAML()
        ruyaml.indent(sequence=4, offset=3)
        ruyaml.dump({"name": line}, template)
